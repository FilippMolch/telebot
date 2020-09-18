import telebot
import os

token = "1137248984:AAH2EtPd-7oVmq2Oo6FZTd1RiZh4nrBoxWY"
bot = telebot.TeleBot(token)

def get_rasp():
    f = open("rasp.txt", "r")
    txt = f.read()
    return txt

def get_file():
    f = open("file", "r")
    txt_2 = f.read()
    return txt_2

def upd_rasp(ahaha):
    f = open("rasp.txt", "w")
    f.write(ahaha)

@bot.message_handler(content_types=['text'])
def send_text(message):
    try:
        if message.text.lower() == '/rasp':
            bot.send_message(message.chat.id, get_rasp())
        if message.text.lower()[0:7] == '/update':
            text = message.text.lower().replace("/update", "")
            upd_rasp(text)
            print(text)
        if message.text.lower()[0:5] == '/exec':
            print("yes")
            comand = message.text.lower().replace("/exec", "").replace("&&", ">> file &&")

            for i in range(0, len(comand)):
                print(i)

            comand = comand + " >> file"

            print(comand)
            exit_status = os.system(comand)
            bot.send_message(message.chat.id, get_file())
            os.remove("file")

    except Exception as e:
        print("ooops", e)
        bot.send_message(message.chat.id, "ooops:\nfile empty")

bot.polling()
