import sys

from peewee import *
from .db import db


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    user_id = UUIDField(primary_key=True, unique=True)
    points = FloatField(default=0)
    rank = IntegerField()
    country = CharField()
    display_name = CharField(unique=True)


class Score(BaseModel):
    user_id = ForeignKeyField(User, backref='score', unique=True)
    score_worth = FloatField()
    timestamp = CharField()
