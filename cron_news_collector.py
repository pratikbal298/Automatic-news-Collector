import schedule
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime


def collect_news():

    print("\nCollecting latest news...")

    url = "https://news.ycombinator.com"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    headlines = soup.select(".titleline a")

    news_data = []

    for item in headlines[:10]:

        title = item.text
        link = item.get("href")

        news_data.append({
            "Title": title,
            "Link": link,
            "Time": datetime.now()
        })

    df = pd.DataFrame(news_data)

    df.to_csv("news.csv", index=False)

    print("News collected and saved successfully!")


# Schedule task daily
schedule.every(10).seconds.do(collect_news).do(collect_news)

print("Cron job started... Waiting for scheduled time.")

# Keep program running
while True:

    schedule.run_pending()

    time.sleep(1)