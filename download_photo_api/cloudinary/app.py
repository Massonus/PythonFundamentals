import os
import base64
import cloudinary
import cloudinary.uploader
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template

# Загрузка секретов из файла .env
dotenv_path = os.path.join(os.path.dirname(__file__), '..', 'dev.env')
load_dotenv(dotenv_path=dotenv_path)

app = Flask(__name__)

# Настройка Cloudinary
cloudinary.config(
    cloud_name=os.getenv("CLOUD_NAME"),
    api_key=os.getenv("API_KEY"),
    api_secret=os.getenv("API_SECRET")
)

# Папка для загрузки изображений
MAIN_FOLDER = 'ConnectX'
SUB_FOLDER = 'rates'
UPLOAD_FOLDER = f'{MAIN_FOLDER}/{SUB_FOLDER}'  # Вложенная структура папок


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    data = request.get_json()
    if 'file_data' not in data or 'file_name' not in data:
        return jsonify({'error': 'No file data or file name provided'}), 400

    file_data = data['file_data']
    file_name = data['file_name']

    try:
        # Декодируем Base64 в бинарные данные
        decoded_file_data = base64.b64decode(file_data)

        # Загружаем изображение на Cloudinary
        upload_result = cloudinary.uploader.upload(decoded_file_data, folder=UPLOAD_FOLDER, public_id=file_name)

        if not upload_result:
            return jsonify({'error': 'Failed to upload to Cloudinary'}), 500

        image_url = upload_result['secure_url']
        public_id = upload_result['public_id']

        return jsonify({'url': image_url, 'public_id': public_id})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/delete', methods=['POST'])
def delete_file():
    data = request.get_json()
    public_id = data.get('public_id')

    if not public_id:
        return jsonify({'error': 'No public ID provided'}), 400

    delete_result = cloudinary.uploader.destroy(public_id)

    if delete_result.get('result') != 'ok':
        return jsonify({'error': 'Failed to delete image'}), 500

    return jsonify({'message': 'Image deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True)
