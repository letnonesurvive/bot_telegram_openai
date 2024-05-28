from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import keyboard
from aiogram.types import menu_button_default


mainKeyboard = ReplyKeyboardMarkup(keyboard=[ [KeyboardButton(text="Мой аккаунт 🤓")], [KeyboardButton(text="Выбрать модель 🕹")], [KeyboardButton(text="Подключить подписку 🤑")]],
                                        resize_keyboard=True,
                                        input_field_placeholder="Сообщение")


settingsModelKeyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Текстовые модели", callback_data="text_models")],
                                                              [InlineKeyboardButton(text="Генерация картинок", callback_data="image_models")]])

textModelKeyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="GPT-3.5 Turbo", callback_data="gpt-3.5-turbo")],
                                                              [InlineKeyboardButton(text="GPT-4o", callback_data="gpt-4o")], 
                                                              [InlineKeyboardButton(text="GPT-4", callback_data="gpt-4")]])

imageModelKeyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="DALL·E 3", callback_data="dall-e-3")],
                                                              [InlineKeyboardButton(text="DALL·E 2", callback_data="dall-e-2")]])

subscriptionKeyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Месяц 150 рублей", callback_data="submonth_150")],
                                                             [InlineKeyboardButton(text="Месяц 300 рублей", callback_data="submonth_300")],
                                                             [InlineKeyboardButton(text="Месяц 450 рублей", callback_data="submonth_450")]])