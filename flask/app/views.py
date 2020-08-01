import sys
import uuid
import json
from flask import request, jsonify

from app import app, r
from app.handlers import users
from app.handlers import score
from app.handlers import leaderboard as leaderboard


@app.route("/")
def index():

    return jsonify(
        status=True,
        message='Welcome to the Dockerized Flask redis app!'
    )


@app.route("/user/create", methods=["POST"])
def create_user():
    # headers = request.headers
    # print(headers)
    user_id = str(request.headers.get('user-id')) or str(uuid.uuid4())
    display_name = str(request.headers.get('display-name'))
    points = float(request.headers.get('points')) or 0,
    rank = int(request.headers.get('rank')) or sys.maxsize,
    country = str(request.headers.get('country')) or 'tr'

    users.register_user(r, user_id, display_name, float(points[0]),
                        int(rank[0]), country)

    return jsonify(
        status=True,
        message='User Created with id:' + user_id
    )


@app.route('/profile/<guid>', methods=['GET'])
def get_user_profile(guid):
    user = users.get_user_profile(r, guid)
    return json.dumps(user)


@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    lb = leaderboard.generate_leaderboard(r)
    return json.dumps(lb)


@app.route('/leaderboard/<iso>', methods=['GET'])
def get_leaderboard_by_country(iso):
    lb = leaderboard.generate_leaderboard_by_country(r, iso)
    return json.dumps(lb)


@app.route('/score/submit', methods=['POST'])
def submit_score():
    user_id = str(request.headers['user-id'])
    score_worth = float(request.headers.get('score-worth'))
    # TODO maybe use this field as well
    timestamp = request.headers.get('timestamp')

    score.update_user_score(r, user_id, score_worth)

    return jsonify(
        status=True,
        message='Score Submitted'
    )
