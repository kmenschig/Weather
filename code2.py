# Import of core packages
import os
import sys
import logging

# Import of third party modules
import requests
from dateutil import parser

# Import of custom modules
from config import API_KEY
from app.config import stations
from app.Station import Station
from app import Utilities as util

# =========================================================
# DEFINITION OF GLOBALS  ==================================
# =========================================================

# Getting API_KEY
if not API_KEY:
  print("No environment variable 'API_KEY' set. Please create one. Exiting..")
  sys.exit(0)
else:
  print("Found API_KEY environment variable: '{0}'.".format(API_KEY))

# Checking if data directory exists
util.check_directory("data/data2")