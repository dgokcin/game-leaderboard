from flask import Flask
import redis

app = Flask(__name__)

r = redis.StrictRedis(
    host='redis',
    port=6379,
    db=0,
    password="root",
    decode_responses=True
)

# connect(
#     db="flask-db",
#     host="mongo",
#     port=27017,
#     username="root",
#     password="root",
#     authentication_source="admin",
#     connect=False
# )


from app import views
