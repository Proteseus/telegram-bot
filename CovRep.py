import CovCompGlobal as CovG
import CovCompCountry as CovC
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

######menus######
def start_covrep_option(update, context):
      update.message.reply_text(main_menu_message(),
                            reply_markup=main_menu_keyboard())

def main_menu(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(
                        text=main_menu_message(),
                        reply_markup=main_menu_keyboard())

def first_menu(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(
                        text=first_menu_message(),
                        reply_markup=first_menu_keyboard())

def second_menu(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(
                        text=second_menu_message(),
                        reply_markup=second_menu_keyboard())

######keyboard####
def main_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Ethiopia', callback_data='eth')],
              [InlineKeyboardButton('Global', callback_data='global')]]
    return InlineKeyboardMarkup(keyboard)

def first_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Main menu', callback_data='cov_main')]]
    return InlineKeyboardMarkup(keyboard)

def second_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Main menu', callback_data='cov_main')]]
    return InlineKeyboardMarkup(keyboard)

#####message######
def main_menu_message():
    return 'Covid-19 Report'

def first_menu_message():
    CovC.get_country()
    strC = CovC.report_printer()
    print(strC)
    return strC

def second_menu_message():
    CovG.get_global()
    str = CovG.report_printer()
    print(str)
    return str