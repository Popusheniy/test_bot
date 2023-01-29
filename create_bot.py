from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()


bot = Bot(token='5460512250:AAH-J-Waecyaz599PXCfwNhM2Xee1W-woXc')
dp = Dispatcher(bot, storage=storage)
