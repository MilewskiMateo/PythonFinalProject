import custom_feet_component
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import dash_daq as daq

app = dash.Dash(__name__)

sensor_values_mock = [896, 568, 708, 23, 0, 5]

theme = {
    'dark': True,
    'detail': '#2d3038',  # Background-card
    'primary': '#007439',  # Green
    'secondary': '#FFD15F',  # Accent
}

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
        style={
            'marginTop': '20px',
            'height': '500px',
            'width': '900px',
        },
        children=[
            generate_metric_list_header(),
            html.Div(
                id='metric_div',
                style={
                    'height': 'calc(100% - 70px)',
                    'overflow-x': 'hidden',
                    'overflow-y': 'hidden'
                },
                children=[
                    generate_metric_row_helper(1),
                    generate_metric_row_helper(2),
                    generate_metric_row_helper(3),
                    generate_metric_row_helper(4),
                    generate_metric_row_helper(5),
                    generate_metric_row_helper(6),
                    generate_metric_row_helper(7),

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
            'children': html.Div("Parameter")
        },
        {
            'id': "m_header_2",
            'children': html.Div("Count")
        },
        {
            'id': "m_header_3",
            'children': html.Div("Sparkline")
        },
        {
            'id': "m_header_4",
            'children': html.Div("OOC%")
        },
        {
            'id': "m_header_5",
            'children': html.Div("%OOC")
        },
        {
            'id': "m_header_6",
            'children': "Pass/Fail"
        })


params = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


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
            'children': html.Button(
                id=button_id,
                children=item,
                title="Click to visualize live SPC chart",
                n_clicks=0
            )
        },
        {
            'id': count_id,
            'children': '0'
        },
        {
            'id': item + '_sparkline',
            'children': dcc.Graph(
                id=sparkline_graph_id,
                style={
                    'width': '100%',
                    'height': '95%',
                },
                config={
                    'staticPlot': False,
                    'editable': False,
                    'displayModeBar': False
                },
                figure=go.Figure({
                    'data': [{'x': [], 'y': [], 'mode': 'lines+markers', 'name': item,
                              'line': {'color': 'rgb(255,209,95)'}}],
                    'layout': {
                        'uirevision': True,
                        'margin': dict(
                            l=0, r=0, t=4, b=4, pad=0
                        ),
                        'paper_bgcolor': 'rgb(45, 48, 56)',
                        'plot_bgcolor': 'rgb(45, 48, 56)'
                    }
                }))
        },
        {
            'id': ooc_percentage_id,
            'children': '0.00%'
        },
        {
            'id': ooc_graph_id + '_container',
            'children':
                daq.GraduatedBar(
                    id=ooc_graph_id,
                    color={"gradient": True, "ranges": {"green": [0, 3], "yellow": [3, 7], "red": [7, 15]}},
                    showCurrentValue=False,
                    max=15,
                    value=0
                )
        },
        {
            'id': item + '_pf',
            'children': daq.Indicator(
                id=indicator_id,
                value=True,
                color=theme['primary']
            )
        }
    )


def generate_metric_row(id, style, col1, col2, col3, col4, col5, col6):
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
                id=col1['id'],
                style={},
                className='one column',
                children=col1['children']
            ),
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
                id=col4['id'],
                style={},
                className='one column',
                children=col4['children']
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
                    'marginTop': '20px',
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
        style={
            'display': 'grid',
            'gridTemplateColumns': '1fr 3fr',
            'width': '100%',
            'height': '100vh',
        },
        children=[
            html.Div(
                id='choose_person_wrapper',
                style={
                    'display': 'grid',
                    'gridTemplateColumns': '1fr 1fr',
                    'gridTemplateRows': '1fr 1fr 1fr',
                    'backgroundColor': '#23262E',
                    'gap': '30px',
                    'padding': '20px',
                },
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
                style={
                    'display': 'grid',
                    'gridTemplateColumns': '1fr',
                    'gridTemplateRows': '1fr 1fr',
                },
                children=[
                    html.Div(
                        id='actual_data_wrapper',
                        style={
                            'display': 'grid',
                            'gridTemplateColumns': '2fr 1fr',
                        },
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
                                style={
                                    # 'backgroundColor': 'pink',
                                    'marginTop': '20px',
                                    'backgroundColor': '#2d3038',
                                    'display': 'flex',
                                    'justifyContent': 'center',
                                    'alignItems': 'center',
                                },
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
                        style={
                            'display': 'flex',
                            'justifyContent': 'center',
                            'alignItems': 'center',
                            # 'backgroundColor': 'blue'
                        },
                        children=[

                        ]
                    )
                ]
            ),
        ]
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
