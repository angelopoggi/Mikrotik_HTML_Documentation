import os
from dotenv import load_dotenv,find_dotenv
from click import echo
from pathlib import Path  # Python 3.6+ only
env_file = find_dotenv('.env', usecwd=True)
try:
    load_dotenv(env_file)
except:
    echo("Please create a local .env file with local credentials")
    exit(1)

USERNAME = os.getenv('username')
PASSWORD = os.getenv("password")