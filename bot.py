import telebot

token = "1030930072:AAFkMta9-uW2FZdgtuJAQ7-52lCwaPGvJtU"
bot = telebot.TeleBot(token)

def get_rasp():
    f = open("rasp.txt", "r")
    txt = f.read()
    return txt

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == '/rasp':
        bot.send_message(message.chat.id, get_rasp())

bot.polling()
