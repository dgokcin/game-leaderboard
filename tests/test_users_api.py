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
        with test_db.atomic() as transaction:
            display_name = "temp_user"
            country = "tr"

            success = create_user_profile(display_name, country)

        self.assertEqual(success, True)

    # def test_get_valid_user_profile(self):
    #     guid = "5b69053b-8a51-42c1-b6cf-4473c4c0bede"
    #     user = get_user_profile(guid)
    #     expected = {'user_id': '5b69053b-8a51-42c1-b6cf-4473c4c0bede',
    #                 'display_name': 'temp_user',
    #                 'points': 0.0, 'rank': 2147483647}
    #
    #     self.assertEqual(user, expected)

    def test_get_invalid_user_profile(self):
        guid = "invalid_guid"
        self.assertIsNone(get_user_profile(guid))


if __name__ == '__main__':
    unittest.main()
