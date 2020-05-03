import os
import requests
import pandas as pd
import json
import time
import numpy as np

# change directory
desiredpath = '/home/pi/data'
os.chdir(desiredpath)
print("path" + desiredpath)

provider = ''
provider = input('Type in provider name: ')
url = {'birdla':'https://mds.bird.co/gbfs/los-angeles/free_bikes',
        'birdsm':'https://mds.bird.co/gbfs/santamonica/free_bikes',
        'lime':'https://lime.bike/api/partners/v1/gbfs/los_angeles/free_bike_status.json',
        'spin':'https://web.spin.pm/api/gbfs/v1/los_angeles/free_bike_status.json',
        'wheels':'https://la-gbfs.getwheelsapp.com/free_bike_status.json'}

print("How long to wait?")
wait = int(input()) * 60
print(str(wait))

time.sleep(wait/2)
print(str(wait/2))
time.sleep(wait/2)

def sleeper():
    while True:
        num = (900-9.65)    # Sleep for 15 minutes
        try:
            num = float(num)
        except ValueError:
            print('Enter in a number.\n')
            continue
        
        # Pulls from api
        print('%s' % time.ctime())
        
        api = requests.get(url[provider]).json()


        # Store all data to df
        df = pd.DataFrame(api['data']['bikes'])


        # Create new column
        df['time'] = api['last_updated']

        # Save to csv
        csvdata = provider + '_loc_data.csv'
        df.to_csv(csvdata,mode='a',header=False)

        # Pull count
        dfcount= str(len(api['data']['bikes']))

        # Pull time
        dftime= str(api['last_updated'])
        

        # Concatenate into a row to write to the output csv file
        count_time = dfcount + "," + dftime
        
        # Append to time_count.csv
        csvct = provider + '_dt.csv'
        with open(csvct,mode='a') as outfile: 
            outfile.write(count_time)
            outfile.write("\n")

        print('%s' % time.ctime())

        time.sleep(num)


apis = url[provider]


try:
    print(requests.get(apis))
    sleeper()
except KeyboardInterrupt:
    print('\n\nKeyboard exception received. Exiting.')
    exit()

