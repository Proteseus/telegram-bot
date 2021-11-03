#Author: Horriblebob11

from __main__ import *
import logging
import telebot
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
import filePursuitAPI
PORT = int(os.environ.get('PORT', 5000))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = '345076322:AAF09Z_BdVWmJulCNVKZgagZgp7wBVkUemk'

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("book", book))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, exec(open("filePursuitAPI.py").read())))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://leviticus-bot.herokuapp.com/' + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()
    
# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def book(update, context):
    """Send a message when the command /book is issued."""
    update.message.reply_text("Send Me The Book's Name:")
    
def echoBook(update, context):
    """Pass the book request."""
    bookReq=update.message.text
    return bookReq

def sendBook(update, context):
    """Pass the book."""
    update.message.reply_text('Name:', filePursuitAPI.data['files_found'][0]['file_name'], '\n', 'Link:', filePursuitAPI.data['files_found'][0]['file_link'],
                              '\n\n', 'Name:', filePursuitAPI.data['files_found'][1]['file_name'], '\n', 'Link:', filePursuitAPI.data['files_found'][1]['file_link'],
                              '\n\n', 'Name:', filePursuitAPI.data['files_found'][2]['file_name'], '\n', 'Link:', filePursuitAPI.data['files_found'][2]['file_link'],
                              '\n\n', 'Name:', filePursuitAPI.data['files_found'][3]['file_name'], '\n', 'Link:', filePursuitAPI.data['files_found'][3]['file_link'])

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)



if __name__ == '__main__':
    main()