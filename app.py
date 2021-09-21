from flask import Flask
from blueprints import users
from structure import config


app = Flask(__name__)
app.register_blueprint(users, url_prefix='/users')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6969)
