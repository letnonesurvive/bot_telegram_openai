from typing import Any
from request_manager import request_manager

from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.enums.content_type import ContentType
from aiogram.types import Message, TextQuote, CallbackQuery
from aiogram import types
from aiogram.filters import Filter

from database import Database
import keyboards

import os

router = Router()
rm = request_manager("gpt-3.5-turbo")

database =  Database("users_database")

from main import bot

YOOTOKEN = str(os.environ.get("YOOTOKEN"))

class ButtonFilter(Filter):
    def __init__(self, my_text: str) -> None:
        self.my_text = my_text

    async def __call__(self, message: Message) -> bool:
        return message.text == self.my_text

@router.message(CommandStart())
async def command_start(message: Message):
    await message.answer("Добро пожаловать в ChatGPT бот", reply_markup=keyboards.mainKeyboard)
    if (not database.is_user_exists(message.from_user.id)):
        database.add_user(message.from_user.id)
    else:
        print("user exists in database")

@router.message(Command(commands=["clear"]))
async def command_clear(message: Message):
    rm.clear_chat()
    await message.answer("Диалог был очищен")
      
@router.message(ButtonFilter("Мой аккаунт 🤓"))
async def command_clear(message: Message):
    await message.answer("Ваш аккаунт не существует")   

@router.message(ButtonFilter("Выбрать модель 🕹"))
async def command_clear(message: Message):
    await message.reply("Выберите вариант модели", reply_markup=keyboards.settingsModelKeyboard)

@router.callback_query(F.data.in_(["text_models", "image_models"]))
async def pick_type_model(callback: CallbackQuery):
    await callback.answer(f"Вы выбрали {callback.data}")
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    if callback.data == "text_models":
        await callback.message.answer("Выберите модель для чата", reply_markup=keyboards.textModelKeyboard )

@router.callback_query(F.data.in_(["gpt-3.5-turbo", "gpt-4o", "gpt-4"]))
async def gpt_set_text_model(callback: CallbackQuery):
    await callback.answer(f"Вы выбрали {callback.data}", show_alert=True)
    rm.set_model(callback.data)
    
@router.callback_query(F.data.in_(["dall-e-3", "dall-e-2"]))
async def gpt_set_image_model(callback: CallbackQuery):
    await callback.answer(f"Вы выбрали {callback.data}", show_alert=True)
    rm.set_model(callback.data)    

@router.message(ButtonFilter("Подключить подписку 🤑"))
async def command_clear(message: Message):
    await message.reply("Выберите вариант подписки", reply_markup=keyboards.subscriptionKeyboard)   

@router.callback_query(F.data == "submonth_150")
async def submonth(callback: types.CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_invoice(chat_id=callback.from_user.id, 
                           title="Оформление подписки", 
                           description="Тестовое описание товара", 
                           payload="month_sub", 
                           provider_token=YOOTOKEN,
                           currency="RUB",
                           start_parameter="test_bot",
                           prices=[{"label": "Руб", "amount" : 15000}])
    
@router.callback_query(F.data == "submonth_300")
async def submonth(callback: types.CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_invoice(chat_id=callback.from_user.id, 
                           title="Оформление подписки", 
                           description="Тестовое описание товара", 
                           payload="month_sub", 
                           provider_token=YOOTOKEN,
                           currency="RUB",
                           start_parameter="test_bot",
                           prices=[{"label": "Руб", "amount" : 30000}])
    
@router.callback_query(F.data == "submonth_450")
async def submonth(callback: types.CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_invoice(chat_id=callback.from_user.id, 
                           title="Оформление подписки", 
                           description="Тестовое описание товара", 
                           payload="month_sub", 
                           provider_token=YOOTOKEN,
                           currency="RUB",
                           start_parameter="test_bot",
                           prices=[{"label": "Руб", "amount" : 45000}])    

@router.pre_checkout_query()
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@router.message(F.content_type == ContentType.SUCCESSFUL_PAYMENT)
async def process_pay(message: Message):
    if message.successful_payment.invoice_payload == "month_sub":
        await message.answer("Вам выдана подписка на месяц")        
   
@router.message()
async def send_message(message: Message):
    if message.content_type == ContentType.TEXT:
        await rm.send_request(message.text)
        anAnswer = rm.get_answer()
        await message.answer(anAnswer)
        print(anAnswer)
    else:
        await message.answer("Введите текстовый запрос")
            
# @router.callback_query(F.data == 'clear_dialog')
# async def process_callback_clear(callback_query: types.CallbackQuery):
#     await callback_query.message.answer("/clear")
#     await command_clear(callback_query.message)