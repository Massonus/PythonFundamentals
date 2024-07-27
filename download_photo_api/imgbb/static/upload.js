// Добавляем обработчик события для формы загрузки
document.getElementById('uploadForm').addEventListener('submit', async function (event) {
    event.preventDefault();  // Предотвращаем отправку формы по умолчанию

    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];  // Получаем первый выбранный файл

    if (!file) {
        alert('Please select a file!');  // Если файл не выбран, показываем предупреждение
        return;
    }

    const formData = new FormData();
    formData.append('file', file);  // Добавляем файл в объект FormData

    try {
        // Отправляем файл на сервер с использованием fetch
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error('Failed to upload file');  // Если ответ не успешный, выбрасываем ошибку
        }

        const data = await response.json();
        document.getElementById('result').innerText = `Image URL: ${data.url}`;  // Отображаем URL загруженного изображения
        document.getElementById('deleteButton').style.display = 'block';  // Показываем кнопку удаления

        console.log('Image URL:', data.url);
        localStorage.setItem('deleteUrl', data.delete_url);  // Сохраняем URL для удаления в localStorage

    } catch (error) {
        console.error('Error:', error);
        document.getElementById('result').innerText = 'Error uploading file';  // Отображаем сообщение об ошибке
    }
});

// Добавляем обработчик события для кнопки удаления
document.getElementById('deleteButton').addEventListener('click', async function () {
    const deleteUrl = localStorage.getItem('deleteUrl');  // Получаем URL для удаления из localStorage
    if (!deleteUrl) {
        alert('No image to delete!');  // Если URL для удаления не найден, показываем предупреждение
        return;
    }

    try {
        // Отправляем запрос на удаление изображения
        const response = await fetch('/delete', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({delete_url: deleteUrl})  // Отправляем URL для удаления в формате JSON
        });

        if (!response.ok) {
            throw new Error('Failed to delete image');  // Если ответ не успешный, выбрасываем ошибку
        }

        const data = await response.json();
        document.getElementById('result').innerText = data.message;  // Отображаем сообщение об успешном удалении
        document.getElementById('deleteButton').style.display = 'none';  // Скрываем кнопку удаления
        localStorage.removeItem('deleteUrl');  // Удаляем URL для удаления из localStorage

        console.log(data.message);

    } catch (error) {
        console.error('Error:', error);
        document.getElementById('result').innerText = 'Error deleting image';  // Отображаем сообщение об ошибке
    }
});
