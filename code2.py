# Import of core packages
import os
import sys
import logging

# Import of third party modules
import requests

# Import of custom modules
from config import API_KEY
from app.config import stations
from app.config.vapor_pressure import vapor_pressure as vp

# =========================================================
# DEFINITION OF GLOBALS  ==================================
# =========================================================

# Setting API_KEY
if not API_KEY:
  print("No environment variable 'API_KEY' set. Please create one. Exiting..")
  sys.exit(0)
else:
  print("Using '{0}' as API_KEY for Wunderground Requests.".format(API_KEY))

# Setting current working directory


# =========================================================
# DEFINITION OF FUNCTIONS =================================
# =========================================================

