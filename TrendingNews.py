import requests
import json

url = 'https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/search/TrendingNewsAPI'

querystring = {"pageNumber":"1","pageSize":"50","withThumbnails":"true","location":"us"}

headers = {
    'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com",
    'x-rapidapi-key': "f22f49748fmsh89ce16976c53c94p191a6djsn2d288ad626fe"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

def pgCounter():
    with open('trending_news.json', 'r') as St:
        my_dict = json.load(St)
    St.close()

    global pgCount 
    pgCount = my_dict['totalCount']


def get_News():
    print(response)
    if (response.status_code == 200):
        print("The request was a success")
        with open("trending_news.json", "w") as res:
            res.write(response.text)
        with open("trending_news.json", "r") as readFile:
            global data
            data = json.load(readFile)

        if (data['_type'] == 'news'):
            with open("trending_news.txt", "w") as ro:
                ro.writelines(("{}" "{}" "\n" "\n" "{}" "{}" "\n" "\n" "{}" "{}" "\n" "\n" "{}" "{}" "\n" "\n" "{}" "{}" "\n").format("Title: ", data['value'][0]['title'], "Source: ", data['value'][0]['url'], "Snippet: ", data['value'][0]['snippet'], "Date: ", data['value'][0]['datePublished'], "Publisher: ", data['value'][0]['provider']['name']))

    elif (response.status_code == 404):
        print("Result not found!")
        with open("report_covid.txt", "w") as ro:
            ro.write("Result not found!")
    elif(response.status_code == 502):
        print("API DOWN")
        with open("report_covid.txt", "w") as ro:
            ro.write("API DOWN")


def news_printer():
    global news
    with open("trending_news.txt", "r") as pros:
        news = pros.read()
    return news


def news_printer():
    pgCounter()
    with open('trending_news.json', 'r') as St:
        my_dict = json.load(St)

    key=['title', 'url', 'snippet', 'datePublished']
    news=''
    for k in key:
        news += str(my_dict['value'][0][k]) + "\n"
    news += "provider: " + str(my_dict['value'][0]['provider']['name'])
    return news
