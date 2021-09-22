import telebot
from telebot.types import (
    KeyboardButton,
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from structure import (
    TOKEN,
    service,
    user_pretty_message_builder
)
from loggers_factory import loggers_factory
logger = loggers_factory.get()


bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=["start", "help"])
def send_welcome(message: Message):
    bot.reply_to(message, "send_welcome_function")
    logger.debug(f"send_welcome to [[ {message.text} ]]")


@bot.message_handler(commands=["list_employees"])
def get_list_employees(message: Message):
    users = service.get_all_users()
    keyboard = InlineKeyboardMarkup()
    for u in users:
        keyboard.add(InlineKeyboardButton(
            text=u.fio,
            callback_data=(f"all_users | {u.id}")))
    bot.send_message(message.from_user.id,
                     text="Выберите сотрудника для уточнения информации",
                     reply_markup=keyboard)


if __name__ == "__main__":
    logger.debug("Start bot")
    bot.polling(none_stop=True, interval=0)
    logger.debug("Bot is working")
