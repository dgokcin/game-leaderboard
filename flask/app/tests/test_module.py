import unittest
import uuid
import redis
import fakeredis

from app.handlers import users
from app.handlers import leaderboard
from app.handlers import score


class TestUserIntegrations(unittest.TestCase):

    def setUp(self):
        self.r = fakeredis.FakeStrictRedis(decode_responses=True)

    def tearDown(self):
        self.r.flushall()

    def test_create_user(self):
        users.register_user(self.r,
                            user_id=str(uuid.uuid4()),
                            display_name='deniz',
                            points=10,
                            rank=1,
                            country='tr')

        self.assertEqual(1, self.r.zcard("leaderboard"))

    def test_get_user_profile(self):
        guid = "1"
        users.register_user(self.r,
                            user_id=guid,
                            display_name='deniz',
                            points=10,
                            rank=1,
                            country='tr')

        expected = {
            'user_id': guid,
            'display_name': "deniz",
            'points': 10,
            'rank': 1,
            'country': "tr"
        }

        self.assertEqual(expected, users.get_user_profile(self.r, guid))

    def test_update_user_score(self):
        guid = "1"
        users.register_user(self.r,
                            user_id=guid,
                            display_name='deniz',
                            points=10,
                            rank=1,
                            country='tr')

        score.update_user_score(self.r, guid, 15)

        pass
        self.assertEqual("25", self.r.hget("player:" + guid, "points"))

    def test_get_leaderboard(self):
        users.register_user(self.r,
                            user_id="1",
                            display_name='deniz',
                            points=10,
                            rank=1,
                            country='tr')

        users.register_user(self.r,
                            user_id="2",
                            display_name='test',
                            points=6,
                            rank=2,
                            country='fr')

        # Increment Score
        self.r.zincrby("leaderboard", 10000, "player:2")

        expected = [
            {
                "rank": 1,
                "points": 10006.0,
                "display_name": "test",
                "country": "fr"
            },
            {
                "rank": 2,
                "points": 10.0,
                "display_name": "deniz",
                "country": "tr"
            }
        ]
        self.assertEqual(expected, leaderboard.generate_leaderboard(self.r))

    def test_get_leaderboard_by_country(self):
        users.register_user(self.r,
                            user_id="1",
                            display_name='deniz',
                            points=10,
                            rank=1,
                            country='tr')

        users.register_user(self.r,
                            user_id="2",
                            display_name='test',
                            points=6,
                            rank=2,
                            country='fr')

        # Increment Score
        self.r.zincrby("leaderboard", 10000, "player:2")

        expected = [
            {
                "rank": 2,
                "points": 10.0,
                "display_name": "deniz",
                "country": "tr"
            }
        ]
        self.assertEqual(expected,
                         leaderboard.generate_leaderboard_by_country(self.r,
                                                                     "tr"))


if __name__ == '__main__':
    unittest.main()
