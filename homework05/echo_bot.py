import telebot
from telebot import apihelper

access_token = '811668477:AAGXDa7U_jS2Oln0ei8cKHRkQf-4WOcxrq0'
apihelper.proxy = {'https': 'https://23.237.22.172:3128'}
bot = telebot.TeleBot(access_token)


@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling()
    
