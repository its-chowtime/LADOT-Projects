import requests
import json
import pandas as pd


wheels_api = requests.get('https://la-gbfs.getwheelsapp.com/free_bike_status.json')
wheels_data = wheels_api.json()
wheels_df = pd.DataFrame(wheels_data['data']['bikes'])

print(wheels_df)

export_csv = wheels_df.to_csv(r'C:\Users\406822\Desktop\LADOT_projects\API Practice\MDS API\df1.csv', index= None, header=True)