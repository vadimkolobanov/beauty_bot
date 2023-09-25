from aiogram import Dispatcher, Bot, F
from aiogram.types import Message, CallbackQuery, InputFile, FSInputFile
from aiogram.filters import Command
from pathlib import Path

from src.kayboards.inline import in_show_spec_types
from src.emoji import Emoji
from src.global_variables import db


async def start(message: Message) -> None:
    await db.add_user(
        user_id=message.from_user.id,
        username=message.from_user.username,
        name=message.from_user.full_name
    )
    await message.answer(
        f'{Emoji.WAVING_HAND} Привет!\n'
        f'Я помогу тебе найти с поиском специалиста на любой вкус)\n\n'
        f'{Emoji.WRITING_HAND} Пишите @david_krbnv с какими-либо вопросами.'
    )


async def settings(message: Message) -> None:     # todo # changing language # add inline buttons #
    await message.answer(
        f'{Emoji.GEAR} Настройки:\n'
        f'{Emoji.SMALL_BLUE_DIAMOND} Мой язык - русский;\n'
        f'{Emoji.SMALL_BLUE_DIAMOND} ;\n'
        f'{Emoji.SMALL_BLUE_DIAMOND} ;\n'   
        f'{Emoji.SMALL_BLUE_DIAMOND} ;\n'
    )


async def support(message: Message, bot: Bot) -> None:
    await message.answer(
        f'{Emoji.WRITING_HAND} Пишите @david_krbnv с какими-либо вопросами:\n'
        f'{Emoji.HAMMER} неполадки в работе сервиса;\n'
        f'{Emoji.LIGHT_BULB} предложения и замечания;\n'
        f'{Emoji.MONEY_BAG} возврат денег;\n'
        f'{Emoji.WINK} что-либо ещё...\n\n'
        f'Твой идентификатор: {message.from_user.id}'
    )
    await bot.send_contact(
        chat_id=message.chat.id,
        phone_number="+380984879807",
        first_name="Davyd",
        last_name="Kurbanov"
    )


async def about(message: Message, bot: Bot) -> None:
    await start(message)
    await bot.send_contact(
        chat_id=message.chat.id,
        phone_number="+380984879807",
        first_name="Davyd",
        last_name="Kurbanov"
    )


async def add_comment(message: Message, bot: Bot) -> None:
    await message.answer()


async def choose_specialist_types(message: Message) -> None:
    await message.answer('Выберите специалиста:', reply_markup=in_show_spec_types)


async def show_specialists(callback: CallbackQuery, bot: Bot) -> None:
    await callback.message.delete()
    specialists = await db.get_specialists(specification=callback.data.replace("spec_", ""))
    for specialist in specialists:
        text = f"<b>\t{specialist['name']}</b>\n"\
                 f"<i>{' '.join([f'#{key}' for key, value in specialist.items() if value == 1])}</i>"
        if "text" in specialist:
            text += f"\n\n<b>P.S.</b>: {specialist['text']}"

        if "photo" in specialist:
            photo = FSInputFile(path=specialist['photo'])
            await bot.send_photo(chat_id=callback.message.chat.id, photo=photo, caption=text)
        else:
            await callback.message.answer(text=text)


def register_handlers(dp: Dispatcher):
    dp.message.register(start, Command(commands=['start', 'run']))
    dp.message.register(settings, Command(commands='settings'))
    dp.message.register(support, Command(commands='support'))
    dp.message.register(about, Command(commands='about'))
    dp.message.register(choose_specialist_types, Command(commands='specialist_types'))
    dp.callback_query.register(show_specialists, F.data.startswith('spec_'))
