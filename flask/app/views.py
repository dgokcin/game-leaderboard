import uuid

from app import app
import sys
from app.models import Message, User

from flask import render_template, request, redirect, url_for, jsonify


@app.route("/")
def index():

    return jsonify(
        status=True,
        message='Welcome to the Dockerized Flask MongoDB app!'
    )



@app.route("/guestbook", methods=["GET", "POST"])
def guestbook():

    messages = Message.objects()

    if request.method == "POST":
        
        Message(
            name=request.form.get("name"),
            message=request.form.get("message")
        ).save()


    return render_template("guestbook.html", messages=messages)


@app.route("/test", methods=["GET", "POST"])
def user_stuff():
    users = User.objects()

    if request.method == "POST":
        User(
                user_id=request.form.get('user_id') or str(uuid.uuid4()),
                display_name=request.form.get('display_name'),
                points=request.form.get('points') or 0,
                rank=request.form.get('rank') or sys.maxsize,
                country=request.form.get('country') or 'tr'
        ).save()

        return jsonify(
            status=True,
            message='Successful Post'
        )

    return users.to_json()
# @app.route('/profile/<guid>', methods=['GET'])
# def get_user(guid):
#     user = get_user_profile(guid)
#     return jsonify(user)
#
#
# @app.route('/user/create', methods=['POST'])
# def create_user():
#     user_id = request.form.get('user_id') or str(uuid.uuid4())
#     display_name = request.form.get('display_name')
#     points = request.form.get('points') or 0
#     rank = request.form.get('rank') or sys.maxsize
#     country = request.form.get('country') or 'tr'
#
#     try:
#         create_user_profile(user_id, display_name, points, rank, country)
#         resp = jsonify(success=True)
#     # TODO: The default values & problematic entries could be handled better.
#     except IntegrityError:
#         resp = jsonify(success=False)
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