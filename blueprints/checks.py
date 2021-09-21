import os
from flask import (
    Blueprint,
    request
)
from structure import (
    UPLOAD_FOLDER,
    check_sercvice,
    check_presenter
)
from exceptions import (
    BadRequest,
    NotFound
)
from loggers_factory import loggers_factory

# Checks work

logger = loggers_factory.get()

checks = Blueprint("checks", __name__)


@checks.route("/<telegram_owner_id>/<telegram_img_id>", methods=["POST"])
def upload_img(telegram_owner_id: str, telegram_img_id: str):
    fields = request.files | {
        "UPLOAD_FOLDER": UPLOAD_FOLDER,
        "telegram_owner_id": telegram_owner_id,
        "telegram_img_id": telegram_img_id}
    try:
        check = check_sercvice.upload(fields)
    except BadRequest as err:
        return '', err.code
    return check_presenter.to_json(check), 200
