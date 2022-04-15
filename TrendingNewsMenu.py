from fnmatch import fnmatch
import json
from re import I
import TrendingNews as TN
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

#######declarations#####
def upp():
    TN.get_News()
    TN.pgCounter()
    x = TN.pgCount
    with open('trendingCount.txt','r') as c:
        f = c.read()
        if(int(f) < TN.pgCount):
            f = int(f)+1
            with open('trendingCount.txt','w') as d:
                d.write(str(f))
        else:
            f = x - 1
        print(f)
    return(int(f))

def dwn():
    x = 0
    with open('trendingCount.txt','r') as c:
        f = c.read()
        if(int(f) > -1):
            f = int(f) - 1
            with open('trendingCount.txt','w') as d:
                d.write(str(f))
        else:
            f = x
        print(f)
    return(int(f))

def res():
    with open('trendingCount.txt','w') as d:
        if(d.write('-1')):
            print('count reset...')
        
def news_printer(f):
    with open('trending_news.json', 'r') as St:
        my_dict = json.load(St)

    pgCount = my_dict['totalCount']
    key=['title', 'url', 'snippet', 'datePublished']
    news=''
    for k in key:
        news += str(my_dict['value'][f][k]) + " "
    news += "provider: " + str(my_dict['value'][f]['provider']['name'])
    return news


def menu_picker():
    with open('trendingCount.txt','r') as c:
        f = c.read()
        print(f)
        print(TN.pgCount)
    if(int(f) == 0):
        return first_menu_keyboard()
    elif(int(f) == TN.pgCount - 1):
        return last_menu_keyboard()
    elif(int(f) > 0):
        return second_menu_keyboard()

######menus######
def start_trend_option(update, context):
    with open('trendingCount.txt', 'r') as trc:
        tr = trc.read()
        print(tr)
    res()
    update.message.reply_text(main_menu_message(),
                            reply_markup=main_menu_keyboard())

def main_menu(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(
                        text=main_menu_message(),
                        reply_markup=main_menu_keyboard())

def trend_menu(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(
                        text=first_menu_message(),
                        reply_markup=menu_picker())

def next_menu(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(
                        text=next_menu_message(),
                        reply_markup=menu_picker())

def prev_menu(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(
                        text=prev_menu_message(),
                        reply_markup=menu_picker())
######keyboard####
def main_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Trending', callback_data = 'trn')]]
    return InlineKeyboardMarkup(keyboard)

def first_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Main menu', callback_data = 'news_main')],
                [InlineKeyboardButton('>>', callback_data = 'next')]]
    return InlineKeyboardMarkup(keyboard)

def second_menu_keyboard():
    keyboard = [[InlineKeyboardButton('<<', callback_data = 'prev')],
                [InlineKeyboardButton('Main menu', callback_data='news_main')],
                [InlineKeyboardButton('>>', callback_data = 'next')]]
    return InlineKeyboardMarkup(keyboard)

def last_menu_keyboard():
    keyboard = [[InlineKeyboardButton('<<', callback_data = 'prev')],
                [InlineKeyboardButton('Main menu', callback_data = 'news_main')]]
    return InlineKeyboardMarkup(keyboard)

#####message######
#print interactive message
def main_menu_message():
    TN.get_News()
    return 'Trending News'

def first_menu_message():
    with open('trendingCount.txt','r') as c:
        f = c.read()
    if(int(f) < 0):
        n = upp()
    else:
        n = int(f)
    strT = news_printer(n)
    print(strT)
    return strT

def next_menu_message():
    n = upp()
    str = news_printer(n)
    print(str)
    return str

def prev_menu_message():
    n = dwn()
    str = news_printer(n)
    print(str)
    return str
