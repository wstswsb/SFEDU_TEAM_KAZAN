from re import T
from flask import Flask
from blueprints import users

app = Flask(__name__)

app.register_blueprint(users, url_prefix='/users')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=6969)
