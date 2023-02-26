import requests as requests
from django.http import HttpResponse
from telebot.types import Update

from config import config
from .bot.bot import bot_telegram

# константы
URL_NGROK = config.URL_NGROK.get_secret_value()
BOT_TOKEN = config.BOT_TOKEN.get_secret_value()
TELEGRAM_API_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/'


def telegram_bot_hook(request):
    if request.method == 'POST':
        update = Update.de_json(request.body.decode('utf-8'))
        bot_telegram.process_new_updates([update])
        return HttpResponse('Correct data')
    else:
        return HttpResponse('Bad Request')


def set_webhook(request):
    response = requests.post(TELEGRAM_API_URL + "setWebhook?url=" + URL_NGROK).json()
    return HttpResponse(f"{response}")
