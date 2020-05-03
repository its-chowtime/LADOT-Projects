import os
import pandas as pd
import numpy as np
import csv
import json

# change directory
desiredpath = '/home/pi/data/MDS'
os.chdir(desiredpath)
print(desiredpath)


jumpb = pd.read_csv('jumpb.csv',sep=',',names=['count','time'])
jumpb_data = pd.read_csv('jumpb_data.csv',sep=',',names=['bikeid','is_reserved','is_disabled','lat','lon','time'])
jumps = pd.read_csv('jumps.csv',sep=',',names=['count','time'])
jumps_data = pd.read_csv('jumps_data.csv',sep=',',names=['bikeid','is_reserved','is_disabled','lat','lon','time'])
lyft = pd.read_csv('lyft.csv',sep=',',names=['count','time'])
lyft_data = pd.read_csv('lyft_data.csv',sep=',',names=['bikeid','is_reserved','is_disabled','lat','lon','type','time'])
spin = pd.read_csv('spin.csv',sep=',',names=['count','time'])
spin_data = pd.read_csv('spin_data.csv',sep=',',names=['bikeid','is_reserved','is_disabled','lat','lon','type','time'])
wheels = pd.read_csv('wheels.csv',sep=',',names=['count','time'])
wheels_data = pd.read_csv('wheels_data.csv',sep=',',names=['bikeid','is_reserved','is_disabled','lat','lon','vehicleid','time'])


list0 = ['jumpb.csv','jumpb_data.csv','jumps.csv','jumps_data.csv','lyft.csv','lyft_data.csv','spin.csv','spin_data.csv','wheels.csv','wheels_data.csv']
list01 = ['jumpb','jumps','lyft','spin','wheels']
list02 = ['jumpb_data','jumps_data','lyft_data','spin_data','wheels_data']
list1 = [jumpb,jumps,lyft,spin,wheels]
list2 = [jumpb_data,jumps_data,lyft_data,spin_data,wheels_data]


# Create new files with header
col_head0 = ['count','unixtime','company'] # How to create headers ?????????
col_head1 = ['bikeid','lat','lon','unixtime','company']
df = pd.DataFrame(columns=col_head0)
df2 = pd.DataFrame(columns=col_head1)
df.to_csv('ct_15_int.csv')
df2.to_csv('test.csv')


# Saves counts and time into one file
for x in range(len(list1)):
    list1[x]['company'] = list01[x] # Create a column to store company name
    list1[x].to_csv('ct_15_int.csv',mode='a',header=False)
df = pd.read_csv('ct_15_int.csv')


'''
# Saves mds data into one file
# FIXED CODE BELOW
for df in range(len(list2)):
    print(list2[df].head())
    new_df = pd.DataFrame(columns=['bikeid','lat','lon','time'])
    new_df = list2[df][['bikeid','lat','lon','time',]]
    new_df['company'] = list01[df]
    new_df.append(list2[df])
    print(new_df)
    new_df.to_csv('mds_data_24hrs.csv')
'''

for y in range(len(list2)):
    list2[y]['company'] = list01[y]
    new_df = pd.DataFrame(columns=['bikeid','lat','lon','time','company'])
    new_df = list2[y][['bikeid','lat','lon','time','company']]
    new_df.to_csv('test.csv',mode='a',header=False)
