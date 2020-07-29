import unittest
from mongoengine.connection import connect, disconnect
from mongoengine import UUIDField, FloatField, IntField, StringField, Document


class User(Document):
    user_id = UUIDField(primary_key=True)
    points = FloatField()
    rank = IntField()
    country = StringField()
    display_name = StringField(unique=True)


class TestPerson(unittest.TestCase):

    def setUp(self):
        self.connection = connect(db='test', host='mongomock://localhost')

    def tearDown(self):
        self.connection.drop_database("test")

    def test_create_user(self):
        User(user_id='1376a111fba449bb800b3f0bca64b3a3',
             display_name='deniz',
             points=1000,
             rank=1,
             country='tr').save()

        usr = User.objects().first()
        self.assertEqual(usr.display_name, 'deniz')

    def test_update_user_score(self):
        User(user_id='1376a111fba449bb800b3f0bca64b3a3',
             display_name='deniz',
             points=1000,
             rank=1,
             country='tr').save()


        User(user_id='1376a111fba449bb800b3f0bca64b3a4',
             display_name='user_2',
             points=900,
             rank=2,
             country='fr').save()

        User.objects(user_id='1376a111fba449bb800b3f0bca64b3a3').update_one(inc__points=15)

        usr = User.objects().first()
        self.assertEqual(usr.points, 1015)

    def test_update_user_rank(self):
        User(user_id='1376a111fba449bb800b3f0bca64b3a1',
             display_name='user_1',
             points=1000,
             rank=1,
             country='tr').save()

        User(user_id='1376a111fba449bb800b3f0bca64b3a2',
             display_name='user_2',
             points=900,
             rank=2,
             country='fr').save()

        User(user_id='1376a111fba449bb800b3f0bca64b3a3',
             display_name='user_3',
             points=800,
             rank=3,
             country='tr').save()

        User.objects(display_name='user_3').update_one(inc__points=201)
        threshold = User.objects(display_name='user_3').first().points
        new_rank = User.objects(points__lt=threshold).update(inc__rank=1)
        User.objects(display_name='user_3').update_one(inc__points=-new_rank)



if __name__ == '__main__':
    unittest.main()
