from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardMarkup, InlineKeyboardButton
)
from aiogram.utils.keyboard import InlineKeyboardBuilder

reply_main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Привет"), KeyboardButton(text="Пока")]
    ],
    resize_keyboard=True
)

links_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Новости", url="https://news.yandex.ru/")],
    [InlineKeyboardButton(text="Музыка",  url="https://music.yandex.ru/")],
    [InlineKeyboardButton(text="Видео",   url="https://www.youtube.com/")]
])

def dynamic_show_more_kb():
    b = InlineKeyboardBuilder()
    b.add(InlineKeyboardButton(text="Показать больше", callback_data="show_more"))
    return b.as_markup()

def dynamic_options_kb():
    b = InlineKeyboardBuilder()
    b.row(
        InlineKeyboardButton(text="Опция 1", callback_data="opt_1"),
        InlineKeyboardButton(text="Опция 2", callback_data="opt_2"),
    )
    return b.as_markup()
