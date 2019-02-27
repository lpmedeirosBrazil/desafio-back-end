from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

from desafio_oglobo import crawler

users = {
    "galleani": "123",
    "rafael": "123"
}


@auth.get_password
def get_password(username):
    if username in users:
        return users.get(username)
    return None

@app.route('/')
@auth.login_required
def index():
    return "Hello, %s!" % auth.username()


@app.route('/globo', methods=['GET'])
@auth.login_required
def hello_world():
    response = crawler()
    return jsonify(response)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8000")
