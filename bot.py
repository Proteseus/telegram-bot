import BookResp as BookRes
import Responses as R
import Menus as M
import logging
from urllib import request
from telegram import  InlineQueryResultArticle, InputTextMessageContent, ParseMode, Update, InlineKeyboardButton, InlineKeyboardMarkup, ForceReply
from telegram.ext import Updater, CallbackQueryHandler, ConversationHandler, CommandHandler, MessageHandler, Filters, CallbackContext, InlineQueryHandler
from uuid import uuid4
import os
import requests

PORT = int(os.environ.get('PORT', 5000))

#logger and API_TOKEN
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
TOKEN = '345076322:AAGCUBpqKatKO62jGm31C8azjy-HLNu9kJk'

status = open("status.txt", 'w')
state = "not_book"
status.write(state)

#####command handlers#####
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

"""def echo(update, context):
    Echo the user message.
    update.message.reply_text(update.message.text)
"""
def book(update, context):
    """Send a message when the command /book is issued."""
    global state 
    state = "book"
    res = open("status.txt", "w")
    res.write(state)
    update.message.reply_text('What book do you want to look for?', reply_markup=ForceReply(), input_field_placeholder="type book name...")
    
def message_hanler(update, context):
    with open("status.txt", "r") as status:
        state = status.read()
    global text
    text= str(update.message.text).lower()
    print(text)
    salute = {"hi", "hello", "who are you", "who are you?", "time", "what time is it?", "what time is it", "levi", "who made you?", "who made you"}
    if text in salute:
        response = R.sample_responses(text)
        update.message.reply_text(response)
    else:
        if state == "book":
            update.message.reply_text(book_func(text, update))
        else:
            update.message.reply_text("Unknown request")
            
def about(update, context):
    update.message.reply_text("I'm a simple personal bot made to serve my creator, @Leviticus_98")

def book_func(bookName, update):
    if(bookName[0] != "/"):
        BookRes.get_book_opt(bookName)
        BookRes.bookResPrinter()
        return BookRes.bookLinks
    else:
        bookID = bookName[1:9]
        print("Book ID: " + bookID)
        if(get_link(bookID)!=None):
            file = file_downloader(get_link(bookID))
            update.message.send_file()

def inline_command(update, context):
    query = update.inline_query.query
    if query == "":
        return

    results = [
        InlineQueryResultArticle(
            id=str(uuid4()),
            title=query.capitalize(),
            input_message_content=InputTextMessageContent(book_func(query, update)),
        )
    ]
    update.inline_query.answer(results)


def get_link(bookID):
    for id in BookRes.dataSnippet:
        if(bookID) == id['file_id']:
            return id['file_link']
        
def file_downloader(link):
    return request.urlretrieve(link)
    
def getBookId(update, context):
    update.message.reply_text("test")

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def purge():
    directory = "./"
    files_in_directory = os.listdir(directory)
    filtered_files = [file for file in files_in_directory if file.endswith(".epub")]

    for file in filtered_files:
	    path_to_file = os.path.join(directory, file)
	    os.remove(path_to_file)
 
    if os.path.exists("results.json"):
        os.remove("results.json")
    
    if os.path.exists("response.txt"):
        os.remove("response.txt")




def main():
    purge()
    
    """Start the bot."""
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    global bookId
    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start_menu", M.start_menu))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("book", book))
    dp.add_handler(CommandHandler("about", about))
    #dp.add_handler(CommandHandler(bookId, getBookId))
    dp.add_handler(MessageHandler(Filters.text , message_hanler))
    #dp.add_handler(CommandHandler(Filters.command, getBookId))
    dp.add_handler(InlineQueryHandler(inline_command))
    #####menu_handlers######
    #dp.add_handler(CommandHandler("Menu", menu))
    dp.add_handler(CallbackQueryHandler(M.main_menu, pattern='main'))
    dp.add_handler(CallbackQueryHandler(M.first_menu, pattern='m1'))
    dp.add_handler(CallbackQueryHandler(M.second_menu, pattern='m2'))
    dp.add_handler(CallbackQueryHandler(M.first_submenu, pattern='m1_1'))
    dp.add_handler(CallbackQueryHandler(M.second_submenu, pattern='m2_1'))
    

    # on noncommand i.e message - echo the message on Telegram
    #dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://test-bot-levi.herokuapp.com/' + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()