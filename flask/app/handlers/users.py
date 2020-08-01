import uuid


def register_user(r, user_id, display_name, points, rank, country):
    user = {
        'user_id': user_id or str(uuid.uuid4()),
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
    return r.zrevrank("leaderboard", "player:" + guid) + 1


def get_user_profile(r, guid):
    user = {
        #   Comment out user_id
        'user_id': guid,
        'display_name': r.hget("player:"+guid, "display_name"),
        'points': r.zscore("leaderboard", "player:" + guid),
        'rank': get_rank_of_user(r, guid),
        'country': r.hget("player:"+guid, "country")
    }

    return user
