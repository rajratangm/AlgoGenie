import os

MODEL= 'gpt-4o'
TEXT_MENTION= 'STOP'
TIMEOUT=120
# Remove this line from constant.py and add it to AlgoGenie.py (one directory up)
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

WORK_DIR = os.path.join(os.path.dirname(__file__), 'temp')
# Create a 'data' folder in the project root
WORK_DIR = os.path.join(ROOT_DIR, "data")

# Make sure the folder exists
os.makedirs(WORK_DIR, exist_ok=True)
MAX_TURNS=10
