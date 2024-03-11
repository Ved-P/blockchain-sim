import dash
from dash import html
from blockchain import Blockchain

app = dash.Dash(__name__)

app.layout = html.P("Hello, World!")

if __name__ == '__main__':
    app.run_server(port = 8000, debug = True, use_reloader = False)