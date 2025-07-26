
from aiogram import Bot, Dispatcher, executor, types
from handlers.commands import register_commands
import logging
import os

API_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

register_commands(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
