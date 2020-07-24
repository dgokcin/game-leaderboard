from db_files.models import *


# TODO add docstring comments
def create_user_profile(user_id, display_name, points, rank, country):
    """
    This method posts to the User database.

    Parameters
    ----------
    :param user_id:
    :param display_name:
    :param points:
    :param rank:
    :param country:

    Returns
    -------
    success : bool

    """
    try:
        User.create(user_id=user_id, points=points, rank=rank,
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
