import config
import telebot

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=['document'])
def handle_message(message):
    # bot.send_message(message.chat.id, message.text)
    with open('./cancel.png', 'rb') as f1:
        bot.send_document(message.chat.id, f1)

bot.polling()