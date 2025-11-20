import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "counterpicker.db"

DATABASE_PATH = os.path.join(dirname, "..", "data", DATABASE_FILENAME)

data_dir = os.path.join(dirname, "..", "data")
os.makedirs(data_dir, exist_ok=True)
