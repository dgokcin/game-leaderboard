from peewee import *
from .db import db


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    user_id = CharField(unique=True)
    points = FloatField()
    rank = IntegerField()
    country = CharField()
    display_name = CharField()


class Score(BaseModel):
    user_id = ForeignKeyField(User, backref='score')
    score_worth = FloatField()
    timestamp = DateTimeField()
