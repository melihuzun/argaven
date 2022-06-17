import requests
from bs4 import BeautifulSoup as bs
from datetime import date
import sqlite3
from db import insert_data
from secrets import ROOT_URL, PATH, PROJ_DIR

root_url = ROOT_URL
path = PATH
con = sqlite3.connect("pgm.db")
cur = con.cursor()

news_dict = {}

with open(f"{PROJ_DIR}/keywords.txt", "r", encoding="utf-8") as f:
    keywords = f.read().splitlines()

keywords += list(map(lambda x: x.lower(), keywords))

today = date.today().strftime("%e.%m.%Y").replace(" ", "")

r = requests.get(ROOT_URL + PATH, verify=False)
r = bs(r.text, "html.parser")

last_item = r.table.tbody.find_all(
    lambda tag: tag.name == "tr" and today in tag.text
)


def search_keywords(keywords, text):
    for i in keywords:
        if i in text:
            return True

    return False


for i in last_item:
    if search_keywords(keywords, i.text):
        url = i.a["href"]
        title = i.a.text
        date = i.select("tr > td")[1].get_text(strip=True)
        if "http" not in url:
            url = root_url + url
        insert_data(title, url, date)
con.close()
