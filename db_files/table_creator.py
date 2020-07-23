from peewee import *
from .db import db


class User(Model):
    user_id = CharField(unique=True)
    points = FloatField()
    rank = IntegerField()
    country = CharField()
    display_name = CharField

    class Meta:
        database = db
