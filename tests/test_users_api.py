from api.users_api import *


def test_create_user():
    with db.atomic() as transaction:
        display_name = "temp_user"
        country = "tr"

        success = create_user(display_name, country)
        # transaction.rollback()

    assert success is True

