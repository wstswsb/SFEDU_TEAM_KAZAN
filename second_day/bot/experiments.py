from telebot import TeleBot
from structure import bot


class Helloer:

    @bot.message_handler(commands=["start"])
    def send_welcome(message):
        bot.reply_to(message, "send_welcome")
