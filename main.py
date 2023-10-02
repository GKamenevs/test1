import telebot
from telebot import types

bot = telebot.TeleBot('6346948655:AAHBSmcIJQ6urXbs5fvFcy8hQHrmjuty_A4')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Perejti na site')
    markup.row(btn1)
    btn2 = types.KeyboardButton('delete')
    btn3 = types.KeyboardButton('Edit Text')
    markup.row(btn2, btn3)
    file = open('./img.png', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup)
    #bot.send_message(message.chat.id, 'Privet!', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'delete':
        bot.send_message(message.chat.id, 'website is open')
    elif message.text == 'Edit Text':
        bot.send_message(message.chat.id, 'website is open')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Perejti na site', url='https://pypi.org/project/pyTelegramBotAPI/#getting-started')
    markup.row(btn1)
    markup.add(types.InlineKeyboardButton('delete', callback_data='delete'))
    markup.add(types.InlineKeyboardButton('Edit Text', callback_data='edit'))
    bot.reply_to(message, 'Kakoe krasivoe photo!',reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
      bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)

bot.polling(none_stop=True)

