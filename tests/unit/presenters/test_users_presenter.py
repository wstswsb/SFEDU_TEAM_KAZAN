from presenters import UsersPresenter
from models import User


class TestUsersPresenter:

    def test_to_json(self):
        model = User()
        model.fullname = "fullname"
        model.telegram_id = "telegram_id"
        model.mongo_id = "mongo_id"

        presenter = UsersPresenter()

        result = presenter.to_json(model)

        assert isinstance(result, dict)
        assert model.fullname == result.get("fullname")
        assert model.telegram_id == result.get("telegram_id")
        assert model.mongo_id == result.get("mongo_id")
