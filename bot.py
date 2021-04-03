import config
import telebot

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=['text'])
def handle_message(message):
    bot.send_message(message.chat.id, message.text)

bot.polling()