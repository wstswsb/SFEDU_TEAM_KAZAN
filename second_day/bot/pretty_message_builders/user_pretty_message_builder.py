from models import User


class UserPrettyMessageBuilder:
    def to_msg(self, model: User) -> str:
        pretty_message = f"ФИО: {model.fio}\n"
        return pretty_message
