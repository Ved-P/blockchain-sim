import dash
from dash import html
from blockchain import Blockchain

app = dash.Dash(__name__)

app.layout = html.Div([

    html.Div("Blockchain", style = {
        'background-color': 'white',
        'border': '3px solid black',
        'border-radius': '8vh',
        'min-height': '30vh',
        'padding': '8vh',
        'font-size': '30px',
        'margin-bottom': '10vh'
    }),

    html.Div("Command Center", style = {
        'background-color': 'white',
        'border': '3px solid black',
        'border-radius': '8vh',
        'min-height': '10vh',
        'padding': '8vh',
        'font-size': '30px',
    })

], style = {
    'background-color': 'gainsboro',
    'padding': '8vh'
})

if __name__ == '__main__':
    app.run_server(port = 8000, debug = True, use_reloader = False)