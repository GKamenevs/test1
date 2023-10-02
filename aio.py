from aiogram import Bot, Dispatcher, types
from aiogram import executor
bot = Bot('6346948655:AAHBSmcIJQ6urXbs5fvFcy8hQHrmjuty_A4')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    #await bot.send_message(message.chat.id, 'Hello')
    #await message.answer('Hello')
    await message.reply('Hello')
    #await  message.answer_photo(file)

@dp.message_handler(commands=['inline'])
async def info(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Site', url='https://web.telegram.org/k/'))
    markup.add(types.InlineKeyboardButton('Hellow', callback_data= 'hello'))
    await message.reply('Hello', reply_markup=markup)

@dp.callback_query_handler()
async def callback(call):
    await call.message.answer(call.data)

@dp.message_handler(commands=['reply'])
async def reply(message: types.Message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(types.KeyboardButton('Site'))
    markup.add(types.KeyboardButton('webSite'))
    await message.answer('Hello', reply_markup=markup)

executor.start_polling(dp)
