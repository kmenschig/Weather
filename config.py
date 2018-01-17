import os

# Returns false if no API_KEY is set as environment variable
try:
    API_KEY = os.environ['WUNDERGROUND_KEY']
except:
    API_KEY = False

