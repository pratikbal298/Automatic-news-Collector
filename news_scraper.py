import requests
from bs4 import BeautifulSoup
import pandas as pd

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
        "Link": link
    })

df = pd.DataFrame(news_data)

df.to_csv("news.csv", index=False)

print("News saved successfully!")