from mongoengine import *
import datetime


class User(Document):
    user_id = UUIDField(primary_key=True)
    points = FloatField()
    rank = IntField()
    country = StringField()
    display_name = StringField(unique=True)


# class Score(Document):
#     user_id = UUIDField(primary_key=True)
#     score_worth = StringField()
#     timestamp = DateTimeField(default=datetime.datetime.utcnow)
#
#
# class Leaderboard(Document):
#     display_name = StringField()
#     rank = IntField()
#     points = FloatField()
