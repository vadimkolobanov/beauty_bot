from aiogram import Dispatcher, Bot, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from datetime import datetime
import os

from src.states.specialist import CreatingCard
from src.kayboards.inline import in_choose_spec_types
from src.global_variables import db


async def start_specialist(message: Message):
    await message.answer("Для того чтобы ваша анкета была видна клиентам ее нужно создать")


async def create_card(message: Message, state: FSMContext):
    await message.answer("Окей, давай создадим твою карту. Ваше имя:")
    await state.set_state(CreatingCard.NAME)


async def add_name(message: Message, state:FSMContext):
    await message.answer("Выберите сферы на которых вы специализируетесь, "
                         "после этого нажмите на ФИНИШ:", reply_markup=in_choose_spec_types),
    await state.update_data(name=message.text)
    await state.set_state(CreatingCard.SPECIFICATIONS)


async def add_specifications(callback: CallbackQuery, state: FSMContext):
    if callback.data == "finish":
        await callback.message.delete()
        await callback.message.answer("Теперь если хотите добавте короткое описание:")
        await state.set_state(CreatingCard.TEXT)
    else:
        data = await state.get_data()
        specifications = data.get('specifications') if data.get('specifications') else []
        await state.update_data(specifications=(specifications + [callback.data]))


async def add_text(message: Message, state: FSMContext):
    await message.answer("Могу предложить вам добавить также фото:")
    await state.update_data(text=message.text)
    await state.set_state(CreatingCard.PHOTO)


async def add_photo(message: Message, bot: Bot, state: FSMContext):
    photo = message.photo[-1]
    date = f"{datetime.now().day}.{datetime.now().month}.{datetime.now().year}"
    folder = os.path.join('./photos', date)
    if not os.path.exists(folder):
        os.makedirs(folder)

    path = os.path.join(folder, photo.file_unique_id + '.png')
    await bot.download(file=photo, destination=path)

    data = await state.get_data()
    await state.clear()

    await db.add_specialist(
        user_id=message.from_user.id,
        name=data.get('name'),
        specifications=str(data.get('specifications')),
        text=data.get('text'),
        photo=path
    )


async def add_bot(message: Message):
    pass # add own bot which I can handle


def register_handlers(dp: Dispatcher):
    dp.message.register(start_specialist, Command(commands=['specialist']))

    # FSM
    dp.message.register(create_card, F.text == "create_card")
    dp.message.register(add_name, CreatingCard.NAME)
    dp.callback_query.register(add_specifications, CreatingCard.SPECIFICATIONS)
    dp.message.register(add_text, CreatingCard.TEXT)
    dp.message.register(add_photo, CreatingCard.PHOTO)
