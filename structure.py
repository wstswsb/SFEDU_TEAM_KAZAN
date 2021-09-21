from pymongo import MongoClient
from dotenv import dotenv_values
from loggers_factory import loggers_factory
from translators import UsersTranslator
from repositories import UsersRepository
from services import UsersService
from presenters import UsersPresenter

logger = loggers_factory.get()

config = dotenv_values(".env")

# === Mongo === #
logger.info("Trying connect to mongo")
MONGO_HOST = config["MONGO_HOST"]
MONGO_PORT = config["MONGO_PORT"]
mongo_client = MongoClient(f"mongodb://{MONGO_HOST}:{MONGO_PORT}")
logger.info("Connection to mongo has been created")


# === Translators === #
users_translator = UsersTranslator()


# === Repositories === #
users_repository = UsersRepository(translator=users_translator,
                                   collection=mongo_client.KAZAN.users)

# === Presenters === #
users_presenter = UsersPresenter()

# === Services === #
users_service = UsersService(repository=users_repository)
