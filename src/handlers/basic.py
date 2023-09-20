from aiogram import Dispatcher, Bot
from aiogram.types import Message, ContentType
from aiogram.filters import Command


async def start(message: Message, bot: Bot):
    await bot.send_message(message.chat.id, 'Hello!')


async def settings(message: Message, bot: Bot):
    await bot.send_message(message.chat.id, 'Settings')


async def support(message: Message, bot: Bot):
    await bot.send_message(message.chat.id, 'Support')


async def about(message: Message, bot: Bot):
    await bot.send_message(message.chat.id, 'About')


def register_handlers_basic(dp: Dispatcher):
    dp.message.register(start, Command(commands=['start', 'run']))
    dp.message.register(settings, Command(commands='settings'))
    dp.message.register(support, Command(commands='support'))
    dp.message.register(about, Command(commands='about'))
