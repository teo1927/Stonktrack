import pandas as pd
import requests
import json
import praw
import csv
from datetime import datetime, timedelta
import enchant

def csvsplit(streamfile,outputlocation,hoursago): #Split stream.csv into hour intervals based off time stamps with hours as the function argument
    with open(streamfile, mode='r', encoding='utf-8-sig') as file:
        reader = csv.reader(file, delimiter=',')
        open(outputlocation + str(hoursago) + 'hour.csv', 'w').close()
        for row in reader:
            strippedtime = datetime.strptime(row[1],"%Y-%m-%d %H:%M:%S.%f")
            #print(type(strippedtime))
            #print(strippedtime)
            ###Build in Backup for file before deleting by os copy###
            if datetime.now() - timedelta(hours=hoursago) <= strippedtime:
                #print("True")
                with open(outputlocation + str(hoursago) + 'hour.csv', mode='a', encoding='utf-8-sig') as agocsv:
                    export = csv.writer(agocsv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    export.writerow(row)

streamlocation = "/home/Tickerdigest/Stream/stream.csv"
outputdirectory = "/home/Tickerdigest/Comments/"

csvsplit(streamlocation,outputdirectory,1)
csvsplit(streamlocation,outputdirectory,4)
csvsplit(streamlocation,outputdirectory,8)
csvsplit(streamlocation,outputdirectory,12)
csvsplit(streamlocation,outputdirectory,24)
