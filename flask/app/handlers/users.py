def register_user(r, user_id, display_name, points, rank, country):
    """
    Stores the json fields of user data in a redis hash.
    Stores the country iso code of a user in a redis set
    Adds the user to the leaderboard using player:<guid>
    as the key and the points as the value.

            Parameters:
                    r (RedisClient): Redis Client
                    user_id (guid): guid
                    display_name (str): Display Name
                    points (float): Initial points
                    rank (int): Initial rank, will be overriden once added
                    to the leaderboard.
                    country (str): Country iso code

    """

    user = {
        'user_id': user_id,
        'display_name': display_name,
        'points': points or 0,
        'rank': rank,
        'country': country or "tr"
    }

    r.hmset("player:" + user['user_id'], user)
    r.set(user["country"], user['user_id'])
    r.zadd("leaderboard", {"player:" + user['user_id']: user[
        'points']})


def get_rank_of_user(r, guid):
    """
    Returns the rank of a specific user in O(log(N)), due to the use of a
    sorted set.

            Parameters:
                    r (RedisClient): Redis Client
                    user_id (guid): guid

            Returns:
                    rank (int): The rank of the given user
    """
    return r.zrevrank("leaderboard", "player:" + guid) + 1


def get_user_profile(r, guid):
    """
    Returns detailed information about a given user.

            Parameters:
                    r (RedisClient): Redis Client
                    guid (guid): guid

            Returns:
                    user (dict): The user object as a dict.
    """
    user = {
        #   Comment out user_id
        'user_id': guid,
        'display_name': r.hget("player:"+guid, "display_name"),
        'points': r.zscore("leaderboard", "player:" + guid),
        'rank': get_rank_of_user(r, guid),
        'country': r.hget("player:"+guid, "country")
    }

    return user
