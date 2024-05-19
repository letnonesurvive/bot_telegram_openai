import request_manager

from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

import keyboards

router = Router()
rm = request_manager.request_manager("gpt-3.5-turbo")


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Добро пожаловать в ChatGPT бот.\nНапишите свой запрос", reply_markup=keyboards.mainKeyboard)
   
@router.message()
async def cmd_start(message: Message):
    await rm.send_request(message.text)
    anAnswer = rm.get_answer()
    await message.answer(anAnswer)
    print(anAnswer)