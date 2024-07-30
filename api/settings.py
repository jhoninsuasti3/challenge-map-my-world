"""
Settings of project
"""
from os import getenv as env
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

DB_NAME = str(env("DB_NAME", default=""))
DB_USER = str(env("DB_USER", default=""))
DB_PASS = str(env("DB_PASS", default=""))
DB_PORT = str(env("DB_PORT", default="5432"))
DB_HOST = str(env("DB_HOST", default="localhost"))
DB_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
print(DB_URL)