from aiogram import Bot, Dispatcher, types
from aiogram import executor
from aiogram.types.web_app_info import WebAppInfo
bot = Bot('6346948655:AAHBSmcIJQ6urXbs5fvFcy8hQHrmjuty_A4')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть Веб Страницу', web_app=WebAppInfo(url='http://localhost:8000/')))
    await message.answer('Привет!', reply_markup=markup)



executor.start_polling(dp)
