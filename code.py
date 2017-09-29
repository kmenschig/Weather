#!/home/klaus/Documents/Projects/Cologne-Weather/env/bin/ python
import requests
import os
# from mapping import vapor_pressure as vp

BASE_URL = 'http://api.wunderground.com/api/403665e38bc0904f/geolookup/conditions/forecast/q/Germany/Cologne.json'

r = requests.get(BASE_URL)


def writeToLog(row):
    """ 
    Writes a single row into the specified log file
    @param row {list} - the row to be written
    """
    cwd = os.getcwd()
    with open(cwd + "/log.txt", "a") as outfile:
        outfile.write('\t'.join(row) + '\n')


if r.status_code == 200:
    data = r.json()
    response = data["current_observation"]

    # Variable declaration
    dewF = str(response["dewpoint_f"])
    dewC = str(response["dewpoint_c"])
    relH = str(response["relative_humidity"])
    prsI = str(response["pressure_in"])
    tmpF = str(response["temp_f"])
    tmpC = str(response["temp_c"])
    obsL = str(response["display_location"]["city"])
    lt = str(response["local_time_rfc822"])

    # Calculation of vapor pressure at given temperature
    # @mmenschig - I don't know what you're doing here, maybe create a dictionary?
    a0 = 6.107799961
    a1 = 4.436518521E-01
    a2 = 1.428945805E-02
    a3 = 2.650648471E-04
    a4 = 3.031240396E-06
    a5 = 2.034080948E-08
    a6 = 6.136820929E-11


    tmp = ((float(tmpF) - 32) * 5 / 9)

    vapprs = str(round(a0 + tmp * (a1 + tmp * (a2 + tmp * (a3 + tmp * (a4 + tmp * (a5 + tmp * a6))))),3))
    vapprs='{:6}'.format(vapprs)

    tmp = ((float(dewF) - 32) * 5 / 9)

    vapdwp = str(round(a0 + tmp * (a1 + tmp * (a2 + tmp * (a3 + tmp * (a4 + tmp * (a5 + tmp * a6))))),3))
    vapdwp='{:6}'.format(vapdwp)


    relH='{:>4}'.format(relH)
    
    row = [obsL, lt, dewF, dewC, relH, prsI, tmpF, tmpC, vapprs, vapdwp]

    writeToLog(row)

else:
    print "No response returned"


