import requests
import json
import telegram
from urllib import request
from bot import book


url = "https://filepursuit.p.rapidapi.com/"


bookName='hyperion'
#search for the book
def get_book_opt(bookName):
    querystring = {"q":bookName,"filetype":"epub","type":"ebook"}
    headers = {
    'x-rapidapi-host': "filepursuit.p.rapidapi.com",
    'x-rapidapi-key': "fbc3f7553bmshc5986cd99c61e17p1514a6jsn9a924f8deda7"
    }
    global response
    response = requests.request("GET", url, headers=headers, params=querystring)
    if (response.status_code == 200):
        print("The request was a success")
        res = open("results.json", "w")
        res.write(response.text)
        with open("results.json", "r") as responseFile:
            global data
            global dataSnippet
            data = json.load(responseFile)
            dataSnippet = data['files_found']
            
            success = "success"
            if(data['status'] == success):
                ro=open("res.txt", "w")
                if(bookName[0]=="/"):
                    bookID = bookName[1:9]
                    print(bookID)
                else:
                    ro.write(bookName)
                bookRes(1)
            else:
                bookRes(0)
    #will only run if the request is successful
    elif (response.status_code == 404):
        print("Result not found!")
    
    print(response)

def bookRes(dataLine):
    pro=open("response.txt", "w")
    if(dataLine==1):
        pro.writelines(("{}" "{}" "\n" "{}" "{}" "\n" "\n" "{}" "{}" "\n" "{}" "{}" "\n" "\n" "{}" "{}" "\n" "{}" "{}" "\n" "\n" "{}" "{}" "\n" "{}" "{}" "\n" "\n" "{}" "{}" "\n" "{}" "{}" "\n" "\n" "{}" "{}" "\n" "{}" "{}" "\n" "\n" "{}" "{}" "\n" "{}" "{}" "\n" "\n").format('ID: /', data['files_found'][0]['file_id'] , 'Name: ', data['files_found'][0]['file_name'], 'ID: /', data['files_found'][1]['file_id'], 'Name: ', data['files_found'][1]['file_name'], 'ID: /', data['files_found'][2]['file_id'], 'Name: ', data['files_found'][2]['file_name'], 'ID: /', data['files_found'][3]['file_id'], 'Name: ', data['files_found'][3]['file_name'], 'ID: /', data['files_found'][4]['file_id'], 'Name: ', data['files_found'][4]['file_name'], 'ID: /', data['files_found'][5]['file_id'], 'Name: ', data['files_found'][5]['file_name'], 'ID: /', data['files_found'][6]['file_id'], 'Name: ', data['files_found'][6]['file_name']))
    else:
        pro.write("No books found with that name!")

def bookResPrinter():
    global bookLinks
    with open("response.txt", "r") as pros:
        bookLinks=pros.read()
    
def getBookFiles():
    telegram.Bot.get_file()

def get_link(bookID):
    for id in dataSnippet:
        if(bookID) == id['file_id']:
            return id['file_link']

def get_title(bookID):
    for id in dataSnippet:
        if(bookID) == id['file_id']:
            return id['file_name']

        
def file_downloader(link, title):
    fileName = ('.\{}').format(title)
    req = requests.get(link)
    file = open(fileName, 'wb')
    for chunk in req.iter_content(10000000000):
        file.write(chunk)
        file.close()
    print("Downloaded")
      