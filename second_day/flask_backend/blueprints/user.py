from exceptions import(
    NotFound,
    BadRequest
)
from flask import(
    Blueprint,
    request,
    jsonify
)
from structure import (
    user_presenter,
    user_service
)

user = Blueprint("user", __name__)


@user.route("/all", methods=["GET"])
def get_all():
    try:
        users = user_service.get_all()
    except NotFound as err:
        return '', err.code
    return jsonify([user_presenter.to_json(user) for user in users])
