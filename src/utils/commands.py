from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

from src.emoji import Emoji


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description=f'{Emoji.CHECKERED_FLAG} Старт'
        ),
        BotCommand(
            command='settings',
            description=f'{Emoji.GEAR} Настройка'
        ),
        BotCommand(
            command='support',
            description=f'{Emoji.WRITING_HAND} Помощь'
        ),
        BotCommand(
            command='about',
            description=f'{Emoji.QUESTION} Про бота'
        ),
    ]

    await bot.set_my_commands(commands=commands, scope=BotCommandScopeDefault())