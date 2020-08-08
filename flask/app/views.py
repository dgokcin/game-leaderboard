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
    json_data = request.get_json(silent=True, force=True)

    for u in json_data:
        user_id = u["user_id"] or str(uuid.uuid4())
        display_name = u["display_name"]
        points = u["points"] or 0
        rank = u["rank"] or sys.maxsize
        country = u["country"] or 'tr'

        users.register_user(r, user_id, display_name, float(points),
                            int(rank), country)

    return jsonify(
        status=True,
        message='User(s) are created'
    )


@app.route('/profile/<guid>', methods=['GET'])
def get_user_profile(guid):
    user = users.get_user_profile(r, guid)
    return jsonify(user)


@app.route('/leaderboard/all', methods=['GET'])
def get_all_leaderboard():
    lb = leaderboard.generate_all_leaderboard(r)
    return jsonify(lb)

@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    lb = leaderboard.generate_leaderboard(r)
    return jsonify(lb)


@app.route('/leaderboard/<iso>', methods=['GET'])
def get_leaderboard_by_country(iso):
    lb = leaderboard.generate_leaderboard_by_country(r, iso)
    return jsonify(lb)


@app.route('/score/submit', methods=['POST'])
def submit_score():
    json_data = request.get_json(silent=True, force=True)

    user_id = json_data["user_id"] or str(uuid.uuid4())
    score_worth = json_data["score_worth"]

    # TODO maybe use this field as well
    timestamp = json_data["timestamp"] or 0,

    score.update_user_score(r, user_id, score_worth)

    return jsonify(
        status=True,
        message='Score Submitted'
    )
