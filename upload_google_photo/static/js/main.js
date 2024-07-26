document.getElementById('upload-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    const fileInput = document.getElementById('file-input');
    const file = fileInput.files[0];

    if (file) {
        const formData = new FormData();
        formData.append('file', file);

        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();
        if (result.url) {
            alert(`File uploaded successfully! URL: ${result.url}`);
        } else {
            alert('File upload failed.');
        }
    }
});
