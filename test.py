#!/home/klaus/Documents/Projects/Weather/env/bin/ python
import os
import subprocess

#subprocess.call(['tail -n 1 ~/Documents/Projects/Weather/data/gb_ISTALYBR4.txt'])
#subprocess.call('df', '-h')
#print f

#os.system("tail -n 1 " + cwd + "/data/" + station_country + "_" + station_id + ".txt > temporary_file")
os.system("tail -n 1 data/gb_ISTALYBR4.txt > temporary_file")
fh=open("temporary_file", "r")
i=1
for line in fh:
    print "i=",i, line
    i=i+1

#ll=fh.readlines()
        #close file
fh.close
os.system("rm -f temporary_file")
#print ll

#print txt
