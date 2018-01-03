#!/home/klaus/Documents/Projects/Weather/env/bin/ python
import os
import datetime
import requests
import argparse
import config
from config import cwd
from dateutil import parser


def writeToLog(row):
    """
    Writes a single row into the specified log file
    @param row {list} - the row to be written
    @param station_id {string} - the private weather station id
    """
    with open(cwd + "/data/" + station_country + "_" + station_id + ".txt", "a") as outfile:
        outfile.write('\t'.join(row) + '\n')

def date_to_ISO(date):
    """
    Returns an ISO datetime object from an
    RFC822 formatted datetime string. Returned
    object has no UTC offset information.
    @param {string} the rfc822 string
    """
    return parser.parse(date).replace(tzinfo=None)

def check_data_directory():
    """
    Checks if the 'data' directory exists
    which is used to store collected data in
    log files.
    No parameters
    """
    if not os.path.isdir(cwd + '/data'):

        print "Data directory does not exist. Creating one.."
        os.mkdir(cwd + '/data')
        print "Created directory!"

def is_valid_data(dewF):
    """
    Checks if data returned from API is valid by doing
    a very naive check to see if dewpoint temperature
    is not equal to -9999.
    @param {dewF} the response object from Wunderground
    """
    return not dewF == "-9999.0"


# Do this once, at start
check_data_directory()

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


        dewF = str(response["dewpoint_f"])
        dewC = str(response["dewpoint_c"])
        relH = str(response["relative_humidity"])
        prsI = str(response["pressure_in"])
        tmpF = str(response["temp_f"])
        tmpC = str(response["temp_c"])
        obsL = str(response["display_location"]["city"])
        lt = str(date_to_ISO(response["observation_time_rfc822"]))

#        print len(obsL), len(lt)

        #Checking if metrics are valid
        if not is_valid_data(dewF):
            continue

        #read lines of file
        fh=open(cwd + "/data/" + station_country + "_" + station_id + ".txt", "r")
        ll=fh.readlines()
        #close file
        fh.close

        #extract last line from ll
        lastll=ll[len(ll)-1]

        #extract date and time information from last line
        dattim=lastll[3+len(obsL)+1:3+len(obsL)+1+len(lt)]

        #skip if date and time of new download are the same as in the last line
        if lt==dattim:
            continue

        # Calculation of vapor pressure at given temperature in [mbar]
        a0 = 6.107799961
        a1 = 4.436518521E-01
        a2 = 1.428945805E-02
        a3 = 2.650648471E-04
        a4 = 3.031240396E-06
        a5 = 2.034080948E-08
        a6 = 6.136820929E-11

        # conversion of temp_f in temp_c for more digits
        tmp = ((float(tmpF) - 32) * 5 / 9)

        # calculations of vapor pressure in [mbar] dependent on temperature
        vapprs = str(round(a0 + tmp * (a1 + tmp * (a2 + tmp * (a3 + tmp * (a4 + tmp * (a5 + tmp * a6))))),3))
        # vapprs='{:6}'.format(vapprs)

        # conversion of dewF in dewC for more digits
        tmp = ((float(dewF) - 32) * 5 / 9)

        # calculations of vapor pressure in [mbar] dependent on temperature of dew point
        vapdwp = str(round(a0 + tmp * (a1 + tmp * (a2 + tmp * (a3 + tmp * (a4 + tmp * (a5 + tmp * a6))))),3))
        # vapdwp='{:6}'.format(vapdwp)

        # relH='{:>4}'.format(relH)

        row = [station_country, obsL, lt, dewF, dewC, relH, prsI, tmpF, tmpC, vapprs, vapdwp]
        writeToLog(row)

    else:
        print "No response returned"
