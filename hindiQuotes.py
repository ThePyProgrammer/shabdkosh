import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta

sdate = date(2009, 10, 1)   # start date
edate = date.today()        # end date

delta = edate - sdate       # as timedelta
print(delta)

#with open("hindiQuotes.txt", "w+") as file:
for i in range(delta.days + 1):
    date = sdate + timedelta(days=i)
    day = date.day
    month = date.month
    year = date.year
    page = requests.get(f"https://www.shabdkosh.com/quote-of-the-day/english-hindi/{year}/{month}/{day}")
    soup = BeautifulSoup(page.content, "html.parser")

    tag = "blockquote"
    arr = [text.get_text().replace("&dash", "–") for text in soup.find_all(tag)][:2]
    print(date, arr[0], arr[1], sep="\n", end="\n\n")
