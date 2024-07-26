document.getElementById('fileForm').addEventListener('submit', async function(event) {
    event.preventDefault(); // Prevent the form from submitting the traditional way

    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];

    if (file) {
        const reader = new FileReader();
        reader.onload = async function(event) {
            const base64String = event.target.result.split(',')[1];

            const jsonPayload = JSON.stringify({
                fileName: file.name,
                fileType: file.type,
                fileData: base64String
            });

            // Получение токена доступа от Dropbox
            const tokenResponse = await fetch('/get_dropbox_token');
            if (tokenResponse.ok) {
                const tokenData = await tokenResponse.json();
                const dropboxToken = tokenData.access_token;

                const response = await fetch('/upload', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${dropboxToken}`
                    },
                    body: jsonPayload
                });

                if (response.ok) {
                    const data = await response.json();
                    console.log('Success:', data);
                } else {
                    console.error('Error:', response.statusText);
                }
            } else {
                console.error('Error fetching Dropbox token:', tokenResponse.statusText);
            }
        };

        reader.readAsDataURL(file);
    } else {
        alert('Please select a file!');
    }
});
