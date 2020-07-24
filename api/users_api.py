import uuid
import sys

from db_files.table_creator import *


def create_user_profile(display_name, country):
    try:
        guid = uuid.uuid4()
        points = 0
        rank = sys.maxsize
        country = country
        display_name = display_name

        User.create(user_id=guid, points=points, rank=rank,
                    country=country, display_name=display_name)
        return True

    except OperationalError:
        return False


def get_user_profile(guid):
    try:
        user = User.select(User.user_id,
                           User.display_name,
                           User.points,
                           User.rank).where(User.user_id == guid).dicts().get()
        return user
    except User.DoesNotExist as e:
        print(e)
        return False

