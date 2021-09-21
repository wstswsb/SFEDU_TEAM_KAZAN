from mock import Mock
from repositories import UsersRepository
from loggers_factory import loggers_factory

logger = loggers_factory.get()


class TestUsersRepository:

    def test_get_by_telegram_id_none(self):
        collection = Mock()
        collection.find_one.return_value = None
        translator = Mock()
        telegram_id = "123"

        repository = UsersRepository(translator, collection)

        result = repository.get_by_telegram_id(telegram_id)
        assert result is None
        logger.debug(collection.find_one.call_args)
        collection.find_one.assert_called_once_with(
            {"telegram_id": telegram_id})
        translator.from_document.assert_not_called()

    def test_get_by_telegram_id_not_none(self):
        document = Mock()

        collection = Mock()
        collection.find_one.return_value = document

        model = Mock()
        translator = Mock()
        translator.from_document.return_value = model

        repository = UsersRepository(translator=translator,
                                     collection=collection)

        telegram_id = 123
        result = repository.get_by_telegram_id(telegram_id)

        assert result == model
        collection.find_one.assert_called_once_with(
            {"telegram_id": telegram_id})
        translator.from_document.assert_called_once_with(document)
