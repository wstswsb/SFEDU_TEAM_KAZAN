from flask import (
    Blueprint,
    request,
    jsonify
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


@checks.route("/history/<telegram_owner_id>", methods=["GET"])
def history(telegram_owner_id: str):
    checks = check_sercvice.history({
        "telegram_owner_id": telegram_owner_id})
    checks = [check_presenter.to_json(check) for check in checks]
    return jsonify(checks), 200


@checks.route("/<telegram_img_id>", methods=["GET"])
def get_by_telegram_img_id(telegram_img_id: str):
    try:
        checks = check_sercvice.get_by_telegram_img_id({
            "telegram_img_id": telegram_img_id
        })
    except NotFound as err:
        return '', err.code
    return check_presenter.to_json(checks), 200


@checks.route("/<telegram_img_id>", methods=["PATCH"])
def patch_date_time_intbalance(telegram_img_id: str):
    try:
        check = check_sercvice.patch_date_time_intbalance(
            request.json | {"telegram_img_id": telegram_img_id})
    except NotFound as err:
        return '', err.code
    except BadRequest as err:
        return '', err.code
    return check_presenter.to_json(check), 200
