from app.handlers import users


def generate_all_leaderboard(r):
    """
    Generates the global leaderboard for all the players. Due to the use of
    sorted sets, as the data structure for the leaderboard, the time
    complexity of obtaining the leaderboard takes O(log(N)+M)  with N being
    the number of elements in the sorted set and M the number of elements
    returned.

            Parameters:
                    r (RedisClient): Redis Client

            Returns:
                    leaderboard (list): The leaderboard as a list of dicts
    """
    lb = r.zrevrange("leaderboard", 0, -1, withscores=True)
    leaderboard_data = []
    for p in lb:
        player = r.hgetall(p[0])
        d = {
            'rank': users.get_rank_of_user(r, player['user_id']),

            'points': r.zscore("leaderboard",
                               "player:" + player['user_id']),
            'display_name': player['display_name'],
            'country': player['country']
        }

        leaderboard_data.append(d)
    return leaderboard_data


def generate_leaderboard(r):
    """
    Generates the top 10 players in the global leaderboard. Due to the use
    sorted sets, as the data structure for the leaderboard, the time
    complexity of obtaining the leaderboard takes O(log(N)+M)  with N being
    the number of elements in the sorted set and M the number of elements
    returned.

            Parameters:
                    r (RedisClient): Redis Client

            Returns:
                    leaderboard (list): The leaderboard as a list of dicts
    """
    lb = r.zrevrange("leaderboard", 0, 9, withscores=True)
    leaderboard_data = []
    for p in lb:
        player = r.hgetall(p[0])
        d = {
            'rank': users.get_rank_of_user(r, player['user_id']),

            'points': r.zscore("leaderboard",
                               "player:" + player['user_id']),
            'display_name': player['display_name'],
            'country': player['country']
        }

        leaderboard_data.append(d)
    return leaderboard_data


def generate_leaderboard_by_country(r, iso):
    """
    Generates the leaderboard and filters it by iso code.

            Parameters:
                    r (RedisClient): Redis Client
                    iso (str): Cointry iso code

            Returns:
                    leaderboard (list): The leaderboard as a list of dicts
    """
    lb = r.zrevrange("leaderboard", 0, 9, withscores=True)
    leaderboard_data = []
    for p in lb:
        player = r.hgetall(p[0])
        if player['country'] == iso:
            d = {
                'rank': users.get_rank_of_user(r, player['user_id']),

                'points': r.zscore("leaderboard",
                                   "player:" + player['user_id']),
                'display_name': player['display_name'],
                'country': player['country']
            }

            leaderboard_data.append(d)
    return leaderboard_data


