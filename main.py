from flask import Flask, jsonify
from api.users_api import *

app = Flask(__name__)

@app.before_first_request
def _db_connect_and_create_tables():
    db.connect()
    db.create_tables([Users])
    db.close()

@app.before_request
def _db_connect():
    db.connect()


@app.route("/", methods=['GET'])
def hello():
    return jsonify({'message': 'Hello world!'})


@app.route('/profile/<guid>')
def get_user(guid):
    return jsonify({'user_guid': guid})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
