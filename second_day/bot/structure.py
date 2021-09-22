from dotenv import dotenv_values
import telebot


config = dotenv_values(".env")

# === BOT === #
TOKEN = config["TELEGRAM_BOT_TOKEN"]

