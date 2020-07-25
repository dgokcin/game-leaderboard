from flask import Flask
import redis
from mongoengine import connect

import os

app = Flask(__name__)

r = redis.Redis(
    host='redis',
    port=6379,
    db=0,
    password="root"
)

connect(
    db="flask-db",
    host="mongo",
    port=27017,
    username="root",
    password="root",
    authentication_source="admin",
    connect=False
)


from app import views
from app import models
