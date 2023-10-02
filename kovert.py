import telebot
from currency_converter import CurrencyConverter
from telebot import types

bot = telebot.TeleBot('6346948655:AAHBSmcIJQ6urXbs5fvFcy8hQHrmjuty_A4')
currency = CurrencyConverter()
amount = 0


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Privet Vvedite Summu')
    bot.register_next_step_handler(message, summa)


def summa(message):
    global amount
    try:
        amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'Kluda Drugaja Summa')
        bot.register_next_step_handler(message, summa)
        return


    if amount > 0:
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
        btn2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
        btn3 = types.InlineKeyboardButton('GBP/EUR', callback_data='gbp/eur')
        btn4 = types.InlineKeyboardButton('Drugoe Znachenie', callback_data='else')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, 'Choose Currency', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Kluda Drugaja Summa')
        bot.register_next_step_handler(message, summa)

@bot.callback_query_handler(func = lambda call: True)
def callback(call):
    if call.data != 'else':
        values = call.data.upper().split('/')
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(call.message.chat.id, f'Poluchaets: {round(res, 2)}.New request')
        bot.register_next_step_handler(call.message, summa)
    else:
        bot.send_message(call.message.chat.id, 'insert values')
        bot.register_next_step_handler(call.message, my_currency)

def my_currency(message):
    try:
        values = message.text.upper().split('/')
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(message.chat.id, f'Poluchaets: {round(res, 2)}.New request')
        bot.register_next_step_handler(message, summa)
    except:
        bot.send_message(message.chat.id, 'Chto-to ne tak. New value')
        bot.register_next_step_handler(message, my_currency)

bot.polling(none_stop=True)
