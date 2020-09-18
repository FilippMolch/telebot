import telebot
import os

token = ""
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
            if message.from_user.username == "nesteroff561" or message.from_user.username == "FIl_OS":
                text = message.text.lower().replace("/update", "")
                upd_rasp(text)
            else:
                bot.send_message(message.chat.id, "permission denied")
        if message.text.lower()[0:5] == '/exec':
            comand = message.text.lower().replace("/exec", "").replace("&&", ">> file &&")

            for i in range(0, len(comand)):
                print(i)
            comand = comand + " >> file"

            if message.from_user.username == "nesteroff561" or message.from_user.username == "FIl_OS":
                exit_status = os.system(comand)
            else:
                bot.send_message(message.chat.id, "permission denied")

            bot.send_message(message.chat.id, get_file())
            os.remove("file")
        if message.text.lower() == '/help':
            bot.send_message(message.chat.id, "/exec - выполнить команду (доступно только админам)\n/rasp получить расписание\n/update заменить расписание (доступно только админам)")

    except Exception as e:
        print("ooops", e)
        bot.send_message(message.chat.id, "ooops")

bot.polling()
