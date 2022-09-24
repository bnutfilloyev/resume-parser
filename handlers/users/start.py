from aiogram import types

from loader import dp


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Iltimos resume yuboring")
