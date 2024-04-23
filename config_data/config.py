from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту


# Создаем экземпляр класса Config и наполняем его данными из переменных окружения
@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:
    env = Env()# Создаем экземпляр класса Env
    env.read_env(path) # Добавляем в переменные окружения данные, прочитанные из файла .env
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')))# возвращаем экземпляр класса Config и наполняем его данными из
    # переменных окружения