from dotenv import dotenv_values
from models import (
    User,
    Check
)
from requesters import (
    UsersRequester
)
from parsers import (
    GetAllUsersParser
)
from services import (
    Service
)
from pretty_message_builders import (
    UserPrettyMessageBuilder
)
config = dotenv_values(".env")

# === BOT === #
TOKEN = config["TELEGRAM_BOT_TOKEN"]

# == Requesters == #
users_requester = UsersRequester(config.get("BASE_HOST"))

# == Parsers == #
get_all_users_parser = GetAllUsersParser()

# == Services == #
service = Service(
    requester=users_requester,
    parser=get_all_users_parser
)

# == PrettyMessageBuilders == #
user_pretty_message_builder = UserPrettyMessageBuilder()
