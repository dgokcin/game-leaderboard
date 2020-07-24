import uuid
import sys

from db_files.models import *


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
    """
    This method gets the profile of a specific user with a select query to
    the User table

    Parameters
    ----------
    guid : string

    Returns
    -------
    user : User

    Returns the user object if the query is successful. A DoesNotExist
    exception is thrown if the user with the specified user does not exist.
    """
    try:
        user = User.select(User.user_id,
                           User.display_name,
                           User.points,
                           User.rank).where(User.user_id == guid).dicts().get()
        return user

    except User.DoesNotExist:
        return None
