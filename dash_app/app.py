from dash import html, Dash

app = Dash(__name__)
app.layout = html.Div([html.H2("Hello Dash!!!")])

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0")
