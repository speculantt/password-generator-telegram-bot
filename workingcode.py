import random

from config import tg_bot_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('Привет! Напиши сколько символов должен быть пароль, максимум 74')

@dp.message_handler()
async def get_password(message: types.Message):
    passlength = message.text
    try:
        passlength = int(passlength)
        if passlength > 74 or passlength < 0:
            await message.reply('Недопустимый размер пароля')
        else:
            a = 'abcdefghijklmnopqrstuvwxyz'
            b = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            c = '0123456789'
            d = '[]{}()*/,-_!?'
            all = a + b + c + d
            password = ''.join(random.sample(all, passlength))
            await message.answer(f'Ваш пароль: {password}')
    except Exception as ex2:
        await message.answer('Необходимо ввести число от 1 до 74')
if __name__ == 'workingcode':
    executor.start_polling(dp)