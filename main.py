import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
import request_manager

import requests

import secret

bot = Bot(secret.telegram_bot_token)
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

    # proxies = {
    # 'http': 'http://172.64.89.152:80',
    # }

    # url = 'https://api.openai.com/v1/chat/completions'
    # response = requests.get(url, proxies=proxies)
    # print(response)
    try: 
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")