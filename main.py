#pip install aiogram
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import TOKEN

import random

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message_handler(Command('photo'))
async def photo(message: Message):
    list = ['https://img.freepik.com/free-photo/lovely-pet-portrait-isolated_23-2149192347.jpg', 'https://img.freepik.com/free-photo/adorable-kitty-with-monochrome-wall-her_23-2148955136.jpg', 'https://img.freepik.com/free-photo/adorable-white-black-kitty-with-monochrome-wall-her_23-2148955171.jpg']
    rand_photo = random.choice(list)
    await message.answer_photo(photo = rand_photo, caption = 'это супер крутая картинка')

@dp.message_handler(F.text == "Что такое ИИ?")
async def react_photo(message: Message):
    await message.answer('Искусственный интеллект — это свойство искусственных интеллектуальных систем выполнять творческие функции')

@dp.message_handler(F.photo)
async def aitext(message: Message):
    list = ['Ого какая фотка!', 'Непонятно что это такое', 'Не отправляй мне такое больше']
    rand_answ = random.choice(list)
    await message.answer(rand_answ)


@dp.message_handler(Command('help'))
async def help(message: Message):
    await message.answer('Этот бот умеет выполнять команды:\n /start \n /help')

@dp.message_handler(CommandStart())
async def start(message: Message):
    await message.answer("Приветики, я бот!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())




