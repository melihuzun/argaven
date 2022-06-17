import sqlite3
import traceback
import requests
from secrets import TABLE_NAME, DB_NAME, BOT_TOKEN, CHAT_ID


con = sqlite3.connect(f"{DB_NAME}.db")
cur = con.cursor()


def insert_data(title, url, date):
    cur.execute(
        f"""CREATE TABLE IF NOT EXISTS {TABLE_NAME}
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT, url TEXT type UNIQUE, date TEXT)"""
    )
    try:
        cur.execute(
            f"INSERT INTO {TABLE_NAME} (title, url,date) VALUES"
            f" ('{title}','{url}','{date}')"
        )
        con.commit()

        requests.get(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={url}"
        )
        print(title)
    except sqlite3.IntegrityError:
        pass

    except Exception:
        traceback.print_exc()
