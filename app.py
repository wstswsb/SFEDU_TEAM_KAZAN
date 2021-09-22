from flask import Flask
from blueprints import (
    users,
    checks
)
from structure import config


app = Flask(__name__)
app.register_blueprint(users, url_prefix="/users")
app.register_blueprint(checks, url_prefix="/checks")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6968)
