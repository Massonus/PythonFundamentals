from flask import Flask, request, jsonify, render_template
import cloudinary
import cloudinary.uploader

app = Flask(__name__)

# Настройка Cloudinary
cloudinary.config(
    cloud_name='dirk598i2',
    api_key='967978327629942',
    api_secret='XdO2dvFYc8cewAt3R_rIR5q50rg'
)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    upload_result = cloudinary.uploader.upload(file)

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
