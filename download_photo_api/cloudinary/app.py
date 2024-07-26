import os

import cloudinary
import cloudinary.uploader
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template

# download secrets from .env file that should be in the main directory
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
UPLOAD_FOLDER = 'my_images'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    # Загрузка изображения в указанную папку
    upload_result = cloudinary.uploader.upload(file, folder=UPLOAD_FOLDER)

    if not upload_result:
        return jsonify({'error': 'Failed to upload to Cloudinary'}), 500

    image_url = upload_result['secure_url']
    public_id = upload_result['public_id']

    return jsonify({'url': image_url, 'public_id': public_id})


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
