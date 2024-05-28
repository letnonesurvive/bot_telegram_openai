import asyncio
import os

from aiogram import Bot, Dispatcher
from handlers import router


BOT_API_KEY = str(os.environ.get("BOT_API_KEY"))
bot = Bot(BOT_API_KEY)
   
async def main():
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)  

if __name__ == '__main__':
    try: 
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")