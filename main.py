import telebot
from telebot import types
token = "5866268119:AAF7dgvd4Qdh6_J2GhxfnAp-u6WcBS8jjYQ"

bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Hi!")


bot.polling()