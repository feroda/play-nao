#-*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
#aggiungee "Bot" alla linea sopra
#presentazione conclusa

from naoqi import ALProxy

from settings import TOKEN, NAO_IP, NAO_PORT

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

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
      [InlineKeyboardButton("/p Valerio", callback_data="1"),
      InlineKeyboardButton("/p Guramrit", callback_data="Guramrit")
      ],
      [
      InlineKeyboardButton("/p Gursharn", callback_data="Gursharn"),
      InlineKeyboardButton("/p Angelo", callback_data="Angelo")
      ],
      [
      InlineKeyboardButton("/p Ferdinando", callback_data="Ferdinando"),
      InlineKeyboardButton("/p Nicolas", callback_data="Nicolas")
      ],
      [
      InlineKeyboardButton("/p Marta", callback_data="Marta"),
      InlineKeyboardButton("/p Amira", callback_data="Amira")
      ],
      [
      InlineKeyboardButton("/p Jamila", callback_data="Jamila"),
      InlineKeyboardButton("/p Giacomo", callback_data="Giacomo")
      ]
  ]
  print(button_table)
  reply_markup = InlineKeyboardMarkup(build_menu(button_table, n_cols=2))
  reply_markup = ReplyKeyboardMarkup(button_table)
  print("bau")
  chat_id = update.message.chat.id
  print(chat_id)
  bot.send_message(chat_id, "Ecco qui il menu", reply_markup=reply_markup)

def p(bot, update):
    pst = 'Ora parla {}'.format(
		update.message.text[len('/p '):])

    update.message.reply_text(pst)

    tts = ALProxy("ALTextToSpeech", NAO_IP, NAO_PORT)
    tts.say(pst)

# def button(update, context):
#     print("Bottone")
#     query = update.callback_query
#     print ("bottone")
#     query.edit_message_text(text="Selected option: {}".format(query.data))

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


  #  answ = 

#def Q&A():
#   risp = ALProxy("ALMemory", NAO_IP, NAO_PORT)

    
    
#bot = Bot(TOKEN)
# subscribe to event
# nella funzione o nel modulo chiamato come callback si fa
# bot.send_message(chat_id, msg)
# dove msg è il testo recuperato dalla memoria di NAO

def main():
  updater = Updater(TOKEN)

  updater.dispatcher.add_handler(CommandHandler('naohello', hello))
  updater.dispatcher.add_handler(CommandHandler('naosay', naosay))
  updater.dispatcher.add_handler(CommandHandler('naopresent', present))
  updater.dispatcher.add_handler(CommandHandler('p', p))
 # updater.dispatcher.add_handler(CallbackQueryHandler(button))
  updater.dispatcher.add_error_handler(error)

  updater.start_polling()
  updater.idle()

if __name__ == '__main__':
  main()