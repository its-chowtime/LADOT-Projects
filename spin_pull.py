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
        num = (900-9.6666666)    # Sleep for 15 minutes
        try:
            num = float(num)
        except ValueError:
            print('Enter in a number.\n')
            continue
        
        # Pulls from api
        print('%s' % time.ctime())
        _spin = requests.get('https://web.spin.pm/api/gbfs/v1/los_angeles/free_bike_status.json').json()

        # Store all data to df
        spin_df = pd.DataFrame(_spin['data']['bikes'])

        # Create new column
        spin_df['time'] = _spin['last_updated']

        # Save to csv
        spin_df.to_csv('spin_data.csv',mode='a',header=False)

        # Pull count
        spin_count= str(len(_spin['data']['bikes']))

        # Pull time
        spin_time= str(_spin['last_updated'])

        # Concatenate into a row to write to the output csv file
        spin = spin_count + "," + spin_time

        # Append to time_count.csv
        with open('spin.csv',mode='a') as outfile: 
            outfile.write(spin)
            outfile.write("\n")

        print('%s' % time.ctime())

        time.sleep(num)

try:
    sleeper()
except KeyboardInterrupt:
    print('\n\nKeyboard exception received. Exiting.')
    exit()

