import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

# change directory
desiredpath = 'C:/Users/406822/Desktop/MDS_Data/'
os.chdir(desiredpath)
print(desiredpath)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

''' # Live API
url = 'https://la-gbfs.getwheelsapp.com/free_bike_status.json'
data = pd.read_json(url)
df = pd.DataFrame(data['data']['bikes'])
'''
# change unix time to readable time
data = 'clean_count.csv'
df = pd.read_csv(data)
# print(df.head())
#df['new_date'] = pd.to_datetime(df['unixtime'],unit='s') # Check time/date
# print(df.head())

app.layout = html.Div([
    dcc.Graph(
        id='bird',
        figure={
            'data': [
                {'x': df[df['company']=='birdla']['date'], 'y': df[df['company']=='birdla']['used'], 'type': 'line', 'name': 'birdla'},
                {'x': df[df['company']=='birdsm']['date'], 'y': df[df['company']=='birdsm']['used'], 'type': 'line', 'name': 'birdsm'},
            ],
            'layout': {
                'height': 400
            }
        }
    ),
    html.Hr(),
    dcc.Graph(
        id='spin',
        style={
            'height': 400
        },
        figure={
            'data': [
                {'x': df[df['company']=='spin']['date'], 'y': df[df['company']=='spin']['used'], 'type': 'line', 'name': 'spin'},
            ]
        }
    ),
    html.Hr(),
    dcc.Graph(
        id='wheels',
        style={
            'height': 400
        },
        figure={
            'data': [
                {'x': df[df['company']=='wheels']['date'], 'y': df[df['company']=='wheels']['used'], 'type': 'line', 'name': 'wheels'},

            ]
        }
    ),
    html.Hr(),
    dcc.Graph(
        id='lime',
        style={
            'height': 400
        },
        figure={
            'data': [
                {'x': df[df['company']=='lime']['date'], 'y': df[df['company']=='lime']['used'], 'type': 'line', 'name': 'lime'},

            ]
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
