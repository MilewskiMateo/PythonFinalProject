import custom_feet_component
import dash
from dash.dependencies import Input, Output
import dash_html_components as html

app = dash.Dash(__name__)

sensor_values_mock = [896, 568, 708, 23, 0, 5]

app.layout = html.Div([
    custom_feet_component.FeetComponent(
        id='input',
        sensorValues=sensor_values_mock
    ),
    html.Div(id='output')
])

if __name__ == '__main__':
    app.run_server(debug=True)
