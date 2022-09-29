from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет! Напиши /pipiska что бы заработать 200 грн")

@dp.message_handler(commands=['pipiska'])
async def process_pipiska_command(message: types.Message):
    await message.reply("Привет, предлогаю тебе работу, плачу 200 грн за член. \nТы спросишь:Почему так много? Я тебе отвечу:Всё просто, один член стоит 100 грн, за два ты получить 200. \nНу как, ты готов? Если да, пиши - /gotovvkalivat")

@dp.message_handler(commands=['gotovvkalivat'])
async def process_gotovvkalivat_command(message: types.Message):
    await message.reply("Пасаси")

if __name__ == '__main__':
    executor.start_polling(dp)