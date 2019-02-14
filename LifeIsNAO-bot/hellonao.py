#-*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler 
from telegram import ReplyKeyboardMarkup, InlineKeyboardButton
#aggiungee "Bot" alla linea sopra

from naoqi import ALProxy

from settings import TOKEN, NAO_IP, NAO_PORT


def hello(bot, update):
    msg = 'Hello {},sei in chat {}'.format(
		update.message.from_user.first_name,
		update.message.chat.title)

    update.message.reply_text(msg)

    tts = ALProxy("ALTextToSpeech", NAO_IP, NAO_PORT)
    tts.say(msg)
		
def naosay(bot, update):
    txt = update.message.text[len('/naosay '):]
    update.message.reply_text(txt)
    
    tts = ALProxy("ALTextToSpeech", NAO_IP, NAO_PORT)
    tts.say(txt.encode("utf-8"))
    
def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu

def present(bot, update):
  print("ciao")
  button_table = [
      [InlineKeyboardButton("gura", callback_data="Guramrit"),
      InlineKeyboardButton("gurshy", callback_data="Gursharn")
      ],
      [
      InlineKeyboardButton("remus", callback_data="Valerio"),
      ]
  ]
  print(button_list)
  # reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
  reply_markup = ReplyKeyboardMarkup([button_table])
  print("bau")
  chat_id = update.message.chat.id
  print(chat_id)
  bot.send_message(chat_id, "A two-column menu", reply_markup=reply_markup)

  #  answ = 

#def Q&A():
#   risp = ALProxy("ALMemory", NAO_IP, NAO_PORT)

    
    
#bot = Bot(TOKEN)
# subscribe to event
# nella funzione o nel modulo chiamato come callback si fa
# bot.send_message(chat_id, msg)
# dove msg è il testo recuperato dalla memoria di NAO

updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('naohello', hello))
updater.dispatcher.add_handler(CommandHandler('naosay', naosay))
updater.dispatcher.add_handler(CommandHandler('naopresent', present))

updater.start_polling()
updater.idle()

