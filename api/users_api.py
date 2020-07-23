import uuid
import sys
from db_files.table_creator import *


def create_user(display_name, country):
    try:
        guid = uuid.uuid4()
        points = 0
        rank = sys.maxsize
        country = country
        display_name = display_name

        Users.create(user_id=guid, points=points, rank=rank,
                     country=country, display_name=display_name)
        return True

    except Users.DoesNotExist as e:
        print(e)
        return False






