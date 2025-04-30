import telebot

TOKEN = "8152614638:AAEtIoLJbEmtwLy5rwEZaLaxI01nKIi09q4"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Я живой!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, f"Ты сказал: {message.text}")

bot.polling()
