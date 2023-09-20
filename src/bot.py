from aiogram import Bot, Dispatcher
import asyncio

from config import Config
from handlers import basic, specialist, admin
from utils.commands import set_commands


async def start():
    bot = Bot(token=Config.token, parse_mode="HTML")
    dp = Dispatcher(bot=bot)
    basic.register_handlers_basic(dp=dp)

    await set_commands(bot=bot)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.send_message(chat_id=Config.admin_id, text="<b>BOT STOPPED</b>")
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())
