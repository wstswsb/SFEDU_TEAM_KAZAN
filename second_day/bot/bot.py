import telebot
from telebot.types import Message
from structure import TOKEN
from loggers_factory import loggers_factory
logger = loggers_factory.get()


bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=["start", "help"])
def send_welcome(message: Message):
    bot.reply_to(message, "send_welcome_function")
    logger.debug(f"send_welcome to [[ {message.text} ]]")


@bot.message_handler(commands=["list_employees"])
def get_list_employees():
    pass


if __name__ == "__main__":
    logger.debug("Start bot")
    bot.polling(none_stop=True, interval=0)
    logger.debug("Bot is working")
