import unittest
from api.users_api import *


class TestUserMethods(unittest.TestCase):

    def test_create_user_profile(self):
        with db.atomic() as transaction:
            display_name = "temp_user"
            country = "tr"

            success = create_user_profile(display_name, country)
            transaction.rollback()

        self.assertEqual(success, True)

    def test_get_user_profile(self):
        guid = "5b69053b-8a51-42c1-b6cf-4473c4c0bede"
        user = get_user_profile(guid)
        expected = {'user_id': '5b69053b-8a51-42c1-b6cf-4473c4c0bede',
                    'display_name': 'temp_user',
                    'points': 0.0, 'rank': 2147483647}

        self.assertEqual(user, expected)


if __name__ == '__main__':
    unittest.main()
