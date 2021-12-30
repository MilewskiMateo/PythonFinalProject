import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import plotly.graph_objects as go
import plotly.express as px
from plotly.colors import n_colors


app = dash.Dash(__name__)
app.layout = html.Div([
    html.H2("Hello Dash!!!"),
    dcc.Dropdown(
        style={
            "width": "50%",
            "height": "30px",
            "lineHeight": "30px",
            "textAlign": "left",
            "margin": "10px",
        },
        id='Patient_Id',
        value='Janek',
        options=[
            {'label': 'Janek', 'value': 'Janek'},
            {'label': 'Elżbieta', 'value': 'Elżbieta'},
            {'label': 'Albert', 'value': 'Albert'},
            {'label': 'Ewelina', 'value': 'Ewelina'},
            {'label': 'Piotr', 'value': 'Piotr'},
            {'label': 'Bartosz', 'value': 'Bartosz'},
        ],
    ),

])

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0")
