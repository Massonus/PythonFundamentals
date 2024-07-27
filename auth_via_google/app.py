import os
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, redirect, url_for, session

# Загружаем секретные данные из файла .env, который должен быть в основной директории
dotenv_path = os.path.join(os.path.dirname(__file__), '..', 'dev.env')
load_dotenv(dotenv_path=dotenv_path)

# Создаём экземпляр Flask приложения
app = Flask(__name__)
app.secret_key = os.urandom(24)  # Устанавливаем секретный ключ для сессий

# Настраиваем OAuth с помощью библиотеки Authlib
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id=os.getenv("GOOGLE_CLIENT_ID"),  # ID клиента Google из .env файла
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),  # Секрет клиента Google из .env файла
    access_token_url='https://oauth2.googleapis.com/token',  # URL для получения токена доступа
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',  # URL для авторизации
    authorize_params=None,
    client_kwargs={'scope': 'email profile'},  # Области доступа, запрашиваемые у пользователя
    redirect_uri='https://127.0.0.1:5000/login/authorized'  # URL для перенаправления после авторизации
)


# Главная страница
@app.route('/')
def index():
    return render_template('index.html')  # Отображаем шаблон index.html


# Страница для входа
@app.route('/login')
def login():
    redirect_uri = url_for('authorized', _external=True)  # Генерируем URL для перенаправления после авторизации
    return google.authorize_redirect(redirect_uri)  # Перенаправляем пользователя на страницу авторизации Google


# Страница для выхода
@app.route('/logout')
def logout():
    session.pop('user')  # Удаляем данные пользователя из сессии
    return redirect(url_for('index'))  # Перенаправляем пользователя на главную страницу


# Страница для обработки авторизации
@app.route('/login/authorized')
def authorized():
    token = google.authorize_access_token()  # Получаем токен доступа
    resp = google.get('https://www.googleapis.com/oauth2/v3/userinfo')  # Запрашиваем информацию о пользователе
    user_info = resp.json()  # Преобразуем ответ в JSON
    session['user'] = user_info  # Сохраняем информацию о пользователе в сессии
    return jsonify(user_info)  # Возвращаем информацию о пользователе в формате JSON


# Запуск приложения
if __name__ == '__main__':
    crt = os.path.join(os.path.dirname(__file__), '..', 'nginx-selfsigned.crt')
    key = os.path.join(os.path.dirname(__file__), '..', 'nginx-selfsigned.key')
    app.run(ssl_context=(crt, key), debug=True)
    # Запускаем приложение с использованием SSL-сертификата и ключа
    # и включённым режимом отладки
