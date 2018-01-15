import os
import sys

# Tries to load API_KEY from environment variable. 
# If it fails, for any reason, API_KEY is set to False
try:
    API_KEY = os.environ['WUNDERGROUND_KEY']
except:
    API_KEY = False

os.chdir(os.path.dirname(os.path.abspath(__file__)))
cwd=os.getcwd()
