from flask import (
    Blueprint,
    request
)
from structure import (
    users_presenter,
    users_service
)
from loggers_factory import loggers_factory
logger = loggers_factory.get()

users = Blueprint("users", __name__)


@users.route("/", methods=["POST"])
def create():
    user = users_service.create(request.json)
    return users_presenter.to_json(user), 200
