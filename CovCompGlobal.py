import requests
import json

url = 'https://covid-19-data.p.rapidapi.com/totals'

headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': "f22f49748fmsh89ce16976c53c94p191a6djsn2d288ad626fe"
}

response = requests.request("GET", url, headers=headers)

def get_global():
    print(response)
    if response.status_code == 200:
        print("The request was a success")
        with open("covid_global_response.json", "w") as res:
            res.write(response.text)
        with open("covid_global_response.json", "r") as readFile:
            global data
            data = json.load(readFile)

        with open("report_covid.txt", "w") as ro:
            ro.writelines(("{}" "\n" "{}" "{}" "\n" "{}" "{}" "\n" "{}" "{}" "\n" "{}" "{}" "\n" "{}" "{}" "\n").format("Global", "Confirmed: ", data[0]['confirmed'], "Recovered: ", data[0]['recovered'], "Critical: ", data[0]['critical'], "Deaths: ", data[0]['deaths'], "Updated: ", data[0]['lastUpdate']))

    elif (response.status_code == 404):
        print("Result not found!")
        with open("report_covid.txt", "w") as ro:
            ro.write("Result not found!")
    elif(response.status_code == 502):
        print("API DOWN")
        with open("report_covid.txt", "w") as ro:
            ro.write("API DOWN")
    

def report_printer():
    global report_covid
    with open("report_covid.txt", "r") as pros:
        report_covid = pros.read()
    return report_covid
