import os
from aiogram import Bot, Dispatcher
import asyncio
import sys
import handlers
import logging
from dotenv import load_dotenv
load_dotenv()


async def main():
    bot = Bot(os.getenv('BOT_TOKEN'), parse_mode="HTML")
    try:
        dp = Dispatcher()
        dp.include_router(handlers.router)
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()  # Закрываем соединение


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
