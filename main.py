import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
import request_manager
import os

#import requests
#import secret

BOT_API_KEY = str(os.environ.get("BOT_API_KEY"))

bot = Bot(BOT_API_KEY)
dp = Dispatcher()
rm = request_manager.request_manager("gpt-3.5-turbo")

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет")
   
@dp.message()
async def cmd_start(message: Message):
    await rm.send_request(message.text)
    anAnswer = rm.get_answer()
    await message.answer(anAnswer)
    print(anAnswer)
   
async def main():
    await dp.start_polling(bot)  

if __name__ == '__main__':
    try: 
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")