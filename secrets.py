import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
DB_NAME = os.getenv("DB_NAME")
TABLE_NAME = os.getenv("TABLE_NAME")
ROOT_URL = os.getenv("ROOT_URL")
PATH = os.getenv("URL_PATH")
PROJ_DIR = os.environ["PROJ_DIR"]
