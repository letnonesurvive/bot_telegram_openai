from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

mainKeyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Очистить диалог")],
                                             [KeyboardButton(text="Кнопка 1")],
                                             [KeyboardButton(text="Кнопка 2"), KeyboardButton(text="Кнопка 3")]],
                                        resize_keyboard=True,
                                        input_field_placeholder="Сообщение")
