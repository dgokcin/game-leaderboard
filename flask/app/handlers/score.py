def update_user_score(r, user_id, score_worth):
    r.zincrby("leaderboard", score_worth, "player:" + user_id)
    r.hincrbyfloat("player:" + user_id, "points", score_worth)

