from telegram.ext import Updater, CommandHandler

from settings import TOKEN


def hello(bot, update):
    update.message.reply_text(
        'Hello {},sei in chat {}'.format(
		update.message.from_user.first_name,
		update.message.chat.title))


updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()
 
