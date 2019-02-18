#-*- coding: utf-8 -*-

import logging
import time
import argparse
import sys

from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
#aggiungee "Bot" alla linea sopra
#presentazione conclusa

from naoqi import *
from settings import TOKEN, NAO_IP, NAO_PORT, EXPERTS_CHAT_ID, FILEPATH, BUFFER_FILEPATH

event_received = 0
sockinfo = None

import time

import argparse

import sys

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def hello(bot, update):
    msg = 'Hello {},sei in chat {}'.format(
		update.message.from_user.first_name,
		update.message.chat.title)

    update.message.reply_text(msg)

    tts = ALProxy("ALTextToSpeech", sockinfo.ip, sockinfo.port)
    tts.say(msg)

def naosay(bot, update):
    txt = update.message.text[len('/naosay '):]
    update.message.reply_text(txt)

    tts = ALProxy("ALTextToSpeech", sockinfo.ip, sockinfo.port)
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

    tts = ALProxy("ALTextToSpeech", sockinfo.ip, sockinfo.port)
    tts.say(pst)

# def button(update, context):
#     print("Bottone")
#     query = update.callback_query
#     print ("bottone")
#     query.edit_message_text(text="Selected option: {}".format(query.data))

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def hrm_read():
    """
    return str of heartrate
    """

    with open(FILEPATH) as F:
        line = F.readline()
        if line != 'NODATA' and line != 'ERROR':
            value = float(line)/160
            line = str(value).replace('.', ',')

    return line

def hrm_read_buffer():

    with open(BUFFER_FILEPATH) as F:
        lines = F.read()

    return lines.split("\n")

def fileread(bot, update):

    value = hrm_read()
    update.message.reply_text(value)
    msg = 'Il valore è {}'.format(value)
    tts = ALProxy("ALTextToSpeech", NAO_IP, NAO_PORT)
    tts.say(msg)


def fileread_media(bot, update):
    i = 0
    while(i<10):
      with open(FILEPATH) as F:
        line = F.readline()
        if line != 'NODATA' and line != 'ERROR':
            value = float(line)/160
            i = i+1
        else:
            value = line
        #inserire eventuale delay
        update.message.reply_text(value)

        msg = 'Il valore è {}'.format(
        value
        ).replace('.', ',')

class HumanAnsweredQuestionModule(ALModule):
    """ A simple module able to react
    to facedetection events
    """
    def __init__(self, name):
        ALModule.__init__(self, name)
        # No need for IP and port here because
        # we have our Python broker connected to NAOqi broker

        # Create a proxy to ALTextToSpeech for later use
        self.tts = ALProxy("ALTextToSpeech")

        # Subscribe to the FaceDetected event:
        global memory
        memory = ALProxy("ALMemory")
        memory.subscribeToEvent("AnswerGiven",
            "HumanAnsweredQuestion",
            "onAnswerGiven")

        self.answers = []
        # Inserire qui le domande vere
        self.questions = [
            "Quanti hanni hai?",
            "Hai mangiato oggi?",
        ]

    def onAnswerGiven(self, *args):
        """ This will be called each time an answer is given
        """
        # OLD Unsubscribe to the event when talking,
        # OLD to avoid repetitions
        # OLD memory.unsubscribeToEvent("FaceDetected",
        # OLD     "HumanAnsweredQuestion")


        print("Rilevata risposta")
        msg = ""
        for i in range(len(self.questions)):
            try:
                question = self.questions[i-1]
                answer = memory.GetData("Domanda/%s" % i)
                msg += u"* Q:%s A:%s\n" % (question, answer)
            except Exception as e:
                # Qui ci va alla prima chiave che non esiste
                # Esce dal ciclo
                break

        # Leggere il valore istantaneo dal sensore
        freq_value = hrm_read()
        msg += " * FREQUENZA: {}".format(freq_value)

        #msg += " * FREQUENZA: %s\n" % freq_value
        # Leggere gli ultimi 10 valori dal sensore
        #i = 0
        hrm_read_last_values = hrm_read_buffer()
        last_10_frequencies = "; ".join(hrm_read_last_values[-10:])
        msg += " * ULTIME 10 FREQUENZE: %s\n" % last_10_frequencies


        # Inviare il messaggio al BOT
        # TODO bot.send_message(chat_id, msg)
        bot.send_message(EXPERTS_CHAT_ID, msg)

        # OLD Subscribe again to the event
        # OLD memory.subscribeToEvent("FaceDetected",
        # OLD     "HumanAnsweredQuestion",
        # OLD     "onFaceDetected")

def main():

    # Parse Args
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', default=NAO_IP)
    parser.add_argument('--port', default=NAO_PORT, type=int)
    parser.add_argument('--volume', default=0.8, type=float)
    # Enable or disable naoqi
    # parser.add_argument('--naoqi', action="store_true", default=False)
    global sockinfo
    sockinfo = parser.parse_args()

    #impostazione di lingua e volume
    tts = ALProxy("ALTextToSpeech", sockinfo.ip, sockinfo.port)
    tts.setLanguage("Italian")
    tts.setVolume(sockinfo.volume)

    # Start NAO Broker
    myBroker = ALBroker("myBroker", "0.0.0.0", 0, sockinfo.ip, sockinfo.port)
    # Warning: HumanAnsweredQuestion must be a global variable
    # The name given to the constructor must be the name of the
    # variable
    global HumanAnsweredQuestion
    HumanAnsweredQuestion = HumanAnsweredQuestionModule("HumanAnsweredQuestion")

    # Start BOT
    def terminate(self, signal_name):
        print("Interrupted bot and NAO module by user, shutdown")
        myBroker.shutdown()
        sys.exit(0)

#def Q&A():
#   risp = ALProxy("ALMemory", sockinfo.ip, sockinfo.port)


# bot = Bot(TOKEN)
# subscribe to event
# nella funzione o nel modulo chiamato come callback si fa
#bot.send_message(chat_id, msg)
# dove msg è il testo recuperato dalla memoria di NAO

    updater = Updater(TOKEN, user_sig_handler=terminate)
    updater.dispatcher.add_handler(CommandHandler('naohello', hello))
    updater.dispatcher.add_handler(CommandHandler('naosay', naosay))
    updater.dispatcher.add_handler(CommandHandler('naopresent', present))
    updater.dispatcher.add_handler(CommandHandler('p', p))
    # updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('fileread', fileread))
    updater.dispatcher.add_handler(CommandHandler('fileread_media', fileread_media))
    updater.dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
