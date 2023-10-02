import telebot
import requests
import json

bot = telebot.TeleBot('6346948655:AAHBSmcIJQ6urXbs5fvFcy8hQHrmjuty_A4')
API = '7056c20c3c5c9b00a9a147c2b3e6ef3c'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Privet napishi nazani goroda! 0_0')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Sejchas pogoda: {temp}')

        image = 'sun.jpg' if temp > 5.0 else 'cloud.jpg'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, 'Gorod ukazan ne verno')
bot.polling(none_stop=True)
