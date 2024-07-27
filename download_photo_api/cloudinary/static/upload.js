// Добавление слушателя событий к форме загрузки
// Эта функция будет вызываться, когда пользователь отправляет форму
document.getElementById('uploadForm').addEventListener('submit', async function (event) {
    event.preventDefault(); // Предотвращение стандартного действия отправки формы

    // Получение файла из элемента input
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];

    // Проверка, выбран ли файл
    if (!file) {
        alert('Please select a file!'); // Если файл не выбран, показываем предупреждение
        return;
    }

    // Чтение файла и преобразование его в Base64
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = async function () {
        const base64Data = reader.result.split(',')[1]; // Получение только данных Base64 без префикса

        // Подготовка JSON данных для отправки на сервер
        const jsonData = JSON.stringify({
            file_data: base64Data,  // Данные файла в формате Base64
            file_name: file.name    // Имя файла
        });

        try {
            // Отправка запроса на сервер с JSON данными
            const response = await fetch('/upload', {
                method: 'POST', // Метод POST используется для загрузки файла
                headers: {
                    'Content-Type': 'application/json' // Установка типа контента как JSON
                },
                body: jsonData // Тело запроса содержит JSON данные
            });

            // Проверка успешности запроса
            if (!response.ok) {
                throw new Error('Failed to upload file'); // В случае ошибки выбрасываем исключение
            }

            // Получение и обработка ответа от сервера
            const data = await response.json();
            document.getElementById('result').innerText = `Image URL: ${data.url}`; // Отображение URL изображения
            document.getElementById('deleteButton').style.display = 'block'; // Показ кнопки удаления

            console.log('Image URL:', data.url); // Логирование URL изображения в консоль
            localStorage.setItem('publicId', data.public_id); // Сохранение публичного ID изображения в localStorage

        } catch (error) {
            console.error('Error:', error); // Логирование ошибок
            document.getElementById('result').innerText = 'Error uploading file'; // Отображение сообщения об ошибке
        }
    };
});

// Добавление слушателя событий к кнопке удаления
document.getElementById('deleteButton').addEventListener('click', async function () {
    const publicId = localStorage.getItem('publicId'); // Получение публичного ID из localStorage
    if (!publicId) {
        alert('No image to delete!'); // Если публичный ID отсутствует, показываем предупреждение
        return;
    }

    try {
        // Отправка запроса на удаление изображения по публичному ID
        const response = await fetch('/delete', {
            method: 'POST', // Метод POST используется для удаления файла
            headers: {
                'Content-Type': 'application/json' // Установка типа контента как JSON
            },
            body: JSON.stringify({public_id: publicId}) // Тело запроса содержит публичный ID изображения
        });

        // Проверка успешности запроса
        if (!response.ok) {
            throw new Error('Failed to delete image'); // В случае ошибки выбрасываем исключение
        }

        // Получение и обработка ответа от сервера
        const data = await response.json();
        document.getElementById('result').innerText = data.message; // Отображение сообщения об удалении
        document.getElementById('deleteButton').style.display = 'none'; // Скрытие кнопки удаления
        localStorage.removeItem('publicId'); // Удаление публичного ID из localStorage

        console.log(data.message); // Логирование сообщения в консоль

    } catch (error) {
        console.error('Error:', error); // Логирование ошибок
        document.getElementById('result').innerText = 'Error deleting image'; // Отображение сообщения об ошибке
    }
});
