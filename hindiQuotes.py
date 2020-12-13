import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta

sdate = date(2009, 10, 1)   # start date in format (year, month, day)
edate = date.today()        # end date

delta = edate - sdate       # as timedelta

lst = []

for i in range(delta.days + 1):
    date = sdate + timedelta(days=i)
    day = date.day
    month = date.month
    year = date.year
    page = requests.get(f"https://www.shabdkosh.com/quote-of-the-day/english-hindi/{year}/{month}/{day}")
    soup = BeautifulSoup(page.content, "html.parser")

    tag = "blockquote"
    arr = [text.get_text().replace("&dash", "–").replace("”", "” - ") for text in soup.find_all(tag)][:2]
    if arr[0] in lst: continue
    lst.append(arr[0])
    print(date, arr[0], arr[1], sep="\n", end="\n\n")
