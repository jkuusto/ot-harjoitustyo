import os

dirname = os.path.dirname(__file__)

DATABASE_PATH = os.path.join(dirname, "..", "data", "counterpicker.db")

data_dir = os.path.join(dirname, "..", "data")
os.makedirs(data_dir, exist_ok=True)
