import unittest
from mongoengine.connection import disconnect
from mongoengine import *




class User(Document):
    user_id = UUIDField(primary_key=True)
    points = FloatField()
    rank = IntField()
    country = StringField()
    display_name = StringField(unique=True)


class TestPerson(unittest.TestCase):

    def setUp(self):
        connect('mongoenginetest', host='mongomock://localhost')

    def tearDown(self):
        disconnect('mongoenginetest')

    def test_create_user(self):
        User(user_id='1376a111fba449bb800b3f0bca64b3a3',
                    display_name='deniz',
                    points=1000,
                    rank=1,
                    country='tr').save()

        usr = User.objects().first()
        self.assertEqual(usr.display_name, 'deniz')


if __name__ == '__main__':
    unittest.main()
