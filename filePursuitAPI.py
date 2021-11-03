from __main__ import *
import requests
import json
import os

if os.path.exists("results.json"):
    os.remove("results.json")

url = "https://filepursuit.p.rapidapi.com/"


#function for setting search params
import bot
#import test
titl=bot.echoBook()
#titl=test.tes
querystring = {"q":titl,"filetype":"epub","type":"ebook"}

headers = {
    'x-rapidapi-host': "filepursuit.p.rapidapi.com",
    'x-rapidapi-key': "fbc3f7553bmshc5986cd99c61e17p1514a6jsn9a924f8deda7"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

def bookRes():
    print('Name:', data['files_found'][0]['file_name'])
    print('Link:', data['files_found'][0]['file_link'])

    print(' ')

    print('Name:', data['files_found'][1]['file_name'])
    print('Link:', data['files_found'][1]['file_link'])
    
    print(' ')

    print('Name:', data['files_found'][2]['file_name'])
    print('Link:', data['files_found'][2]['file_link'])
    
    print(' ')

    print('Name:', data['files_found'][3]['file_name'])
    print('Link:', data['files_found'][3]['file_link'])

if (response.status_code == 200):
    print("The request was a success")
    res = open("results.json", "w")
    res.write(response.text)
    with open("results.json", "r") as responseFile:
        data = json.load(responseFile)

    #bookRes()
    bot.sendBook()
        
    # Code here will only run if the request is successful
elif (response.status_code == 404):
    print("Result not found!")
    
print(response)
