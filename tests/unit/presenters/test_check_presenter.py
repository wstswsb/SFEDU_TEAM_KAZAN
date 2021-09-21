from models import Check
from presenters import CheckPresenter


class TestCheckPresenter:

    def test_to_json(self):
        model = Check()
        model.telegram_owner_id = "telegram_owner_id"
        model.telegram_img_id = "telegram_img_id"
        model.text = "text"
        model.balance = 123
        model.INN = "INN"

        presenter = CheckPresenter()

        result = presenter.to_json(model)

        assert isinstance(result, dict)
        assert model.telegram_owner_id == result.get("telegram_owner_id")
        assert model.telegram_img_id == result.get("telegram_img_id")
        assert model.text == result.get("text")
        assert model.balance == result.get("info").get("balance")
        assert model.INN == result.get("info").get("INN")
