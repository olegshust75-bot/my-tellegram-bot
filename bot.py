import asyncio import logging import os from aiogram import Bot, Dispatcher, types from aiogram.filters import CommandStart
Отримуємо токен із системної змінної Render
TOKEN = os.getenv("TOKEN")
bot = Bot(token=TOKEN) dp = Dispatcher()
@dp.message(CommandStart()) async def command_start_handler(message: types.Message): await message.answer("Привіт! Я працюю на Render.com 🚀")
@dp.message() async def echo_handler(message: types.Message): await message.answer(f"Отримано: {message.text}")
async def main(): logging.basicConfig(level=logging.INFO) await dp.start_polling(bot)
if name == "main": asyncio.run(main())