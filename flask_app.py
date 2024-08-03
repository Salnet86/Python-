import dash
import dash_core_components as dcc
import dash_html_components as html




app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [4,5,6], 'y':[20,40,200], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name':  'DF'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])
if __name__ == '__main__':
    #app.run_server(debug=True)
    app.run_server(debug='False',port=8050,host='0.0.0.0')
    #app.run_server(host='127.0.0.1', debug=True)