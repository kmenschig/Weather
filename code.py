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

def is_valid_data(relH):
    """
    Checks if data returned from API is valid by doing
    a very naive check to see if dewpoint temperature
    is not equal to -9999.
    @param {relH} the response object from Wunderground
    """
    return not relH == "-999%"


# Do this once, at start
check_data_directory()

for i in range(0, len(config.stations)):
    station_id = config.stations[i]["station_id"]
    station_country = config.stations[i]["country_short"]

    BASE_URL='https://api.wunderground.com/api/{0}/conditions/q/{1}/pws:{2}.json' \
        .format(config.API_KEY, station_country, station_id)

#    print "GET Request: " + BASE_URL

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

        print obsL, obsL.find(' ')

        #make obsL a string without a blank character
        if obsL.find(' ')!=-1:
            obsL=obsL.replace(' ','_')

        #Checking if metrics are valid
        if not is_valid_data(relH):
            continue


        #block to check whether the weather station has not updated it's information since last Request
        #new observation_time_rfc822 will be compared with the time in the last line of the respective file
        #if times are the same, the program will move to the next weather station

        os.system("tail -n 1 " + cwd + "/data/" + station_country + "_" + station_id + ".txt > temporary_file.txt")

        file_handle=open("temporary_file.txt", "r")

        for last_line in file_handle:
            date_time=last_line[3+len(obsL)+1:3+len(obsL)+1+len(lt)]

        file_handle.close

        os.system("rm -f temporary_file.txt")

        file_time=datetime.datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')
        station_time=datetime.datetime.strptime(lt, '%Y-%m-%d %H:%M:%S')

        #if file is empty and there is no date_time entry this command will not be executed
        #and program will move to next weather station
        if len(date_time)>0 and station_time<=file_time:
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


        #calculation of grams water in 1 cu.m of air
        #according to ideal gas law: pV=nRT

        #calculation of total moles in 1 cu.m at the reported conditions
        ntotal=float(prsI)*3386.3752577878*1/8.314/(273.15+float(tmpC))
        xH2O=float(vapdwp)*100/(float(prsI)*3386.3752577878)
        #number of moles of water in 1 cu.m air
        nH2O=xH2O*ntotal
        #mass of water in grams in 1 cu.m air
        mH2O=nH2O*18
        mH2O="{:2.2f}".format(mH2O)
        mH2O=str(mH2O)

        #calculation of the respective air density`
        rho=((float(prsI)*3386.3752577878-float(vapdwp)*100)*0.028964+float(vapdwp)*100*0.018016)/8.314/(273.15+float(tmpC))
        rho="{:1.3f}".format(rho)
        rho=str(rho)

        row = [station_country, obsL, lt, dewF, dewC, relH, prsI, tmpF, tmpC, vapprs, vapdwp, mH2O, rho]
        writeToLog(row)

    else:
        print "No response returned"
