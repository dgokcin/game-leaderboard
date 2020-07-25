import uuid
import sys

from app import app
from app.models import Message, User

from flask import render_template, request, redirect, url_for, jsonify


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
#
#
# @app.route('/user/create', methods=['post'])
# def create_user():
#     user_id = request.form.get('user_id') or str(uuid.uuid4())
#     display_name = request.form.get('display_name')
#     points = request.form.get('points') or 0
#     rank = request.form.get('rank') or sys.maxsize
#     country = request.form.get('country') or 'tr'
#
#     try:
#         create_user_profile(user_id, display_name, points, rank, country)
#         resp = jsonify(success=true)
#     # todo: the default values & problematic entries could be handled better.
#     except integrityerror:
#         resp = jsonify(success=false)
#
#     return resp
#
#
# @app.route('/score/submit', methods=['POST'])
# def submit_score():
#     user_id = request.form.get('user_id')
#     score_worth = request.form.get('score_worth')
#     now = datetime.now()
#     current_date_parsed = datetime(now.year, now.month, now.day, now.hour,
#                                    0, 0)
#     timestamp = request.form.get('timestamp') or datetime.timestamp(
#         current_date_parsed)
#
#     try:
#         submit_score_to_db(user_id, score_worth, timestamp)
#         resp = jsonify(success=True)
#
#     except IntegrityError:
#         resp = jsonify(success=False)
#
#     return resp