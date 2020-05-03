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
        _lyft = requests.get('https://s3.amazonaws.com/lyft-lastmile-production-iad/lbs/lax/free_bike_status.json').json()

        # Store all data to df
        lyft_df = pd.DataFrame(_lyft['data']['bikes'])

        # Create new column
        lyft_df['time'] = _lyft['last_updated']

        # Save to csv
        lyft_df.to_csv('lyft_data.csv',mode='a',header=False)

        # Pull count
        lyft_count= str(len(_lyft['data']['bikes']))

        # Pull time
        lyft_time= str(_lyft['last_updated'])

        # Concatenate into a row to write to the output csv file
        lyft = lyft_count + "," + lyft_time

        # Append to time_count.csv
        with open('lyft.csv',mode='a') as outfile: 
            outfile.write(lyft)
            outfile.write("\n")

        print('%s' % time.ctime())

        time.sleep(num)

try:
    sleeper()
except KeyboardInterrupt:
    print('\n\nKeyboard exception received. Exiting.')
    exit()

