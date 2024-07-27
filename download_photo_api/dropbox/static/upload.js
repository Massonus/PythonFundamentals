// Добавляем обработчик события для формы с id 'fileForm'
document.getElementById('fileForm').addEventListener('submit', async function (event) {
    event.preventDefault(); // Предотвращаем стандартное поведение формы (перезагрузку страницы)

    const fileInput = document.getElementById('fileInput'); // Получаем элемент input для файла
    const file = fileInput.files[0]; // Получаем первый выбранный файл

    if (file) { // Проверяем, выбран ли файл
        const reader = new FileReader(); // Создаем объект FileReader для чтения файла
        reader.onload = async function (event) { // Устанавливаем функцию-обработчик для события onload
            const base64String = event.target.result.split(',')[1]; // Извлекаем Base64-строку из результата чтения файла

            // Создаем JSON-пayload с информацией о файле
            const jsonPayload = JSON.stringify({
                fileName: file.name,
                fileType: file.type,
                fileData: base64String
            });

            // Получаем токен доступа от Dropbox, отправляя запрос на сервер
            const tokenResponse = await fetch('/get_dropbox_token');
            if (tokenResponse.ok) { // Проверяем, успешен ли запрос
                const tokenData = await tokenResponse.json(); // Извлекаем данные токена из ответа
                const dropboxToken = tokenData.access_token; // Получаем access_token

                // Отправляем запрос на сервер для загрузки файла на Dropbox
                const response = await fetch('/upload', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json', // Указываем, что отправляем JSON
                        'Authorization': `Bearer ${dropboxToken}` // Добавляем токен авторизации в заголовок
                    },
                    body: jsonPayload // Отправляем JSON-пayload с информацией о файле
                });

                if (response.ok) { // Проверяем, успешен ли запрос
                    const data = await response.json(); // Извлекаем данные из ответа
                    console.log('Success:', data); // Логируем успешный ответ
                } else {
                    console.error('Error:', response.statusText); // Логируем ошибку, если запрос неуспешен
                }
            } else {
                console.error('Error fetching Dropbox token:', tokenResponse.statusText); // Логируем ошибку при получении токена
            }
        };

        reader.readAsDataURL(file); // Начинаем чтение файла как Data URL (Base64 строка)
    } else {
        alert('Please select a file!'); // Показываем предупреждение, если файл не выбран
    }
});
