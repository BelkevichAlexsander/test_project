import telebot
from telebot.types import Message
import requests

from config import config
from .keyboard import keyboard_start_message

bot_telegram = telebot.TeleBot(config.BOT_TOKEN.get_secret_value())


@bot_telegram.message_handler(commands=['start'])
def start(message: Message):
    bot_telegram.send_message(message.chat.id,
                              'Привет, а дай номер',
                              reply_markup=keyboard_start_message)


@bot_telegram.message_handler(content_types=['contact'])
def send_contact(message: Message):
    headers = {'Content-Type': 'application/json'}
    json = {'phone': message.contact.phone_number, 'login': message.from_user.username}
    url = 'https://s1-nova.ru/app/private_test_python/'

    # отправка логина и телефона на сервер
    requests.post(url=url, json=json, headers=headers)
    # ответ пользователю
    bot_telegram.send_message(chat_id=message.chat.id, text='Телефонный номер получен!')
