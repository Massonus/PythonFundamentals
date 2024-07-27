import base64
import os
from urllib.parse import urlencode

import dropbox
import dropbox.exceptions
import requests
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template, redirect, url_for, session

# Загружаем секретные данные из файла .env, который должен быть в основной директории
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '..', 'dev.env')
load_dotenv(dotenv_path=dotenv_path)

# Создаём экземпляр Flask приложения
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Устанавливаем секретный ключ для сессий

# Эти переменные должны быть установлены вашим OAuth2 провайдером (например, Dropbox)
DROPBOX_APP_KEY = os.getenv("DROPBOX_APP_KEY")
DROPBOX_APP_SECRET = os.getenv("DROPBOX_APP_SECRET")

# Получите эти URL из настроек вашего приложения Dropbox
REDIRECT_URI = 'http://localhost:5000/oauth2/callback'


@app.route('/')
def index():
    if 'refresh_token' not in session:
        return redirect(url_for('authorize'))  # Перенаправляем на авторизацию, если нет refresh токена
    return render_template('index.html')  # Отображаем шаблон index.html


@app.route('/authorize')
def authorize():
    auth_url = 'https://www.dropbox.com/oauth2/authorize?' + urlencode({
        'client_id': DROPBOX_APP_KEY,
        'response_type': 'code',
        'redirect_uri': REDIRECT_URI,
        'token_access_type': 'offline'
    })
    return redirect(auth_url)  # Перенаправляем пользователя на страницу авторизации Dropbox


@app.route('/oauth2/callback')
def oauth2_callback():
    code = request.args.get('code')  # Получаем код авторизации из URL
    response = requests.post('https://api.dropboxapi.com/oauth2/token', data={
        'code': code,
        'grant_type': 'authorization_code',
        'client_id': DROPBOX_APP_KEY,
        'client_secret': DROPBOX_APP_SECRET,
        'redirect_uri': REDIRECT_URI
    })

    if response.status_code == 200:
        token_data = response.json()
        session['refresh_token'] = token_data['refresh_token']  # Сохраняем refresh токен в сессии
        return redirect(url_for('index'))  # Перенаправляем на главную страницу
    else:
        return 'Error: Failed to get refresh token', 400  # Ошибка, если не удалось получить refresh токен


@app.route('/get_dropbox_token', methods=['GET'])
def get_dropbox_token():
    if 'refresh_token' not in session:
        return jsonify({'error': 'Not authorized'}), 401  # Ошибка, если пользователь не авторизован

    # Используем refresh token для получения нового access token
    response = requests.post('https://api.dropboxapi.com/oauth2/token', data={
        'grant_type': 'refresh_token',
        'refresh_token': session['refresh_token'],
        'client_id': DROPBOX_APP_KEY,
        'client_secret': DROPBOX_APP_SECRET
    })

    if response.status_code == 200:
        return jsonify(response.json())  # Возвращаем новый access token в формате JSON
    else:
        return jsonify(
            {'error': 'Failed to get Dropbox token'}), response.status_code  # Ошибка, если не удалось получить токен


@app.route('/upload', methods=['POST'])
def upload_file():
    data = request.get_json()  # Получаем данные из POST запроса
    token = request.headers.get('Authorization').split(' ')[1]  # Получаем токен из заголовков запроса

    file_name = data['fileName']
    file_data = data['fileData']

    # Декодируем данные файла из Base64
    file_bytes = base64.b64decode(file_data)

    # Инициализируем клиент Dropbox с полученным токеном
    dbx = dropbox.Dropbox(token)

    try:
        # Загружаем файл на Dropbox
        dbx.files_upload(file_bytes, f'/{file_name}')
        return jsonify({'message': 'File uploaded successfully to Dropbox!', 'file': file_name})
    except dropbox.exceptions.ApiError as err:
        print('Dropbox API error:', err)
        return jsonify({'message': 'Failed to upload file to Dropbox',
                        'error': str(err)}), 500  # Ошибка, если не удалось загрузить файл


if __name__ == '__main__':
    app.run(debug=True)  # Запускаем приложение в режиме отладки
