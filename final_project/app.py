from dash import html, Dash

app = Dash(__name__)
app.layout = html.Div([html.H2("Hello Dash!")])
