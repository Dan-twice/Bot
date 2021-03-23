import telebot

bot = telebot.TeleBot("1750326917:AAGYFKRGQAwYuT0M-vw0SIam9uIgww2vwWc")


@bot.message_handlers(commands=['start', 'help'])
def get_messages(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.from_user.id, 'Hello human, I\'m your friend')
    else:
        bot.send_message(message.from_user.id, 'What? |(')


bot.polling(none_stop=True)
