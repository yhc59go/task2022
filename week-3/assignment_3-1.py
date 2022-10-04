from unittest import result
import urllib.request as request
import json
import re
import csv
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src)as response:
    data=json.load(response)
    
with open("data.csv","w", newline="", encoding="utf-8") as csvFile:
    writer=csv.writer(csvFile)
    
    for idx in range(0,len(data["result"]["results"])):
        yearOfData=data["result"]["results"][idx]["xpostDate"].split("/")
        if int(yearOfData[0])>=2015:
            administrativeRegion=re.search(r'\s.*區' , data["result"]["results"][idx]["address"] ).group(0).strip()
            imageFile=re.split("jpg",data["result"]["results"][idx]["file"], flags=re.IGNORECASE)       
            writer.writerow(
                #景點名稱,區域,經度,緯度,第一張圖檔網址
                [data["result"]["results"][idx]["stitle"],
                administrativeRegion,
                data["result"]["results"][idx]["longitude"],
                data["result"]["results"][idx]["latitude"],
                imageFile[0]+"jpg"])
  



