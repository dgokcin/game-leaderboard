import uuid
import sys
from flask import Flask, jsonify, request, redirect, url_for
from api.users_api import *

app = Flask(__name__)


@app.before_first_request
def _db_connect_and_create_tables():
    db.connect()
    db.create_tables([User, Score])
    db.close()


@app.before_request
def _db_connect():
    db.connect()


@app.route("/", methods=['GET'])
def hello():
    return jsonify({'message': 'Hello world!'})


@app.route('/profile/<guid>', methods=['GET'])
def get_user(guid):
    user = get_user_profile(guid)
    return jsonify(user)


@app.route('/user/create', methods=['POST'])
def create_user():
    user_id = request.form.get('user_id') or str(uuid.uuid4())
    display_name = request.form.get('display_name')
    points = request.form.get('points') or 0
    rank = request.form.get('rank') or sys.maxsize
    country = request.form.get('country') or 'tr'

    try:
        create_user_profile(user_id, display_name, points, rank, country)
        resp = jsonify(success=True)
    # TODO: Improve how you handle the exception, it is too generic
    # TODO: Handle default values & problematic entries
    except Exception:
        resp = jsonify(success=False)

    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
