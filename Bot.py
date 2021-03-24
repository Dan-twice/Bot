import logging
import sys
from aiogram import Bot, Dispatcher, executor, types
from flask import Flask
import os

app = Flask(__name__)
API_TOKEN = '1750326917:AAGYFKRGQAwYuT0M-vw0SIam9uIgww2vwWc'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    if message.text.lower() == 'bay':
        message.answer("Good bay, till next time!")
        sys.exit()
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
