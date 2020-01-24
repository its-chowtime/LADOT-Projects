import requests
import json
import numpy as np
import pandas as pd
import os

print(os.getcwd())
os.chdir('C:/Users/Pat/Desktop/test')


apiList = {'wheels':'https://la-gbfs.getwheelsapp.com/free_bike_status.json',
        'lime':'https://lime.bike/api/partners/v1/gbfs/los_angeles/free_bike_status.json',
        'birdla':'https://mds.bird.co/gbfs/los-angeles/free_bikes',
        'birdsm':'https://mds.bird.co/gbfs/santamonica/free_bikes',
        'spin':'https://web.spin.pm/api/gbfs/v1/los_angeles/free_bike_status.json'}
providerList = ['wheels','lime','birdla','birdsm','spin']

def ProviderPick():
        print(providerList)
        print("\nChoose a provider: ")
        arg = input()
        # print(apiList[arg])
        try:
                Store_Df(arg)    
        except KeyboardInterrupt:
                print('\n\nKeyboard exception received. Exiting.')
                exit()  


def Store_Df(arg):
        try:
                tempvar = requests.get(apiList[arg]).json()
                tempvar = requests.get(apiList[arg]).json()
                temp_df = pd.DataFrame(tempvar['data']['bikes'])
                temp_df['time'] = tempvar['last_updated']
                print(temp_df)
                Save_To(arg)
                
        except:
                print("Error")
                ProviderPick()


def Save_To(arg):
        print("\n Would you like to store the data? y/n")
        temp_in = input()
        if temp_in == 'y':
                print('\nWhat data would you like to save?\nall | count | both\n')
                temp_in2 = input()
                if temp_in2 == 'all':
                        tempvar = requests.get(apiList[arg]).json()
                        temp_df = pd.DataFrame(tempvar['data']['bikes'])
                        temp_df['time'] = tempvar['last_updated']
                        temp_df.to_csv(arg + '_data.csv',mode='a',header=False)
                        
                elif temp_in2 == 'count':
                        tempvar = requests.get(apiList[arg]).json()
                        temp_count = str(len(tempvar['data']['bikes']))
                        temp_time = str(tempvar['data']['bikes']) 
                        count_time = temp_count+','+temp_time      
                        with open(arg+'_count.csv', mode='a') as outfile:
                                outfile.write(count_time)
                                outfile.write("\n")   

                elif temp_in2 == 'both':
                        tempvar = requests.get(apiList[arg]).json()
                        temp_df = pd.DataFrame(tempvar['data']['bikes'])
                        temp_df['time'] = tempvar['last_updated']
                        temp_df.to_csv(arg + '_data.csv',mode='a',header=False)
                        temp_count = str(len(tempvar['data']['bikes']))
                        temp_time = str(tempvar['data']['bikes']) 
                        count_time = temp_count+','+temp_time      
                        with open(arg+'_count.csv', mode='a') as outfile:
                                outfile.write(count_time)
                                outfile.write("\n")         
                else:
                        print('\n Not saving data') 
                        pass
        else:
                print('\n Not saving data') 

try:
        ProviderPick()    
except KeyboardInterrupt:
    print('\n\nKeyboard exception received. Exiting.')
    exit()    
