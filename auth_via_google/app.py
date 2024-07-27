from flask import Flask, redirect, url_for, session, request, jsonify, render_template
from authlib.integrations.flask_client import OAuth
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id='66208709014-l7tr5ttaalp10mkookpfae1rhihhd1f6.apps.googleusercontent.com',
    client_secret='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',
    access_token_url='https://oauth2.googleapis.com/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    client_kwargs={'scope': 'email profile'},
    redirect_uri='https://127.0.0.1:5000/login/authorized'
)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    redirect_uri = url_for('authorized', _external=True)
    return google.authorize_redirect(redirect_uri)


@app.route('/logout')
def logout():
    session.pop('user')
    return redirect(url_for('index'))


@app.route('/login/authorized')
def authorized():
    token = google.authorize_access_token()
    resp = google.get('https://www.googleapis.com/oauth2/v3/userinfo')
    user_info = resp.json()
    session['user'] = user_info
    return jsonify(user_info)


if __name__ == '__main__':
    app.run(ssl_context=('server.crt', 'server.key'), debug=True)
