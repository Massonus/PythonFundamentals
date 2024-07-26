document.getElementById('uploadForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];

    if (!file) {
        alert('Please select a file!');
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error('Failed to upload file');
        }

        const data = await response.json();
        document.getElementById('result').innerText = `Image URL: ${data.url}`;
        document.getElementById('deleteButton').style.display = 'block';

        console.log('Image URL:', data.url);
        localStorage.setItem('publicId', data.public_id);

    } catch (error) {
        console.error('Error:', error);
        document.getElementById('result').innerText = 'Error uploading file';
    }
});

document.getElementById('deleteButton').addEventListener('click', async function() {
    const publicId = localStorage.getItem('publicId');
    if (!publicId) {
        alert('No image to delete!');
        return;
    }

    try {
        const response = await fetch('/delete', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ public_id: publicId })
        });

        if (!response.ok) {
            throw new Error('Failed to delete image');
        }

        const data = await response.json();
        document.getElementById('result').innerText = data.message;
        document.getElementById('deleteButton').style.display = 'none';
        localStorage.removeItem('publicId');

        console.log(data.message);

    } catch (error) {
        console.error('Error:', error);
        document.getElementById('result').innerText = 'Error deleting image';
    }
});
