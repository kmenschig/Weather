#!/home/klaus/Documents/Projects/Cologne-Weather/env/bin/ python
import os
import datetime
import requests
import argparse
import config
from config import cwd
from dateutil import parser


def writeToLog(row, station_id):
    """
    Writes a single row into the specified log file
    @param row {list} - the row to be written
    @param station_id {string} - the private weather station id
    """

    # TODO: check if /data exists, create if not

    with open(cwd + "/data/" + station_id + ".txt", "a") as outfile:
        outfile.write('\t'.join(row) + '\n')

def date_to_ISO(date):
    """ 
    Returns an ISO datetime object from an 
    RFC822 formatted datetime string. Returned 
    object has no UTC offset information.
    @param {string} the rfc822 string 
    """
    return parser.parse(date).replace(tzinfo=None)


for i in range(0, len(config.stations)):
    station_id = config.stations[i]["station_id"]
    station_country = config.stations[i]["country_short"]

    BASE_URL='https://api.wunderground.com/api/{0}/conditions/q/{1}/pws:{2}.json' \
        .format(config.API_KEY, station_country, station_id)

    print "GET Request: " + BASE_URL

    r = requests.get(BASE_URL)

    if r.status_code == 200:
        data = r.json()
        response = data["current_observation"]


        # Variable declaration
        dewF = str("{0:.1f}".format(response["dewpoint_f"]))
        dewC = str("{0:.1f}".format(response["dewpoint_c"]))
        relH = str(response["relative_humidity"])
        prsI = str(response["pressure_in"])
        tmpF = str("{0:.1f}".format(response["temp_f"]))
        tmpC = str("{0:.1f}".format(response["temp_c"]))
        obsL = str(response["display_location"]["city"])
        lt = str(date_to_ISO(response["observation_time_rfc822"]))


        # Calculation of vapor pressure at given temperature
        a0 = 6.107799961
        a1 = 4.436518521E-01
        a2 = 1.428945805E-02
        a3 = 2.650648471E-04
        a4 = 3.031240396E-06
        a5 = 2.034080948E-08
        a6 = 6.136820929E-11

        # conversion of temp_f in temp_c for more digits
        tmp = ((float(tmpF) - 32) * 5 / 9)

        # calculations of vapor pressure dependent on temperature
        vapprs = str(round(a0 + tmp * (a1 + tmp * (a2 + tmp * (a3 + tmp * (a4 + tmp * (a5 + tmp * a6))))),3))
        # vapprs='{:6}'.format(vapprs)

        # conversion of dewF in dewC for more digits
        tmp = ((float(dewF) - 32) * 5 / 9)

        # calculations of vapor pressure dependent on temperature of dew point
        vapdwp = str(round(a0 + tmp * (a1 + tmp * (a2 + tmp * (a3 + tmp * (a4 + tmp * (a5 + tmp * a6))))),3))
        # vapdwp='{:6}'.format(vapdwp)


        # relH='{:>4}'.format(relH)

        row = [obsL, lt, dewF, dewC, relH, prsI, tmpF, tmpC, vapprs, vapdwp]
        writeToLog(row, station_id)

    else:
        print "No response returned"
