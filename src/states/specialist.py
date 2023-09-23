from aiogram.fsm.state import StatesGroup, State


class CreatingCard(StatesGroup):
    NAME = State()
    SPECIFICATIONS = State()
    TEXT = State()
    PHOTO = State()

