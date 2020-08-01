def update_user_score(r, user_id, score_worth):
    """
    Increments the score of a given player by score_worth.
    Time complexity of incrementing the score: O(log(N)) where N is the
    number of elements in the sorted set. Time complexity of updating user
    profile: O(1).

            Parameters:
                    r (RedisClient): Redis Client
                    user_id (guid): guid
                    score_worth (float): Score to increment

    """
    r.zincrby("leaderboard", score_worth, "player:" + user_id)
    r.hincrbyfloat("player:" + user_id, "points", score_worth)
