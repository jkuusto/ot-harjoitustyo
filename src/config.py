import os
from pathlib import Path

dirname = os.path.dirname(__file__)

DATABASE_PATH = os.path.join(dirname, "..", "data", "counterpicker.db")

Path(os.path.join(dirname, "..", "data")).mkdir(parents=True, exist_ok=True)
