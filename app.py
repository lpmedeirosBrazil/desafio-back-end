__author__ = 'galleani'

from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth
from crawler import get_auto_esporte

app = Flask(__name__)
auth = HTTPBasicAuth()

users = dict(galleani='123', rafael='123', teste='teste')


@auth.get_password
def get_password(username):
    if username in users:
        return users.get(username)
    return None


@app.route('/api/v1/crawler/autoesporte', methods=['GET'])
@auth.login_required
def crawler_auto_esporte():
    response = get_auto_esporte()
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
