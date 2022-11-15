import requests
import json
import datetime
import csv


for i in range(0,180):
    today = datetime.date.today()
    endDate = today - datetime.timedelta(days=i*30)
    startDate = today - datetime.timedelta(days=(i+1)*30)
    urlString = "https://api.weatherstack.com/historical?access_key={INSERT_API_KEY}&query=Istanbul&historical_date_start="+str(startDate)+"&historical_date_end="+str(endDate)
    r = requests.get(url=urlString, headers="", params="").json()
    try:
        with open('weathergetter.json', 'r') as fin:
            data = json.load(fin)
    except FileNotFoundError as exc:
        pass

    try:
        if data:
            temp = r["historical"]
            for filename, file_data in temp.items():
                date = file_data["date"]
                mintemp = file_data["mintemp"]
                totalsnow = file_data["totalsnow"]
                data.append([date,mintemp,totalsnow])           
            header = ['date', 'mintemp', 'totalsnow']
            with open('weathergetter.csv', 'w', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(header)
                writer.writerows(data)
            with open('weathergetter.json', 'w') as fout:
                json.dump(data, fout)
    except UnboundLocalError as exc:
        with open('weathergetter.json', 'w') as fout:
            json.dump(data, fout)

