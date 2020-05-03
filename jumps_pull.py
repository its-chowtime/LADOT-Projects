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
        _jumps = requests.get('https://gbfs.uber.com/v1/laxs/free_bike_status.json').json()

        # Store all data to df
        jumps_df = pd.DataFrame(_jumps['data']['bikes'])

        # Create new column
        jumps_df['time'] = _jumps['last_updated']

        # Save to csv
        jumps_df.to_csv('jumps_data.csv',mode='a',header=False)

        # Pull count
        jumps_count= str(len(_jumps['data']['bikes']))

        # Pull time
        jumps_time= str(_jumps['last_updated'])

        # Concatenate into a row to write to the output csv file
        jumps = jumps_count + "," + jumps_time

        # Append to time_count.csv
        with open('jumps.csv',mode='a') as outfile: 
            outfile.write(jumps)
            outfile.write("\n")

        print('%s' % time.ctime())

        time.sleep(num)

try:
    sleeper()
except KeyboardInterrupt:
    print('\n\nKeyboard exception received. Exiting.')
    exit()

