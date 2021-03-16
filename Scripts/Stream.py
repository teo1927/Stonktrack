import pandas as pd
import requests
import json
import praw
import csv
from datetime import datetime, timedelta
import enchant

def streamdata(filelocation):
    # Stream/Reddit API credentials for Praw
    reddit = praw.Reddit(client_id="EY365y7Sub32ig", client_secret="eWztV3U0TgzJ1AkD8beJv8Z47i87kA",
                         username="StonkTrend", password='Erli6965913', user_agent="testscript by u/StonkTrend")
    subreddit = reddit.subreddit('wallstreetbets')
    count = 0
    subreddit.hot(limit=1)
    for comment in subreddit.stream.comments(skip_existing=True):
        try:
            print(comment.body)
            comment.body = comment.body.replace('\n', ' ').replace('\r', '').replace(',', '').replace('.',' ').replace(')','').replace('(','')
            count = count + 1
            print(count)
            with open(filelocation, mode='a', encoding='utf-8-sig') as streamdata:
                stream_export = csv.writer(streamdata, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                stream_export.writerow([comment.body, datetime.now()])
        except praw.exceptions.PRAWException as e:
            pass

streamlocation = "/home/Tickerdigest/Stream/stream.csv"

streamdata(streamlocation)
