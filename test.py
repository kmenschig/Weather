from datetime import datetime
from dateutil.parser import parse

def date_to_ISO(date):
    print date

    new_date = datetime.strptime(date, "%a, %d %b %Y %H:%M:%S  %z")
    print new_date


date_to_ISO("Sun, 15 Oct 2017 15:39:38 -0500")


"""
Articles to read
https://docs.python.org/2/library/datetime.html
https://docs.python.org/2/library/datetime.html#datetime.datetime.strptime
"""
