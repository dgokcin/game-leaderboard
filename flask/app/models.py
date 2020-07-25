from mongoengine import *
import datetime


class Message(Document):
    name = StringField()
    message = StringField()
    date = DateTimeField(default=datetime.datetime.utcnow)

    meta = {
        "ordering": [
            "-date"
        ]
    }


class User(Document):
    user_id = UUIDField()
    points = FloatField()
    rank = IntField()
    country = StringField()
    display_name = StringField()


class Score(Document):
    user_id = UUIDField()
    score_worth = StringField()
    timestamp = DateTimeField(default=datetime.datetime.utcnow)

