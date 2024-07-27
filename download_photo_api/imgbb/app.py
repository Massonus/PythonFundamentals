import os

import requests
from dotenv import load_dotenv  # Модуль для загрузки переменных среды из файла .env
from flask import Flask, request, jsonify, render_template  # Импорт необходимых классов и функций из Flask

# Загрузка секретов из файла .env, который должен быть в основной директории
dotenv_path = os.path.join(os.path.dirname(__file__), '..', 'dev.env')
load_dotenv(dotenv_path=dotenv_path)

app = Flask(__name__)  # Инициализация приложения Flask

# Замените на ваш API ключ Imgbb, загруженный из переменной среды
IMGBB_API_KEY = os.getenv("IMGBB_API_KEY")


@app.route('/')
def index():
    return render_template('index.html')  # Отображение главной страницы


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400  # Проверка, что файл присутствует в запросе

    file = request.files['file']
    files = {'image': file.read()}  # Чтение содержимого файла для отправки на Imgbb
    response = requests.post(f'https://api.imgbb.com/1/upload?key={IMGBB_API_KEY}', files=files)

    if response.status_code != 200:
        return jsonify({'error': 'Failed to upload to Imgbb'}), 500  # Проверка на успешность загрузки файла

    response_data = response.json()
    image_url = response_data['data']['url']  # Получение URL загруженного изображения
    delete_url = response_data['data']['delete_url']  # Получение URL для удаления изображения

    return jsonify({'url': image_url, 'delete_url': delete_url})  # Возвращаем URL изображения и URL для его удаления


@app.route('/delete', methods=['POST'])
def delete_file():
    data = request.get_json()
    delete_url = data.get('delete_url')

    if not delete_url:
        return jsonify({'error': 'No delete URL provided'}), 400  # Проверка, что URL для удаления присутствует

    response = requests.delete(delete_url)

    if response.status_code != 200:
        return jsonify({'error': 'Failed to delete image'}), 500  # Проверка на успешность удаления изображения

    return jsonify({'message': 'Image deleted successfully'})  # Возвращаем сообщение об успешном удалении


if __name__ == '__main__':
    app.run(debug=True)  # Запуск приложения в режиме отладки
