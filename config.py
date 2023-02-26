from pydantic import BaseSettings, SecretStr
from dotenv import load_dotenv
import os


class Settings(BaseSettings):
    BOT_TOKEN: SecretStr
    URL_NGROK: SecretStr
    DJANGO_SECRET_KEY: SecretStr

    class Config:
        dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
        if os.path.exists(dotenv_path):
            load_dotenv(dotenv_path)


# Валидация объекта конфига
config = Settings()
