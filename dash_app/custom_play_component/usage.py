import custom_play_component
import dash
from dash.dependencies import Input, Output
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div([
    custom_play_component.PlayComponent(
        id='input',
        value=True,
    ),
])





if __name__ == '__main__':
    app.run_server(debug=True)
