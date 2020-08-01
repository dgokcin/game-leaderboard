from app.handlers import users


def generate_leaderboard_by_country(r, iso):
    lb = r.zrevrange("leaderboard", 0, -1, withscores=True)
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


def generate_leaderboard(r):
    lb = r.zrevrange("leaderboard", 0, -1, withscores=True)
    leaderboard_data = []
    for p in lb:
        print(p)
        print(p[0])
        player = r.hgetall(p[0])
        print(player)
        d = {
            'rank': users.get_rank_of_user(r, player['user_id']),

            'points': r.zscore("leaderboard",
                                    "player:" + player['user_id']),
            'display_name': player['display_name'],
            'country': player['country']
        }

        leaderboard_data.append(d)
    return leaderboard_data
