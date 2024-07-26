from flask import Flask, redirect, url_for, session, request, render_template, jsonify
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
import requests
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'static/uploads'

CLIENT_SECRETS_FILE = "client_secret.json"
SCOPES = ['https://www.googleapis.com/auth/photoslibrary']


@app.route('/')
def index():
    return render_template('index.html')


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
    return redirect(authorization_url)


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
    session['credentials'] = credentials_to_dict(credentials)
    return render_template('upload.html')


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
    file.save(file_path)

    upload_token = upload_file(credentials, file_path)

    if upload_token:
        create_album(credentials, file.filename, upload_token)
        return jsonify({'message': 'File uploaded successfully'})
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


def create_album(credentials, album_title, upload_token):
    headers = {
        'Authorization': 'Bearer {}'.format(credentials.token),
        'Content-Type': 'application/json'
    }
    album_body = {
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
        json=album_body
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
    context = ('server.crt', 'server.key')  # Путь к сертификату и ключу
    app.run(host='localhost', port=5000, ssl_context=context, debug=True)
