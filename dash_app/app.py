from __future__ import absolute_import
import redis
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import dash_daq as daq
import json
import custom_feet_component
import custom_people_component
import time
from enum import Enum
from datetime import datetime
app = dash.Dash(__name__)
redis_connection = redis.Redis(host="pythonfinalproject_redis_1")
sensor_values_mock = [896, 568, 708, 23, 0, 5]

while not all([redis_connection.lindex(f"patient_{id}", 0) for id in range(1,7)]):
    app.logger.info("Waiting for redis...")
    time.sleep(1)

names = [json.loads(redis_connection.lindex(f"patient_{id}", 0))['firstname'] for id in range(1,7)]

suffix_row = '_row'
suffix_button_id = '_button'
suffix_sparkline_graph = '_sparkline_graph'
suffix_count = '_count'
suffix_ooc_n = '_OOC_number'
suffix_ooc_g = '_OOC_graph'
suffix_indicator = '_indicator'


def build_top_panel():
    return html.Div(
        id='metric-summary-session',
        children=[
            generate_metric_list_header(),
            html.Div(
                id='metric_div',
                children=[
                    generate_metric_row_helper(0),
                    generate_metric_row_helper(1),
                    generate_metric_row_helper(2),
                    generate_metric_row_helper(3),
                    generate_metric_row_helper(4),
                    generate_metric_row_helper(5),
                ]
            )
        ]
    )


def generate_metric_list_header():
    return generate_metric_row(
        'metric_header',
        {
            'height': '30px',
            'margin': '10px 0px',
            'textAlign': 'center'
        },
        {
            'id': "m_header_1",
            'children': html.Div("Sensor")
        },
        {
            'id': "m_header_3",
            'children': html.Div("Wykres")
        },
        {
            'id': "m_header_5",
            'children': html.Div("Aktualny nacisk")
        },
        {
            'id': "m_header_6",
            'children': "Anomalia"
        })


params = [
    "left foot front",
    "left foot middle",
    "left foot back",
    "right foot front",
    "right foot middle",
    "right foot back"
]

def generate_metric_row_helper(index):
    item = params[index]

    div_id = item + suffix_row
    button_id = item + suffix_button_id
    sparkline_graph_id = item + suffix_sparkline_graph
    ooc_graph_id = item + suffix_ooc_g
    indicator_id = item + suffix_indicator

    return generate_metric_row(
        div_id, None,
        {
            'id': item,
            'children': html.Div(
                id=button_id,
                children=item,
            )
        },
        {
            'id': item + '_sparkline',
            'children': dcc.Graph(
                id=sparkline_graph_id,
                style={
                    'width': '100%',
                    'height': '60%',
                },
                config={
                    'displayModeBar': False
                },
                figure=go.Figure({
                    'data': [{'x': [1, 2, 3, 4, 5], 'y': [1, 2, 1, 15, 2],
                              'mode': 'lines+markers',
                              'line': {'color': 'rgb(255,209,95)'}}],
                    'layout': {
                        'margin': dict(
                            l=0, r=0, t=0, b=0, pad=0
                        ),
                        'paper_bgcolor': 'rgb(45, 48, 56)',
                        'plot_bgcolor': 'rgb(45, 48, 56)',
                        'xaxis': {
                            'visible': False
                        },
                        'yaxis': {
                            'visible': False

                        }
                    }
                }))
        },
        {
            'id': ooc_graph_id + '_container',
            'children':
                daq.GraduatedBar(
                    id=ooc_graph_id,
                    className='progress_bar',
                    color={"gradient": True, "ranges": {"#4C78A8": [0, 5], "FFd15f": [5, 10]}},
                    showCurrentValue=False,
                    value=10,
                    size=140
                )
        },
        {
            'id': item + '_pf',
            'children': daq.Indicator(
                className ='Indicator',
                id=indicator_id,
                value=False,
                color='#ffd15f',
            )
        }
    )


def generate_metric_row(passed_id, style, col2, col3, col5, col6):
    if style is None:
        style = {
            'height': '100px',
            'width': '100%',
        }
    return html.Div(
        id=passed_id,
        className='row metric-row',
        style=style,
        children=[
            html.Div(
                id=col2['id'],
                style={'textAlign': 'center'},
                className='one column',
                children=col2['children']
            ),
            html.Div(
                id=col3['id'],
                style={
                    'height': '100%',
                },
                className='four columns',
                children=col3['children']
            ),
            html.Div(
                id=col5['id'],
                style={
                    'height': '100%',
                },
                className='three columns',
                children=col5['children']
            ),
            html.Div(
                id=col6['id'],
                style={
                    'display': 'flex',
                    'justifyContent': 'center'
                },
                className='one column',
                children=col6['children']
            )
        ]
    )


