from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from src.global_variables import specialist_types


in_show_spec_types = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=item['ru'], callback_data=f"show_spec_{item['en']}")]
    for item in specialist_types])

in_choose_spec_types = InlineKeyboardMarkup(inline_keyboard=([
    [InlineKeyboardButton(text=item['ru'], callback_data=f"{item['en']}")]
    for item in specialist_types] + [[InlineKeyboardButton(text='ФИНИШ', callback_data='finish')]]))
