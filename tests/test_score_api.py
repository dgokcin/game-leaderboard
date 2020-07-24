import unittest

from datetime import datetime
from api.score_api import *


MODELS = [Score]
# use an in-memory SQLite for tests.
test_db = SqliteDatabase(':memory:')


class TestUserMethods(unittest.TestCase):
    def setUp(self):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        test_db.drop_tables(MODELS)

        # Close connection to db.
        test_db.close()

    def test_submit_valid_score(self):
        user_id = 0
        score_worth = 100
        now = datetime.now()
        timestamp = datetime.timestamp(now)

        success = submit_score_to_db(user_id=user_id, score_worth=score_worth,
                                     timestamp=timestamp)

        self.assertEqual(success, True)


if __name__ == '__main__':
    unittest.main()