app.layout = html.Div([
    dcc.Interval(
        id='data_updater',
    ),
    html.Div(
        id='main_content_wrapper',
        children=[
            custom_people_component.PeopleComponent(
                id='people_component',
                value='Janek',
                names = names
            ),
            html.Div(
                id='graphs_wrapper',
                children=[
                    html.Div(
                        id='actual_data_wrapper',
                        children=[
                            html.Div(
                                id='status-container',
                                style={
                                },
                                children=[
                                    build_top_panel(),
                                ]
                            ),
                            html.Div(
                                id='feet_wrapper',
                                children=[
                                    custom_feet_component.FeetComponent(
                                        id='feet_component',
                                        sensorValues=sensor_values_mock
                                    )
                                ]
                            )
                        ]
                    ),
                    html.Div(
                        id='historic_data_wrapper',
                        children=[
                            html.Div(
                                style={
                                    'padding': '0 0 0 10px',
                                    'display': 'flex',
                                    'alignItems': 'flex-end'
                                },
                                children=[daq.BooleanSwitch(
                                    on=True,
                                    label="Anomalia",
                                    labelPosition="top",
                                    color='#FFd15f',
                                    style={
                                        'width': '200px',
                                        'marginTop': '10px',
                                    }
                                ),
                                    dcc.Dropdown(
                                        id='dropdown',
                                        options=[
                                            {'label': 'left foot front', 'value': 0},
                                            {'label': 'left foot middle', 'value': 1},
                                            {'label': 'left foot back', 'value': 2},
                                            {'label': 'right foot front', 'value': 3},
                                            {'label': 'right foot middle', 'value': 4},
                                            {'label': 'right foot back', 'value': 5},

                                        ],
                                        style={
                                            'backgroundColor': '#2d3038',
                                            'width': '800px',
                                        },
                                        multi=True,
                                    ),
                                ]
                            ),
                            dcc.Graph(
                                id='HistGraph',
                                figure={
                                    'data': [
                                        {'x': [1, 2, 3, 4, 5], 'y': [1, 2, 1, 15, 2], 'mode': 'lines+markers'},
                                        {'x': [1, 2, 3, 4, 5], 'y': [6, 3, 5, 8, 6], 'mode': 'lines+markers'},
                                    ],
                                    'layout': go.Layout(
                                        margin={'t': 30},
                                        showlegend=True,
                                        xaxis={'title': 'X Label'},
                                        yaxis={'title': 'y Label'},
                                        paper_bgcolor='rgb(45, 48, 56)',
                                        plot_bgcolor='rgb(45, 48, 56)',
                                        font_color="#FFd15f",
                                        height=400,
                                    )
                                }
                            )
                        ]
                    )
                ]
            ),
        ]
    )
])

class PatientsEnum(str, Enum):
    Janek = 1
    Elżbieta = 2
    Albert = 3
    Ewelina = 4
    Piotr = 5 
    Bartosz = 6

dropdown_traces_values = {
    0: "left foot front",
    1: "left foot middle",
    2: "left foot back",
    3: "right foot front",
    4: "right foot middle",
    5: "right foot back"
}


@app.callback(
    Output('feet_component', 'sensorValues'),
    Input('data_updater', 'n_intervals'),
    Input('people_component', 'value')
)
def update_foot_data(n_intervals, value):
    # return [n_intervals,0,0,0,0,0]
    raw_data = redis_connection.lindex(f'patient_{PatientsEnum[value]}', 0)
    if raw_data is None:
        return [0,0,0,0,0,0]
    patient_current_data = json.loads(raw_data)
    return [value_object['value'] for value_object in patient_current_data['trace']['sensors']]


# [
#     {'x': [1, 2, 3, 4, 5], 'y': [1, 2, 1, 15, 2], 'mode': 'lines+markers'},
#     {'x': [1, 2, 3, 4, 5], 'y': [6, 3, 5, 8, 6], 'mode': 'lines+markers'},
# ],

