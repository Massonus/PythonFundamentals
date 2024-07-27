from flask import Flask, redirect, url_for, session, request, render_template, jsonify
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from flask_sqlalchemy import SQLAlchemy
import requests
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Устанавливаем секретный ключ для сессий
app.config['UPLOAD_FOLDER'] = 'static/uploads'  # Папка для загрузки файлов
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tokens.db'  # Настройка базы данных
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)  # Инициализация SQLAlchemy для работы с базой данных

CLIENT_SECRETS_FILE = os.path.join(os.path.dirname(__file__), 'client_secret.json')  # Файл с клиентскими секретами
SCOPES = sorted([
    'https://www.googleapis.com/auth/photoslibrary.sharing',
    'https://www.googleapis.com/auth/userinfo.profile',
    'openid',
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/photoslibrary'
])


# Модель для хранения токенов в базе данных
class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(500), nullable=False)
    refresh_token = db.Column(db.String(500), nullable=False)
    token_uri = db.Column(db.String(500), nullable=False)
    client_id = db.Column(db.String(500), nullable=False)
    client_secret = db.Column(db.String(500), nullable=False)
    scopes = db.Column(db.String(500), nullable=False)


@app.route('/')
def index():
    return redirect(url_for('upload_page'))  # Перенаправляем на страницу загрузки файлов


@app.route('/upload')
def upload_page():
    if 'credentials' not in session:
        token = Token.query.first()
        if token:
            credentials = Credentials(
                token=token.token,
                refresh_token=token.refresh_token,
                token_uri=token.token_uri,
                client_id=token.client_id,
                client_secret=token.client_secret,
                scopes=token.scopes.split(',')
            )
            if credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())
                token.token = credentials.token
                db.session.commit()
                session['credentials'] = credentials_to_dict(credentials)
        else:
            return redirect(url_for('authorize'))

    return render_template('upload.html')  # Отображаем шаблон upload.html


@app.route('/authorize')
def authorize():
    session.clear()  # Очистка сессии перед авторизацией
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=SCOPES,
        redirect_uri='https://localhost:5000/oauth2callback'
    )
    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true'
    )
    session['state'] = state
    return redirect(authorization_url)  # Перенаправляем пользователя на страницу авторизации Google


@app.route('/oauth2callback')
def oauth2callback():
    state = session.get('state')
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=SCOPES,
        state=state,
        redirect_uri='https://localhost:5000/oauth2callback'
    )
    flow.fetch_token(authorization_response=request.url)
    credentials = flow.credentials

    token = Token.query.first()
    if token:
        db.session.delete(token)  # Удаляем старый токен из базы данных
    new_token = Token(
        token=credentials.token,
        refresh_token=credentials.refresh_token,
        token_uri=credentials.token_uri,
        client_id=credentials.client_id,
        client_secret=credentials.client_secret,
        scopes=','.join(credentials.scopes)
    )
    db.session.add(new_token)
    db.session.commit()

    session['credentials'] = credentials_to_dict(credentials)
    return redirect(url_for('upload_page'))  # Перенаправляем на страницу загрузки файлов


@app.route('/upload', methods=['POST'])
def upload():
    if 'credentials' not in session:
        return redirect(url_for('authorize'))

    credentials = Credentials(
        token=session['credentials']['token'],
        refresh_token=session['credentials']['refresh_token'],
        token_uri=session['credentials']['token_uri'],
        client_id=session['credentials']['client_id'],
        client_secret=session['credentials']['client_secret'],
        scopes=session['credentials']['scopes']
    )

    file = request.files['file']
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)  # Сохраняем файл в указанную папку

    upload_token = upload_file(credentials, file_path)

    if upload_token:
        media_item_info = create_media_item(credentials, upload_token)
        if media_item_info:
            # Создание и публикация альбома
            album_id = create_album(credentials, 'Uploaded Album')
            if album_id:
                add_media_to_album(credentials, album_id, media_item_info['id'])
                publish_album(credentials, album_id)
                image_url = media_item_info['productUrl']
                print(f"Public URL: {image_url}")
                os.remove(file_path)  # Удаляем файл из папки uploads
                return jsonify({'message': 'File uploaded successfully', 'url': image_url})
            else:
                return jsonify({'message': 'Failed to create or share album'})
        else:
            return jsonify({'message': 'Failed to retrieve media item info'})
    else:
        return jsonify({'message': 'File upload failed'})


def upload_file(credentials, file_path):
    headers = {
        'Authorization': 'Bearer {}'.format(credentials.token),
        'Content-Type': 'application/octet-stream',
        'X-Goog-Upload-File-Name': os.path.basename(file_path),
        'X-Goog-Upload-Protocol': 'raw'
    }
    with open(file_path, 'rb') as file:
        response = requests.post(
            'https://photoslibrary.googleapis.com/v1/uploads',
            headers=headers,
            data=file
        )
    if response.status_code == 200:
        return response.content.decode('utf-8')
    return None


def create_media_item(credentials, upload_token):
    headers = {
        'Authorization': 'Bearer {}'.format(credentials.token),
        'Content-Type': 'application/json'
    }
    media_item_body = {
        'newMediaItems': [
            {
                'description': 'Uploaded by Flask app',
                'simpleMediaItem': {'uploadToken': upload_token}
            }
        ]
    }
    response = requests.post(
        'https://photoslibrary.googleapis.com/v1/mediaItems:batchCreate',
        headers=headers,
        json=media_item_body
    )
    if response.status_code == 200:
        media_item = response.json().get('newMediaItemResults')[0].get('mediaItem')
        return media_item
    return None


def create_album(credentials, album_title):
    headers = {
        'Authorization': 'Bearer {}'.format(credentials.token),
        'Content-Type': 'application/json'
    }
    album_body = {
        'album': {'title': album_title}
    }
    response = requests.post(
        'https://photoslibrary.googleapis.com/v1/albums',
        headers=headers,
        json=album_body
    )
    if response.status_code == 200:
        album_id = response.json().get('id')
        return album_id
    return None


def add_media_to_album(credentials, album_id, media_id):
    headers = {
        'Authorization': 'Bearer {}'.format(credentials.token),
        'Content-Type': 'application/json'
    }
    add_media_body = {
        'mediaItemIds': [media_id]
    }
    response = requests.post(
        f'https://photoslibrary.googleapis.com/v1/albums/{album_id}:batchAddMediaItems',
        headers=headers,
        json=add_media_body
    )
    return response.status_code == 200


def publish_album(credentials, album_id):
    headers = {
        'Authorization': 'Bearer {}'.format(credentials.token),
        'Content-Type': 'application/json'
    }
    share_body = {
        'mediaItems': [{
            'id': album_id
        }],
        'shareInfo': {
            'shareable': True
        }
    }
    response = requests.post(
        f'https://photoslibrary.googleapis.com/v1/albums/{album_id}:share',
        headers=headers,
        json=share_body
    )
    return response.status_code == 200


def credentials_to_dict(credentials):
    return {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }


if __name__ == '__main__':
    crt = os.path.join(os.path.dirname(__file__), '..', '..', 'nginx-selfsigned.crt')
    key = os.path.join(os.path.dirname(__file__), '..', '..', 'nginx-selfsigned.key')
    context = (crt, key)  # Путь к сертификату и ключу
    with app.app_context():
        db.create_all()  # Создаем все таблицы в базе данных
    app.run(host='localhost', port=5000, ssl_context=context, debug=True)  # Запуск приложения с SSL и в режиме отладки
