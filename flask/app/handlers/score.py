def update_user_score(r, user_id, score_worth):
    r.zincrby("leaderboard", score_worth, "player:" + user_id)
    r.hincrby("player:" + user_id, "points", score_worth)
    pass