@app.callback(
    Output('HistGraph', 'figure'),
    Input('data_updater', 'n_intervals'),
    Input('people_component', 'value'),
    Input('dropdown', 'value')
)
def update_graph_data(n_intervals, current_patient, selected_traces):
    raw_data = redis_connection.lrange(f'patient_{PatientsEnum[current_patient]}', 0, -1)

    timestamps = [datetime.fromtimestamp(json.loads(raw_data_obj)['timestamp']) for raw_data_obj in raw_data]

    if selected_traces is None:
        traces = []
    else:
        traces = [
            {
                'name': dropdown_traces_values[trace_id],
                'x': timestamps,
                'y': [json.loads(raw_data_obj)['trace']['sensors'][trace_id]['value'] for raw_data_obj in raw_data],
                'mode': 'lines+markers'
            }
            for trace_id in selected_traces
        ]

    return {
    'data': traces,
    'layout': go.Layout(
            margin={'t': 30},
            showlegend=True,
            xaxis={'title': 'Timestamp'},
            yaxis={'title': 'Sensor value'},
            paper_bgcolor='rgb(45, 48, 56)',
            plot_bgcolor='rgb(45, 48, 56)',
            font_color="#FFd15f",
            height=400,
        )
    }




@app.callback(
    Output('left foot front_OOC_graph', 'value'),
    Output('left foot middle_OOC_graph', 'value'),
    Output('left foot back_OOC_graph', 'value'),
    Output('right foot front_OOC_graph', 'value'),
    Output('right foot middle_OOC_graph', 'value'),
    Output('right foot back_OOC_graph', 'value'),
    Output('left foot front_indicator', 'value'),
    Output('left foot middle_indicator', 'value'),
    Output('left foot back_indicator', 'value'),
    Output('right foot front_indicator', 'value'),
    Output('right foot middle_indicator', 'value'),
    Output('right foot back_indicator', 'value'),
    Input('data_updater', 'n_intervals'),
    Input('people_component', 'value')
)
def update_progress_bars_and_anomaly_indicator(n_intervals, current_patient):
    raw_data = redis_connection.lindex(f'patient_{PatientsEnum[current_patient]}', 0)
    if raw_data is None:
        return  0,0,0,0,0,0,False, False, False, False, False, False
    patient_current_data = json.loads(raw_data)
    return tuple(
        [
            value_object['value'] * 10 // 1023
            for value_object in patient_current_data['trace']['sensors']
        ] + [
            value_object['anomaly']
            for value_object in patient_current_data['trace']['sensors']
        ]
    )



@app.callback(
    Output('left foot front_sparkline_graph', 'figure'),
    Output('left foot middle_sparkline_graph', 'figure'),
    Output('left foot back_sparkline_graph', 'figure'),
    Output('right foot front_sparkline_graph', 'figure'),
    Output('right foot middle_sparkline_graph', 'figure'),
    Output('right foot back_sparkline_graph', 'figure'),
    Input('data_updater', 'n_intervals'),
    Input('people_component', 'value')
)
def update_small_graphs(n_intervals, current_patient):
    raw_data = redis_connection.lrange(f'patient_{PatientsEnum[current_patient]}', 0, 50)
    timestamps = [datetime.fromtimestamp(json.loads(raw_data_obj)['timestamp']) for raw_data_obj in raw_data]
    return tuple([go.Figure({
        'data': [{'x': timestamps, 'y': [json.loads(raw_data_obj)['trace']['sensors'][n]['value'] for raw_data_obj in raw_data],
                    'mode': 'lines+markers',
                    'line': {'color': 'rgb(255,209,95)'}}],
        'layout': {
            'margin': dict(
                l=0, r=0, t=0, b=0, pad=0
            ),
            'paper_bgcolor': 'rgb(45, 48, 56)',
            'plot_bgcolor': 'rgb(45, 48, 56)',
            'xaxis': {
                'visible': False
            },
            'yaxis': {
                'visible': False

            }
        }
    }) for n in range(6)])





# {
#   "birthdate": "1976",
#   "disabled": true,
#   "firstname": "El\u017cbieta",
#   "id": 12,
#   "lastname": "Kochalska",
#   "trace": {
#     "id": 13571805062019,
#     "name": "ela",
#     "sensors": [
#       {
#         "anomaly": false,
#         "id": 0,
#         "name": "L0",
#         "value": 1023
#       },
#       {
#         "anomaly": false,
#         "id": 1,
#         "name": "L1",
#         "value": 1023
#       },
#       {
#         "anomaly": false,
#         "id": 2,
#         "name": "L2",
#         "value": 1023
#       },
#       {
#         "anomaly": false,
#         "id": 3,
#         "name": "R0",
#         "value": 13
#       },
#       {
#         "anomaly": false,
#         "id": 4,
#         "name": "R1",
#         "value": 11
#       },
#       {
#         "anomaly": false,
#         "id": 5,
#         "name": "R2",
#         "value": 13
#       }
#     ]
#   }
# }

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0")