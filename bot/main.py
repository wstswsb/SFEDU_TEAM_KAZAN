'''
    File name: ьфшт.py
    Author: Pavel Klimovskoy
    Date created: 21.09.2021
    Python Version: 3.9
'''

import telebot
import requests
import cv2
import pytesseract
from telebot.types import  Message
import telebot.types
from telebot import types

bot = telebot.TeleBot('1901231658:AAFMrvAHtYy0cz3eFsfxje9wqZlcoR8Y9Co')

# Логирование действия пользвателей
def logg(string, mode = 0):
    if mode == 0:
        print(string)

#  Событие на запуск бота
@bot.message_handler()
def start_command(message):
    bot.send_message(message.chat.id, "Начало работы")

    url = f'http://10.53.4.189:6969/users/{message.from_user.id}'
    res = requests.get(url)
    logg(res.status_code)

    if res.status_code == 200:
        bot.send_message(message.chat.id, "Ты уже есть в системе")
    elif res.status_code == 404:
        bot.send_message(message.chat.id, "Давай зарегестрируемся")
        bot.send_message(message.chat.id, "Напишите своё ФИО через пробел")
        bot.register_next_step_handler(message, get_full_name_and_send);
        get_full_name_and_send(message)

# Получение ФИО из сообщения и отправка на сервер
def get_full_name_and_send(message):
    fullname = message.text

    print(message.text)

    logg("sended")
    url = 'http://10.53.4.189:6969/users/'
    data = ({"fullname": fullname, "telegram_id": str(message.from_user.id)})
    res = requests.post(url, json=data)
    logg(res.status_code)

# Проверка на существование пользователя
def is_user_by_id(message):
    url = 'http://10.53.4.189:6969/users/'
    data = ({"telegram_id": str(message.from_user.id)})
    res = requests.post(url, json=data)

    logg(res.status_code)
    if res.status_code != 404:
        logg("new")
    else:
        logg("there is")

# Обработка команды создания нового пользователя
@bot.message_handler(commands=['newuser'])
def start_command(message):
    bot.send_message(message.chat.id, "Добавление нового пользователя")
    bot.send_message(message.chat.id, "Напишите своё ФИО через пробел")
    bot.register_next_step_handler(message, get_full_name_and_send);

# Вывод всех комманд бота
@bot.message_handler(commands=['help'])
def start_command(message):
    bot.send_message(message.chat.id, "Список команд")
    logg("help")

# Получение telegram id пользователя
@bot.message_handler(commands=['getid'])
def start_command(message):
    bot.send_message(message.chat.id, message.from_user.id)
    logg("getid")

# Обработчик на приём фотографии
@bot.message_handler(content_types=["document", "photo"])
def photo(message):
    idphoto = message.photo[0].file_id
    bot.send_message(message.chat.id, "Получил фото")
    bot.send_photo(message.chat.id, idphoto )

    file_on_disk = ""

    try:
       file_info = bot.get_file(message.photo[-1].file_id)
       downloaded_file = bot.download_file(file_info.file_path)

       src = 'C:/pic/' + message.photo[-1].file_id + ".jpg"
       file_on_disk = src
       with open(src, 'wb') as new_file:
           new_file.write(downloaded_file)

       bot.reply_to(message, "Пожалуй, я сохраню это")
    except Exception as e:
       bot.reply_to(message, e)

    # Обработка фото
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    img = cv2.imread(file_on_disk)

    text = pytesseract.image_to_string(img, lang="rus")
    # bot.send_message(message.chat.id, text)
    print(text)
    print(type(text))
    # Обработка фото

    flag = False
    text = text.upper()
    keywords2 = ["ИНН", "СУММА", "ИТОГО", "УСЛУГА", "ДАТА"]
    for word2 in keywords2:
        if word2 in text:
            flag = True
            break

    if flag == True:
        bot.send_message(message.chat.id, "Вот текст с фото:")
        bot.send_message(message.chat.id, text)
    else:
        mes = "Неудалось распознать или это не чек"
        bot.send_message(message.chat.id, mes)
        mes = "Ввести чек вручную?"

        keyboard = types.InlineKeyboardMarkup()  # клавиатура
        key_again = types.InlineKeyboardButton(text='Ввести вручную', callback_data='again')  # кнопка «Да»
        keyboard.add(key_again)  # добавляем кнопку в клавиатуру
        bot.send_message(message.from_user.id, text=mes, reply_markup=keyboard)


_date, _time, _sum = "", "", ""
def get_date(message):
    global _date
    _date = message.text
    bot.register_next_step_handler(message, get_time)

def get_time(message):
    global _time
    _time = message.text

    msg = "Введите время с чека"
    bot.send_message(message.chat.id, msg)
    bot.register_next_step_handler(message, get_sum)


def get_sum(message):
    global _sum
    _sum = message.text

    msg = "Введите сумму с чека"
    bot.send_message(message.chat.id, msg)
    bot.register_next_step_handler(message, show_date)

def show_date():
    global _sum, _time, _date
    print(_date)
    print(_time)
    print(_date)

def hand_fill_in(message):

    msg = "Введите дату с чека"
    bot.send_message(message.chat.id, msg)
    bot.register_next_step_handler(message, get_date)

# Хэндлер для кнопок
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # Если сообщение из чата с ботом

    if call.data == "again":
        hand_fill_in(call.message)

bot.polling(none_stop=True, interval=0)
