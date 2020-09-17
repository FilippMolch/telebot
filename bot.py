import telebot

token = "1030930072:AAFkMta9-uW2FZdgtuJAQ7-52lCwaPGvJtU"
bot = telebot.TeleBot(token)

def get_rasp():
    f = open("rasp.txt", "r")
    txt = f.read()
    return txt

def upd_rasp(ahaha):
    f = open("rasp.txt", "w")
    f.write(ahaha)

@bot.message_handler(content_types=['text'])
def send_text(message):
    try:
        if message.text.lower() == '/rasp':
            bot.send_message(message.chat.id, get_rasp())
        if message.text.lower()[0] == '/' and message.text.lower()[1] == 'u' and message.text.lower()[2] == 'p':
            text = message.text.lower().replace("/update", "")
            upd_rasp(text)
            print(text)
    except Exception as e:
        print("ooops")

bot.polling()
