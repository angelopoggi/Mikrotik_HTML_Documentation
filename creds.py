import os
from dotenv import load_dotenv,find_dotenv
from pathlib import Path  # Python 3.6+ only
#Turns the text in .env into os operating system variables to be used and passed to other scripts
env_file = find_dotenv()
try:
    load_dotenv(env_file)
except:
    print("Please create a local .env file with local credentials")
    exit()
#Define the 3 variables
username=os.getenv("username")
password=os.getenv("password")

#ssh_key=os.getenv("ssh_keys")
#load_dotenv(ctly like os vars
#How to pull env info into this file
#Ties values in python vars
#Git ignore ptyc and env files before I commit
