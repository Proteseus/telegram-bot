#Author - Debrye
import starter as St
import BookResp as BookRes
import Responses as R
import Menus as M
import CovRep as Cov
import TrendingNewsMenu as TRN
import logging
from urllib import request
from telegram import  InlineQueryResultArticle, InputTextMessageContent, ParseMode, Update, InlineKeyboardButton, InlineKeyboardMarkup, ForceReply
from telegram import Updater, CallbackQueryHandler, ConversationHandler, CommandHandler, MessageHandler, Filters, CallbackContext, InlineQueryHandler
from uuid import uuid4
import os
import schedule as SCH
import telepot

PORT = int(os.environ.get('PORT', 5000))

#logger and API_TOKEN
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
TOKEN = '345076322:AAEGAPyYAzCJSAWXk9WjvJgmwGU69EonAms'

#####command handlers#####
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

def help(update, context):
    #Send a message when the command /help is issued.
    help_str = R.help()
    update.message.reply_text(help_str)

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
    
def message_handler(update, context):
    with open("status.txt", "r") as status:
        state = status.read()
    global text
    text= str(update.message.text).lower()
    print(text)
    print(state)
    salute = {"hi", "hello", "who are you", "who are you?", "time", "what time is it?", "what time is it", "levi", "who made you?", "who made you", "help"}
    if state == "book":
        update.message.reply_text(book_func(text, update))
        state = "not_book"
        with open("status.txt", 'w') as status2:
            status2.write(state)
    elif text[0] == "/":
        book_func(text, update)
        print ("Downloading......")
    else:
        if text in salute:
            response = R.sample_responses(text)
            update.message.reply_text(response)
        else:
            update.message.reply_text("Unknown request")
            
def about(update, context):
    update.message.reply_text("I'm a simple personal bot made to serve my creator, @Leviticus_98")
    
"""def covid(update, context):
    Cov.get_country()
    reportC = Cov.report_printer()
    update.message.reply_text(reportC)
    print("Local report retrieved")

    Cov.get_global()
    reportG = Cov.report_printer()
    update.message.reply_text(reportG)
    print("Global report retrieved")"""

def schedule(update, context):
    update.message.reply_text(SCH.schedule())

def book_func(bookName, update):
    if(bookName[0] != "/"):
        BookRes.get_book_opt(bookName)
        BookRes.bookResPrinter()
        return BookRes.bookLinks
    else:
        bookID = bookName[1:9]
        print("Book ID: " + bookID)
        if(BookRes.get_link(bookID)!=None):
            BookRes.file_downloader(BookRes.get_link(bookID), BookRes.get_title(bookID))
            #update.message.reply_text(BookRes.get_link(bookID))
            
            bot = telepot.Bot(TOKEN)
            output_file = open(BookRes.get_title(bookID), 'rb')
            #send document by chat id
            bot.sendDocument("344776272", output_file)
            purge()



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



#--------------------------------------------------------#
def main():
    purge()
    St.starter()
    
    """Start the bot."""
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    global bookId
    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start_menu", M.start_menu))
    #dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("book", book))
    dp.add_handler(CommandHandler("about", about))
    dp.add_handler(CommandHandler("covid", Cov.start_covrep_option))
    dp.add_handler(CommandHandler("news", TRN.start_trend_option))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("schedule", schedule))
    dp.add_handler(MessageHandler(Filters.text , message_handler))
    #dp.add_handler(CommandHandler(Filters.command, getBookId))
    dp.add_handler(InlineQueryHandler(inline_command))
    #####menu_handlers######
    #dp.add_handler(CommandHandler("Menu", menu))
    dp.add_handler(CallbackQueryHandler(M.main_menu, pattern='main'))
    dp.add_handler(CallbackQueryHandler(M.first_menu, pattern='m1'))
    dp.add_handler(CallbackQueryHandler(M.second_menu, pattern='m2'))
    dp.add_handler(CallbackQueryHandler(M.first_submenu, pattern='m1_1'))
    dp.add_handler(CallbackQueryHandler(M.second_submenu, pattern='m2_1'))

    dp.add_handler(CallbackQueryHandler(Cov.main_menu, pattern='cov_main'))
    dp.add_handler(CallbackQueryHandler(Cov.first_menu, pattern='eth'))
    dp.add_handler(CallbackQueryHandler(Cov.second_menu, pattern='global'))

    dp.add_handler(CallbackQueryHandler(TRN.main_menu, pattern='news_main'))
    dp.add_handler(CallbackQueryHandler(TRN.trend_menu, pattern='trn'))
    dp.add_handler(CallbackQueryHandler(TRN.next_menu, pattern='next'))
    dp.add_handler(CallbackQueryHandler(TRN.prev_menu, pattern='prev'))
    
    

    # on noncommand i.e message - echo the message on Telegram
    #dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://test-bot-leviathan.herokuapp.com/' + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()