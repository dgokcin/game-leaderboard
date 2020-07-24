import unittest
from api.users_api import *

MODELS = [User]
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

    def test_create_user_profile(self):
        user_id = 0
        display_name = "temp_user"
        points = 5000
        rank = 1
        country = 'tr'

        success = create_user_profile(user_id=user_id,
                                      display_name=display_name,
                                      points=points, rank=rank,
                                      country=country)

        self.assertEqual(success, True)

    def test_get_invalid_user_profile(self):
        guid = "invalid_guid"
        self.assertIsNone(get_user_profile(guid))


if __name__ == '__main__':
    unittest.main()
