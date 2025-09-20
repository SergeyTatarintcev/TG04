import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, BotCommand
from aiogram.fsm.storage.memory import MemoryStorage

import keyboards as kb
from config import TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())

async def setup_bot_commands():
    commands = [
        BotCommand(command="start",   description="Запуск меню с кнопками"),
        BotCommand(command="links",   description="Ссылки: новости/музыка/видео"),
        BotCommand(command="dynamic", description="Динамическая inline-клавиатура"),
        BotCommand(command="help",    description="Справка и показать меню"),
        BotCommand(command="menu",    description="Показать меню с кнопками"),
    ]
    await bot.set_my_commands(commands)

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Меню:", reply_markup=kb.reply_main)

@dp.message(F.text == "Привет")
async def say_hello(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}!")

@dp.message(F.text == "Пока")
async def say_bye(message: Message):
    await message.answer(f"До свидания, {message.from_user.first_name}!")

@dp.message(Command("links"))
async def cmd_links(message: Message):
    await message.answer("Полезные ссылки:", reply_markup=kb.links_kb)

@dp.message(Command("dynamic"))
async def cmd_dynamic(message: Message):
    await message.answer("Динамическое меню:", reply_markup=kb.dynamic_show_more_kb())

@dp.callback_query(F.data == "show_more")
async def cb_show_more(callback: CallbackQuery):
    await callback.message.edit_text("Выберите опцию:", reply_markup=kb.dynamic_options_kb())
    await callback.answer()

@dp.callback_query(F.data == "opt_1")
async def cb_opt1(callback: CallbackQuery):
    await callback.message.answer("Вы выбрали: Опция 1")
    await callback.answer()

@dp.callback_query(F.data == "opt_2")
async def cb_opt2(callback: CallbackQuery):
    await callback.message.answer("Вы выбрали: Опция 2")
    await callback.answer()

@dp.message(Command("help"))
async def cmd_help(message: Message):
    text = (
        "Доступные команды:\n"
        "/start — меню с кнопками\n"
        "/links — ссылки\n"
        "/dynamic — динамическая клавиатура\n"
        "/help — справка\n"
        "/menu — показать меню\n"
    )
    await message.answer(text, reply_markup=kb.reply_main)

@dp.message(Command("menu"))
async def cmd_menu(message: Message):
    await message.answer("Меню:", reply_markup=kb.reply_main)

async def main():
    await setup_bot_commands()
    await bot.delete_webhook(drop_pending_updates=True)
    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
