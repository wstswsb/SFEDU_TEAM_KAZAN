from pymongo import MongoClient
from dotenv import dotenv_values

from presenters import (
    UserPresenter,
    CheckPresenter
)
from translators import (
    UserTranslator,
    CheckTranslator,
)

from repositories import (
    UserRepository,
    MongoRepository,
    CheckRepository
)

config = dotenv_values('.env')

# === Mongo === #
MONGO_HOST = config["MONGO_HOST"]
MONGO_PORT = config["MONGO_PORT"]
mongo_client = MongoClient(f"mongodb://{MONGO_HOST}:{MONGO_PORT}")

# == Presenters == #
user_presenter = UserPresenter()
check_presenter = CheckPresenter()


# == Translators == #
user_translator = UserTranslator()
check_translator = CheckTranslator()

# == Repositories == #
user_repository = UserRepository(
    translator=user_translator,
    collection=mongo_client.KAZAN.s_users
)

check_repository = CheckRepository(
    translator=check_translator,
    collection=mongo_client.KAZAN.s_checks
)
