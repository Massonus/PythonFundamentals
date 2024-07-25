# ConnectX

ConnectX is an internet provider project utilizing technologies such as Python, Flask, PostgreSQL, HTML, CSS, and JavaScript.

## Installation

1. Clone the repository:
    ```bash
    git clone <repository URL>
    ```
2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
3. Activate the virtual environment and install dependencies:
    ```bash
    source venv/bin/activate  # for Linux/Mac
    venv\Scripts\activate  # for Windows
    pip install -r requirements.txt
    ```
4. Create a `dev.env` file in the root directory of the project and add the following parameters:
    ```env
    RECAPTCHA_SECRET_KEY=your_secret_key
    RECAPTCHA_SITE_KEY=your_secret_key
    APPLICATION_SECRET_KEY=your_flask_app_secret_key
    INITIALIZE_DB_ENGINE=postgresql+psycopg://postgres:root@localhost/ConnectX
    ```
5. Install PostgreSQL from [here](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) and create the ConnectX database as shown in the image:
    ![pgAdmin4](image.png)
    - Username: `postgres`
    - Password: `root`
    - Database name: `ConnectX`

6. If the server is not created, register a new server:
    - Right-click on `servers` -> `register` -> `server..`
    - Enter the server name
    - In the `connection` tab, enter `localhost` in the `Host name/address` field

## Usage

1. Run the application:
    ```bash
    flask run
    ```

2. Access the application in your web browser at `http://localhost:5000`.

3. Register a new user and log in to access the features.

4. The application includes functionalities for managing internet provider services, user accounts, and administrative tasks.

## Authors

- Maksym Lithuanian
- Andriy Zhornyak
- Danylo Voloshyn
- Oleksandra Vedmid

## License

This project is licensed under the MIT License.
