from aiogram import Dispatcher, Bot
from aiogram.types import Message
from aiogram.filters import Command


async def start_admin(message: Message):
    pass


async def distribution_message(message: Message):
    pass


def register_handlers(dp: Dispatcher):
    dp.message.register(start_admin, Command(commands=['admin']))
    dp.message.register(distribution_message)
