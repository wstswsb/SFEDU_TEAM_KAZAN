from flask import(
    Blueprint,
    request
)


user = Blueprint("user", __name__)


@user.route("/all", methods=["GET"])
def get_all():
    ...
