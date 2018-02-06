import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from dateutil import parser

def excel_date(date1):
    temp = dt.datetime(1899, 12, 30)    # Note, not 31st Dec but 30th!
    delta = date1 - temp
    return float(delta.days) + (float(delta.seconds) / 86400)

fieldnames=['country','daytime','tmpF','tmpC','rH','P','dwpF','dwpC','vapprs','vapdwp','mH2O','rho']
#datafield = np.genfromtxt('mx_IESTADOD2.txt',names=fieldnames,dtype=np.str,delimiter='\t',unpack=True)
#x,y = np.genfromtxt('ph_ICALABAR26.txt',names=fieldnames,usecols=('daytime' ,'mH2O'),dtype=np.str,delimiter='\t',unpack=True)
#x,y = np.genfromtxt('ph_ICALABAR26.txt',usecols=(2 ,11),dtype=np.str,delimiter='\t',unpack=True)
x,y = np.genfromtxt('data/ph_ICALABAR26.txt',usecols=(2 ,11),dtype=np.str,delimiter='\t',unpack=True)
df=pd.DataFrame({'date0':pd.date_range('1990-01-01 00:00:00', periods=1),
                 'date1':pd.date_range('2000-01-01 00:00:00',periods=1, freq='24H')})
df['diff'] = df['date1'] - df['date0']
df['seconds'] = df['diff'].dt.total_seconds()
print (df)
#a=np.datetime64(x)
#print (a)
#x=pd.to_timedel
#x=parser.parse(x)
#print (y)
#print
#print (x)
# Compute the x and y coordinates for points on a sine curve
#x = np.arange(0, 3 * np.pi, 0.1)
#y = np.sin(x)
#testdate2 = datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
# Plot the points using matplotlib
ax = plt.axes()
#ax.set_yscale('linear')
#ax.set_ylim([20,30])
#major_yticks=np.arange(0,31,10)
#minor_yticks=np.arange(0,31,5)
ax.set_ylim([0,30])
#ax.yaxis.set_major_locator(plt.NullLocator())
#ax.xaxis.set_major_formatter(plt.NullFormatter())
#ax.xaxis.set_major_locator(plt.MaxNLocator(4))
#ax.yaxis.set_major_locator(plt.MaxNLocator(4))
#ticks = ax.set_yticks([0,5,10,15,20,25])
labels = ax.set_yticks([0,30,5])

plt.title('mH2O in Air in Mexico')
plt.xlabel('time')
plt.ylabel('mH2O [g/cu.m]')
#plt.autoscale(False)
#plt.ylim(0,30)

#plt.axis(['13:00:00','22:00:00',0,25])
#plt.plot(x, y, 'ro')
#plt.show()  # You must call plt.show() to make graphics appear.
