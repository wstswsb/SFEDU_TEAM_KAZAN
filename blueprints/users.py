import os

from flask import (
    Blueprint,
    request
)
from werkzeug.utils import redirect, secure_filename
from structure import (
    UPLOAD_FOLDER,
    users_presenter,
    users_service,
)
from loggers_factory import loggers_factory
from exceptions import (
    BadRequest,
    NotFound,
    Conflict
)


logger = loggers_factory.get()

users = Blueprint("users", __name__)


@users.route("/", methods=["POST"])
def create():
    logger.debug(str(request))
    try:
        user = users_service.create(request.json)
    except Conflict as err:
        return '', err.code
    return users_presenter.to_json(user), 200


@users.route("/<telegram_id>", methods=["GET"])
def get(telegram_id: str):
    logger.debug(str(request))
    try:
        user = users_service.get_by_telegram_id(
            {"telegram_id": telegram_id})
    except NotFound as err:
        return '', err.code
    return users_presenter.to_json(user), 200


# Checks work

@users.route("/<telegram_id>/<img_id>", methods=["POST"])
def upload_img(telegram_id: str, img_id: str):
    fields = request.files | {
        "UPLOAD_FOLDER": UPLOAD_FOLDER,
        "telegram_id": telegram_id}
    try:
        pass
    except:
        pass
    return '', 201
