import custom_people_component
import dash
from dash.dependencies import Input, Output
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div([
    custom_people_component.PeopleComponent(
        id='input',
        value='Janek',
        names=['Janek', 'Ela', 'Szymon', 'Tomek', 'Ania', 'Hania']
    ),
    html.Div(id='output')
])


@app.callback(Output('output', 'children'), [Input('input', 'value')])
def display_output(value):
    return 'You have entered {}'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)
