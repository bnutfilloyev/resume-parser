from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import nltk

from config import load_config
from utils.database import MongoDB

nltk.download('stopwords')

config = load_config()
bot = Bot(token=config.bot.token, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = MongoDB()
