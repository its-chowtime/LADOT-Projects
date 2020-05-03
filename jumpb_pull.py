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
        _jumpb = requests.get('https://gbfs.uber.com/v1/laxb/free_bike_status.json').json()

        # Store all data to df
        jumpb_df = pd.DataFrame(_jumpb['data']['bikes'])

        # Create new column
        jumpb_df['time'] = _jumpb['last_updated']

        # Save to csv
        jumpb_df.to_csv('jumpb_data.csv',mode='a',header=False)

        # Pull count
        jumpb_count= str(len(_jumpb['data']['bikes']))

        # Pull time
        jumpb_time= str(_jumpb['last_updated'])

        # Concatenate into a row to write to the output csv file
        jumpb = jumpb_count + "," + jumpb_time

        # Append to time_count.csv
        with open('jumpb.csv',mode='a') as outfile: 
            outfile.write(jumpb)
            outfile.write("\n")

        print('%s' % time.ctime())

        time.sleep(num)

try:
    sleeper()
except KeyboardInterrupt:
    print('\n\nKeyboard exception received. Exiting.')
    exit()

