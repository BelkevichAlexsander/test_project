from telebot.types import ReplyKeyboardMarkup, KeyboardButton

keyboard_start_message = ReplyKeyboardMarkup(True)
keyboard_start_message.add(
        KeyboardButton('Отправить номер телефона', request_contact=True)
    )
