from db_files.models import *


def submit_score_to_db(user_id, score_worth, timestamp):
    try:
        Score.create(user_id=user_id, score_worth=score_worth,
                     timestamp=timestamp)
        return True

    except OperationalError:
        return False
