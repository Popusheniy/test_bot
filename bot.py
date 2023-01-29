from os import link
from aiogram import types
from aiogram.utils import executor
from create_bot import dp, bot


async def on_startup(_):
    print('Бот вышел в онлайн, прям как твой батя за хлебом')


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
