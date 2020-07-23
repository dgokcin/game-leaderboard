from peewee import MySQLDatabase

from . import settings


db = MySQLDatabase(
    settings.DATABASE['NAME'], user=settings.DATABASE['USER'],
    password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'],
    port=int(settings.DATABASE['PORT'])
)
