import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import dash_daq as daq
from custom_feet_component import FeetComponent

app = dash.Dash(__name__)
sensor_values_mock = [896, 568, 708, 23, 0, 5]

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


# Build header
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


params = ['sensor 1', 'sensor 2', 'sensor 3', 'sensor 4', 'sensor 5', 'sensor 6']


def generate_metric_row_helper(index):
    item = params[index]

    div_id = item + suffix_row
    button_id = item + suffix_button_id
    sparkline_graph_id = item + suffix_sparkline_graph
    count_id = item + suffix_count
    ooc_percentage_id = item + suffix_ooc_n
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
#                     'staticPlot': False,
#                     'editable': False,
                    'displayModeBar': False  #ukrywanie menu
                },
                figure=go.Figure({
                    'data': [{'x': [1,2,3,4,5], 'y': [1,2,1,15,2], 'mode': 'lines+markers', 'line': {'color': 'rgb(255,209,95)'}}],
                    'layout': {
#                         'uirevision': True,
                        'margin': dict(
                            l=0, r=0, t=0, b=0, pad=0
                        ),
                        'paper_bgcolor': 'rgb(45, 48, 56)',
                        'plot_bgcolor': 'rgb(45, 48, 56)',
                        'xaxis': {
                            'visible': False
                        },
                        'yaxis' :{
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
                    color={"gradient":True,"ranges":{"#4C78A8":[0,5],"FFd15f":[5,10]}},
                    showCurrentValue=False,
                    value=10,
                    size= 140
                )
        },
        {
            'id': item + '_pf',
            'children': daq.Indicator(
                id=indicator_id,
                value=False,
                color='#ffd15f',
            )
        }
    )


def generate_metric_row(id, style, col2, col3, col5, col6):
    if style is None:
        style = {
            'height': '100px',
            'width': '100%',
        }
    return html.Div(
        id=id,
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


def personButton(name, chosenOne=False):
    return html.Button(
        id=name,
        className='person',
        children=[
            html.Img(
                id=name + 'avatar',
                src= app.get_asset_url('personYellow.png') if chosenOne else app.get_asset_url('personBlue.png'),
                style={'width': '70%'}
            ),
            html.Div(
                id=name + 'label',
                style={
                    'color': '#95969A',
                    'fontSize': '20px',
                },
                children=[
                    name
                ]
            )
        ]
    )


app.layout = html.Div([
    html.Div(
        id='main_content_wrapper',
        children=[
            html.Div(
                id='choose_person_wrapper',
                children=[
                    personButton('Tomek', True),
                    personButton('Ania'),
                    personButton('Sandra'),
                    personButton('Szymon'),
                    personButton('Mateusz'),
                    personButton('Kacper'),
                ]
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
                                    # 'backgroundColor': 'green',
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
                            style= {
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
                            id = 'dropdown',
                                options=[
                                    {'label': 'left foot front', 'value': 'L1'},
                                    {'label': 'left foot middle', 'value': 'L2'},
                                    {'label': 'left foot back', 'value': 'L3'},
                                    {'label': 'right foot front', 'value': 'R1'},
                                    {'label': 'right foot middle', 'value': 'R2'},
                                    {'label': 'right foot back', 'value': 'R3'},

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
                                    id = 'HistGraph',
                                    figure = {
                                        'data' : [
                                           {'x': [1,2,3,4,5], 'y': [1,2,1,15,2], 'mode': 'lines+markers'},
                                           {'x': [1,2,3,4,5], 'y': [6,3,5,8,6], 'mode': 'lines+markers'},
                                        ],
                                        'layout' : go.Layout(
                                            margin={'t': 30},
                                            showlegend = True,
                                            xaxis = {'title': 'X Label'},
                                            yaxis = {'title': 'y Label'},
                                            paper_bgcolor = 'rgb(45, 48, 56)',
                                            plot_bgcolor = 'rgb(45, 48, 56)',
                                            font_color="#FFd15f",
                                            colorway = ['#4C78A8', '#3C6086', '#627F9E', '#517CB8', '#406393', '#49579D',],
                                            height = 400,
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


if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0")
