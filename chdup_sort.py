import os
import pandas as pd
import numpy as np
import json
import requests
import time

reqApi = requests.get("https://web.spin.pm/api/gbfs/v1/los_angeles/free_bike_status.json").json()
apiDf = pd.DataFrame(reqApi['data']['bikes'])
apiDf.sort_values('bike_id', inplace=True)
apiDf.round(decimals=7)
apiDf.columns # List the column head

newDf = apiDf[['bike_id','lat','lon','vehicle_type']]
newDf.tail() # Selected columns in a new df

# Look for duplicates
dupDf = newDf[newDf.duplicated(['bike_id'])]
dupDf

# Count unique id and sum up unique id
s = newDf['bike_id'].value_counts()
s.tail() # Series

uniqueDf = pd.DataFrame(s)
uniqueDf.rename(columns={'bike_id':'counts'},inplace=True)
uniqueDf.tail() # List (same as series)
uniqueDf.sum(axis=0) # Sum up counts