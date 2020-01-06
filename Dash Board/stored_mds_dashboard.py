import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

''' # Live API
url = 'https://la-gbfs.getwheelsapp.com/free_bike_status.json'
data = pd.read_json(url)
df = pd.DataFrame(data['data']['bikes'])
'''
data = 'mds_collection.csv'
df = pd.read_csv(data)
df['date'] = pd.to_datetime(df['time'],unit='s')
print(df.head())


colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    
    dcc.Graph(
        id='birdla',
        figure={
            'data': [
                {'x': df[df['provider']=='birdla']['date'], 'y': df[df['provider']=='birdla']['count'], 'type': 'line', 'name': 'birdla'},
                {'x': df[df['provider']=='spin']['date'], 'y': df[df['provider']=='spin']['count'], 'type': 'line', 'name': 'birdla'},
                {'x': df[df['provider']=='wheels']['date'], 'y': df[df['provider']=='wheels']['count'], 'type': 'line', 'name': 'birdla'},
                {'x': df[df['provider']=='birdsm']['date'], 'y': df[df['provider']=='birdsm']['count'], 'type': 'line', 'name': 'birdla'},
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
