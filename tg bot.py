import telebot
import webbrowser

bot = telebot.TeleBot('6791630495:AAFTdZTcyLeE3hcr0AKjS357xZ-xevT3Nfo')





@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, '<b>hello, my dear</b> <em>friend</em>', parse_mode="html")


@bot.message_handler(commands=['website', 'site'])
def site(message):
    bot.send_message(message.chat.id, 'https://www.youtube.com/')


@bot.message_handler(commands=['browser'])
def browser(message):
    webbrowser.open('https://www.youtube.com/')
 

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id,
    f'hello, {message.from_user.first_name} {message.from_user.last_name}')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'hi':
        bot.send_message(message.chat.id,
        f'hello, {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID {message.from_user.id}')




@bot.message_handler(content_types='photo')
def photo(message):
    bot.reply_to(message,'handsome')


bot.polling(none_stop=True)