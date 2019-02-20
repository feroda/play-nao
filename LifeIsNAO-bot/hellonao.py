#-*- coding: utf-8 -*-

import logging
import time
import argparse
import sys

from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, Bot
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
      [InlineKeyboardButton("/v Nicolas", callback_data="Nicolas"),
      InlineKeyboardButton("/d Valerio", callback_data="Valerio")
      ],
      [
      InlineKeyboardButton("/w Giàcòmo", callback_data="Giacomo"),
      InlineKeyboardButton("/d Nando", callback_data="Nando")
      ],
      [
      InlineKeyboardButton("/p Angelo", callback_data="Angelo"),
      InlineKeyboardButton("/w Gùramrit", callback_data="Guramrit")
      ],
      [
      InlineKeyboardButton("/d Marta", callback_data="Marta"),
      InlineKeyboardButton("/a Amira", callback_data="Amira")
      ],
      [
      InlineKeyboardButton("/w Gùrsharn", callback_data="Gursharn"),
      InlineKeyboardButton("/f Jamila", callback_data="Jamila")
      ],
      [
      InlineKeyboardButton("/finish", callback_data="Fine")
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

def a(bot, update):
    pst = u'Ora parla Amòra, oh scusate {} '.format(
		update.message.text[len('/a '):])

    update.message.reply_text(pst)

    tts = ALProxy("ALTextToSpeech", sockinfo.ip, sockinfo.port)
    tts.say(pst.encode("utf-8"))
    tts.say(pst)

def d(bot, update):
    pst = 'Bene, {} adesso presèntati tu!'.format(
		update.message.text[len('/d '):])

    update.message.reply_text(pst)

    tts = ALProxy("ALTextToSpeech", sockinfo.ip, sockinfo.port)
    tts.say(pst)

def w(bot, update):
    pst = u'{}, è il tuo turno!'.format(
		update.message.text[len('/w '):])

    update.message.reply_text(pst)

    tts = ALProxy("ALTextToSpeech", sockinfo.ip, sockinfo.port)
    tts.say(pst.encode("utf-8"))
    tts.say(pst)

def f(bot, update):
    msg ='Jamila, manchi solo tu, presèntati!'

    tts = ALProxy("ALTextToSpeech", sockinfo.ip, sockinfo.port)
    tts.say(msg)

    update.message.reply_text(msg)

def lol(bot, update):
    msg = 'Amira, hai parlato abbastanza ora basta'

    tts = ALProxy("ALTextToSpeech", sockinfo.ip, sockinfo.port)
    tts.say(msg)    

    update.message.reply_text(msg)

def v(bot, update):
    msg = 'Dai Nìcolas, inizia tu a presentarti!'

    tts = ALProxy("ALTextToSpeech", sockinfo.ip, sockinfo.port)
    tts.say(msg)    

    update.message.reply_text(msg)

# def button(update, context):
#     print("Bottone")
#     query = update.callback_query
#     print ("bottone")
#     query.edit_message_text(text="Selected option: {}".format(query.data))

def error(bot, update, context):
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

def finish(bot, update):
    tts = ALProxy("ALTextToSpeech", sockinfo.ip, sockinfo.port)
    tts.say("Tanti auguri Jamila! Ora festeggiamo insieme!")

    update.message.reply_text(msg)

class HumanAnsweredQuestionModule(ALModule):
    """ A simple module able to react
    to facedetection events
    """
    def __init__(self, name):
        ALModule.__init__(self, name)
        # No need for IP and port here because
        # we have our Python broker connected to NAOqi broker

        self.bot = Bot(TOKEN)
        # Create a proxy to ALTextToSpeech for later use
        self.tts = ALProxy("ALTextToSpeech")

        # Subscribe to the AnswerGiven event:
        self.memory = ALProxy("ALMemory")
        self.memory.subscribeToEvent("AnswerGiven",
            "HumanAnsweredQuestion",
            "onAnswerGiven")

        self.answers = []
        # Inserire qui le domande vere
        self.questions = [
            "Ciao amico io sono nao vuoi che ti faccia delle domande?",
            "Hai mai subito degli atti di bullismo?",
            "Dove hai subito questi atti di bullismo?",
            "E' mai intervenuto qualche professore ad aiutarti?",
            "Che ne dici di parlarne con me?"
        ]

    def onAnswerGiven(self, *args):
        """ This will be called each time an answer is given
        """
        # OLD Unsubscribe to the event when talking,
        # OLD to avoid repetitions
        # OLD self.memory.unsubscribeToEvent("FaceDetected",
        # OLD     "HumanAnsweredQuestion")


        print("Rilevata risposta")
        msg = ""
        for i in range(len(self.questions)):
            try:
                question = self.questions[i]
                answer = self.memory.GetData("domanda/%s" % (i+1))
                msg += u"* Q:%s A:%s\n" % (question, answer)
            except Exception as e:
                # Qui ci va alla prima chiave che non esiste
                # Esce dal ciclo
                break

        # Leggere il valore istantaneo dal sensore
        freq_value = hrm_read()
        msg += " * FREQUENZA: {}\n".format(freq_value)

        #msg += " * FREQUENZA: %s\n" % freq_value
        # Leggere gli ultimi 10 valori dal sensore
        #i = 0
        hrm_read_last_values = hrm_read_buffer()
        last_10_frequencies = "; ".join(hrm_read_last_values[-10:])
        msg += " * ULTIME 10 FREQUENZE: %s\n" % last_10_frequencies


        # Inviare il messaggio al BOT
        self.bot.send_message(EXPERTS_CHAT_ID, msg)

        # OLD Subscribe again to the event
        # OLD self.memory.subscribeToEvent("FaceDetected",
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


# subscribe to event
# nella funzione o nel modulo chiamato come callback si fa
#bot.send_message(chat_id, msg)
# dove msg è il testo recuperato dalla memoria di NAO

    updater = Updater(TOKEN, user_sig_handler=terminate)
    updater.dispatcher.add_handler(CommandHandler('naohello', hello))
    updater.dispatcher.add_handler(CommandHandler('naosay', naosay))
    updater.dispatcher.add_handler(CommandHandler('naopresent', present))
    updater.dispatcher.add_handler(CommandHandler('p', p))
    updater.dispatcher.add_handler(CommandHandler('f', f))
    updater.dispatcher.add_handler(CommandHandler('w', w))
    updater.dispatcher.add_handler(CommandHandler('d', d))
    updater.dispatcher.add_handler(CommandHandler('v', v))
    updater.dispatcher.add_handler(CommandHandler('a', a))
    updater.dispatcher.add_handler(CommandHandler('finish', finish))
    updater.dispatcher.add_handler(CommandHandler('lol', lol))
    # updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('fileread', fileread))
    updater.dispatcher.add_handler(CommandHandler('fileread_media', fileread_media))
    updater.dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
