from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# Замените на ваш API ключ Imgbb
IMGBB_API_KEY = '791b9b9141f84a37a8427f94c581d67e'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    files = {'image': file.read()}
    response = requests.post(f'https://api.imgbb.com/1/upload?key={IMGBB_API_KEY}', files=files)

    if response.status_code != 200:
        return jsonify({'error': 'Failed to upload to Imgbb'}), 500

    response_data = response.json()
    image_url = response_data['data']['url']
    delete_url = response_data['data']['delete_url']

    return jsonify({'url': image_url, 'delete_url': delete_url})


@app.route('/delete', methods=['POST'])
def delete_file():
    data = request.get_json()
    delete_url = data.get('delete_url')

    if not delete_url:
        return jsonify({'error': 'No delete URL provided'}), 400

    response = requests.delete(delete_url)

    if response.status_code != 200:
        return jsonify({'error': 'Failed to delete image'}), 500

    return jsonify({'message': 'Image deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True)
