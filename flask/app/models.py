from mongoengine import *
import datetime


class User(Document):
    user_id = UUIDField(primary_key=True)
    points = FloatField()
    rank = IntField()
    country = StringField()
    display_name = StringField(unique=True)
