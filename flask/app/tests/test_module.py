import unittest
from app import app
from mockupdb import MockupDB, go, Command
from pymongo import MongoClient
from json import dumps


class MyTestCase(unittest.TestCase):
    def test_something(self):
        pass


if __name__ == '__main__':
    unittest.main()
