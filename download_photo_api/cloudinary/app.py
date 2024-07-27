import os
import base64
import cloudinary
import cloudinary.uploader
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template

# Загрузка секретов из файла .env
# .env файл содержит конфиденциальные данные, такие как ключи API
dotenv_path = os.path.join(os.path.dirname(__file__), '..', 'dev.env')
load_dotenv(dotenv_path=dotenv_path)

app = Flask(__name__)

# Настройка Cloudinary с использованием переменных окружения
# Эти переменные содержат информацию для аутентификации в Cloudinary
cloudinary.config(
    cloud_name=os.getenv("CLOUD_NAME"),
    api_key=os.getenv("API_KEY"),
    api_secret=os.getenv("API_SECRET")
)

# Определение вложенной структуры папок для загрузки изображений
MAIN_FOLDER = 'ConnectX'
SUB_FOLDER = 'rates'
UPLOAD_FOLDER = f'{MAIN_FOLDER}/{SUB_FOLDER}'  # Путь к папке загрузки


@app.route('/')
def index():
    # Отображение главной страницы
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    # Получение JSON данных из запроса
    data = request.get_json()

    # Проверка наличия данных файла и имени файла в запросе
    if 'file_data' not in data or 'file_name' not in data:
        return jsonify({'error': 'No file data or file name provided'}), 400

    # Получение данных файла и имени файла из JSON
    file_data = data['file_data']
    file_name = data['file_name']

    try:
        # Декодирование данных файла из Base64 в бинарный формат
        decoded_file_data = base64.b64decode(file_data)

        # Загрузка изображения в Cloudinary
        upload_result = cloudinary.uploader.upload(decoded_file_data, folder=UPLOAD_FOLDER, public_id=file_name)

        # Проверка успешности загрузки
        if not upload_result:
            return jsonify({'error': 'Failed to upload to Cloudinary'}), 500

        # Получение URL загруженного изображения и публичного ID
        image_url = upload_result['secure_url']
        public_id = upload_result['public_id']

        # Возвращение JSON ответа с URL и публичным ID изображения
        return jsonify({'url': image_url, 'public_id': public_id})

    except Exception as e:
        # Обработка ошибок и возвращение сообщения об ошибке
        return jsonify({'error': str(e)}), 500


@app.route('/delete', methods=['POST'])
def delete_file():
    # Получение JSON данных из запроса
    data = request.get_json()
    public_id = data.get('public_id')

    # Проверка наличия публичного ID в запросе
    if not public_id:
        return jsonify({'error': 'No public ID provided'}), 400

    # Удаление изображения из Cloudinary
    delete_result = cloudinary.uploader.destroy(public_id)

    # Проверка успешности удаления
    if delete_result.get('result') != 'ok':
        return jsonify({'error': 'Failed to delete image'}), 500

    # Возвращение сообщения об успешном удалении
    return jsonify({'message': 'Image deleted successfully'})


if __name__ == '__main__':
    # Запуск Flask приложения
    app.run(debug=True)
