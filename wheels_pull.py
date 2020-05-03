import os
import requests
import pandas as pd
import json
import time
import numpy as np

# change directory
desiredpath = '/home/pi/data/MDS'
os.chdir(desiredpath)
print("path" + desiredpath)

print("How long to wait?")
wait = int(input()) * 60
print(str(wait))

time.sleep(wait/2)
print(str(wait/2))
time.sleep(wait/2)

def sleeper():
    while True:
        num = (900-11.33)    # Sleep for 15 minutes
        try:
            num = float(num)
        except ValueError:
            print('Enter in a number.\n')
            continue
        
        # Pulls from api
        print('%s' % time.ctime())
        _wheels = requests.get('https://la-gbfs.getwheelsapp.com/free_bike_status.json').json()

        # Store all data to df
        wheels_df = pd.DataFrame(_wheels['data']['bikes'])

        # Create new column
        wheels_df['time'] = _wheels['last_updated']

        # Save to csv
        wheels_df.to_csv('wheels_data.csv',mode='a',header=False)

        # Pull count
        wheels_count= str(len(_wheels['data']['bikes']))

        # Pull time
        wheels_time= str(_wheels['last_updated'])

        # Concatenate into a row to write to the output csv file
        wheels = wheels_count + "," + wheels_time

        # Append to time_count.csv
        with open('wheels.csv',mode='a') as outfile: 
            outfile.write(wheels)
            outfile.write("\n")

        print('%s' % time.ctime())

        time.sleep(num)

try:
    sleeper()
except KeyboardInterrupt:
    print('\n\nKeyboard exception received. Exiting.')
    exit()

