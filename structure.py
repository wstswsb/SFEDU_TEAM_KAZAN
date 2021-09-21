from pymongo import MongoClient
from dotenv import dotenv_values
from loggers_factory import loggers_factory
from translators import (
    UsersTranslator,
    CheckTranslator,
)
from repositories import (
    UsersRepository,
    CheckRepository
)
from services import (
    UsersService,
    CheckService,
)
from presenters import (
    UsersPresenter,
    CheckPresenter
)
from utils import (
    CheckChecker,
    ImgToText,
)


# === UTILS === #
check_checker = CheckChecker()
img_to_text = ImgToText()


logger = loggers_factory.get()

config = dotenv_values(".env")

# === Constatns === #
UPLOAD_FOLDER = config["FLASK_UPLOAD_FOLDER"]


# === Mongo === #
logger.info("Trying connect to mongo")
MONGO_HOST = config["MONGO_HOST"]
MONGO_PORT = config["MONGO_PORT"]
mongo_client = MongoClient(f"mongodb://{MONGO_HOST}:{MONGO_PORT}")
logger.info("Connection to mongo has been created")


# === Translators === #
users_translator = UsersTranslator()
check_translator = CheckTranslator()


# === Repositories === #
users_repository = UsersRepository(translator=users_translator,
                                   collection=mongo_client.KAZAN.users)
check_repository = CheckRepository(translator=check_translator,
                                   collection=mongo_client.KAZAN.checks)
# === Presenters === #
users_presenter = UsersPresenter()
check_presenter = CheckPresenter()

# === Services === #
check_sercvice = CheckService(repository=check_repository,
                              img_to_text=img_to_text,
                              check_checker=check_checker)
users_service = UsersService(
    repository=users_repository)
