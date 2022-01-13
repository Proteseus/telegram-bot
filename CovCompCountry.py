import requests
import json

url = 'https://covid2019-api.herokuapp.com/v2/country/ethiopia'

response = requests.request("GET", url)

def get_country():
    print(response)
    if (response.status_code == 200):
        print("The request was a success")
        with open("covid_country_response.json", "w") as res:
            res.write(response.text)
        with open("covid_country_response.json", "r") as readFile:
            global data
            data = json.load(readFile)

        if (data['data']['location'] == 'Ethiopia'):
            with open("report_covid_country.txt", "w") as ro:
                ro.writelines(("{}" "\n" "{}" "{}" "\n" "{}" "{}" "\n" "{}" "{}" "\n" "{}" "{}" "\n" "{}" "{}" "\n").format(data['data']['location'], "Confirmed: ", data['data']['confirmed'], "Active: ", data['data']['active'], "Recovered: ", data['data']['recovered'], "Deaths: ", data['data']['deaths'], "Updated: ", data['dt']))

    elif (response.status_code == 404):
        print("Result not found!")
        
def report_printer():
    global report_covid
    with open("report_covid_country.txt", "r") as pros:
        report_covid = pros.read()
    return report_covid
