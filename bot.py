import telebot

token = "1137248984:AAH2EtPd-7oVmq2Oo6FZTd1RiZh4nrBoxWY"
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
        bot.send_message(message.chat.id, "ooops:\nfile empty")

bot.polling()
