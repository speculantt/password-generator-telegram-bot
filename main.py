from config import tg_bot_token
import random
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message:types.Message):
    await message.reply('how many symbols the pass should be?')

@dp.message_handler()
async def get_password(message:types.Message):
    passlength = message.text
    try:
        passlength = int(passlength)
        if passlength < 14 and passlength > 1:
            a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            b = 'abcdefghijklmnopqrstuvwxyz'
            c = '0123456789'
            d = '!@#$%^&*()_+'
            all = a+b+c+d
            password = "".join(random.sample(all, passlength))
            await message.answer(f'your password: {password}')
        else:
            await message.reply('Pass length is incorrect')
            print(passlength)
    except Exception as ex2:
        print(ex2)
        await message.answer('input number from 1 to 14')

if __name__ == '__main__':
    executor.start_polling(dp)