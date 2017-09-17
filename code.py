import requests

#BASE_URL = 'http://api.wunderground.com/api/403665e38bc0904f/geolookup/conditions/forecast/q/Germany/Cologne.json'
BASE_URL = 'http://api.wunderground.com/api/f9d3ddb9a811ec37/geolookup/conditions/forecast/q/Germany/Cologne.json'

r = requests.get(BASE_URL)

print r.status_code

if r.status_code == 200:
    data = r.json()
    print data # THE WHOLE RESPONSE
    # print data["current_observation"]
    # print "City is: " + data["current_observation"]["observation_location"]["city"]
    # print "Dewpoint (f) is: " + str(data["current_observation"]["dewpoint_f"])

    dewF = str(data["current_observation"]["dewpoint_f"])
    dewC = str(data["current_observation"]["dewpoint_c"])
    relH = str(data["current_observation"]["relative_humidity"])
    prsI = data["current_observation"]["pressure_in"]
    tmpF = str(data["current_observation"]["temp_f"])
    tmpC = str(data["current_observation"]["temp_c"])
    obsL = data["current_observation"]["observation_location"]["city"]
    lt = data["current_observation"]["local_time_rfc822"]
#    dspL = data["current_observation"]["display_location"]
    

    # Let's optimize this routine

    with open('log.txt', 'a') as infile:
        infile.write(obsL + "   " + lt + "   " + dewF + "   " + dewC + "   " + relH + "   " + prsI + "   " + tmpF)
        infile.write("   " + tmpC)
        infile.write('\n')
else:
    print "No response returned"


# 1.) use terminal to `cd` into project dir
# 2.) run `source env/bin/activate` to activate virtual environment
# 3.) an `(env)` should appear in CLI on left side
# 4.) run `pip install <package name>` if you want additional packages
# 5.) `atom .` will open current directory in atom
# 6.) modify and run code
# 7.) `deactivate` will exit virtual environment
