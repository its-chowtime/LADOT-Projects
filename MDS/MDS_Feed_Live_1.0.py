import requests
import pandas as pd
import json
import time


def sleeper():
    while True:
        num = 17999.5
        try:
            num = float(num)
        except ValueError:
            print('Enter in a number.\n')
            continue
        
        print('%s' % time.ctime())
        
        # Pull data from API
        mds_data = requests.get('https://mds.bird.co/gbfs/los-angeles/free_bikes').json()
        avail_count= str(len(mds_data['data']['bikes']))
        avail_time= str(mds_data['last_updated'])

        # Concatenate into a row to write to the output csv file
        line_something = avail_count + "," + avail_time
        # Append to time_count.csv
        with open('time_count.csv',mode='a') as outfile: 
            outfile.write(line_something)
            outfile.write("\n")
        

        # Store to a different file
        mds_data = requests.get('https://mds.bird.co/gbfs/los-angeles/free_bikes').json()
        mds_df = pd.DataFrame(mds_data['data']['bikes'])
        mds_df['time'] = mds_data['last_updated']
        # foo_df = mds_df[['bike_id','lat','lon']]
        mds_df.to_csv('data.csv',mode='a',header=False)

        time.sleep(num)

try:
    sleeper()
except KeyboardInterrupt:
    print('\n\nKeyboard exception received. Exiting.')
    exit()



