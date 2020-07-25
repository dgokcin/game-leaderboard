import sys
import uuid

from app import app
from app.models import User

from flask import request, jsonify


@app.route("/")
def index():

    return jsonify(
        status=True,
        message='Welcome to the Dockerized Flask MongoDB app!'
    )


@app.route("/user/create", methods=["POST"])
def create_user():
    User(
            user_id=request.form.get('user_id') or str(uuid.uuid4()),
            display_name=request.form.get('display_name'),
            points=request.form.get('points') or 0,
            rank=request.form.get('rank') or sys.maxsize,
            country=request.form.get('country') or 'tr'
    ).save()

    return jsonify(
        status=True,
        message='User Created'
    )


@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.objects()
    return users.to_json()


@app.route('/profile/<guid>', methods=['GET'])
def get_user_profile(guid):
    user = User.objects(user_id=guid)
    return user.to_json()


@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    leaderboard = User.objects.exclude('user_id').order_by('rank')
    return leaderboard.to_json()


@app.route('/leaderboard/<iso>', methods=['GET'])
def get_leaderboard_by_country(iso):
    leaderboard = User.objects(country=iso).exclude('user_id').order_by(
        'rank')
    return leaderboard.to_json()


@app.route('/score/submit', methods=['POST'])
def submit_score():
    user_id = request.form.get('user_id')
    score_worth = request.form.get('score_worth')
    timestamp = request.form.get('timestamp')

    User.objects(user_id=user_id).update_one(inc__points=score_worth)

    return jsonify(
        status=True,
        message='Score Submitted'
    )

