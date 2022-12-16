import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import Styles
import DataHandler as dh
import warnings
warnings.filterwarnings('ignore')
warnings.simplefilter("ignore", UserWarning)

app = dash.Dash(__name__, suppress_callback_exceptions=True,
                external_stylesheets=[dbc.themes.BOOTSTRAP],
                url_base_pathname='/')


sidebar = html.Div(
    [
        html.H1("Sports\nDashboard", style={'fontSize': '46px', 'fontWeight': 'bold'}),
        html.Hr(style={'borderColor': Styles.greys[3]}),
        html.H2("Section", className="lead", style={'fontSize': '30px'}),
        html.Hr(style={'borderColor': Styles.greys[3]}),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Cycling", href="/cycling", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=Styles.SIDEBAR_STYLE,
)


content = html.Div(id="page-content", style=Styles.CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content],
                      style={'backgroundColor': 'white'})


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.Div(children=[
            dcc.Upload()
        ])
    elif pathname == "/cycling":
        return html.Div(children=[
            html.Div([
                html.H1('Your Cycling Performance'),
            ], style={'width': '100%', 'display': 'inline-block', 'align': 'right', 'padding': Styles.graph_padding}),
            html.Hr(),
            # Display the first row of key performance indicators, triggered via the kpiboxes function located in the
            # Styles module.
            html.Div([
                # Show the risk willingness score.
                Styles.kpiboxes('Total Activities:', 1000, Styles.colorPalette[0]),
                Styles.kpiboxes('Total Time:', 1000, Styles.colorPalette[1]),
                Styles.kpiboxes('Total Distance:', 1000, Styles.colorPalette[2]),
                Styles.kpiboxes('Total Elevation:', 1000, Styles.colorPalette[3]),

            ]),
            html.Hr(),
            html.Div([
                # Dash Core Components Graph element.
                dcc.Graph(
                    id='Portfolio Backtesting Graph',
                    # Trigger the function in the Data_Handler module that retrieves both the date values as well as
                    # the backtesting values.
                    figure={'data': [{'x': [1, 2, 3, 4, 5, 6, 7, 8, 9],
                                      'y': [1, 2, 6, 7, 5, 7, 2, 8, 10],
                                      'type': 'bar', 'title': "Performance per Month (past 3 years)",
                                      'mode': 'line',
                                      'marker': {'color': Styles.colorPalette[0]},
                                      'line': {'width': 8}}],
                            'layout': {'title': 'Performance per Month (past 3 years)',
                                       'xaxis': {'title': 'Time as Date Stamps', 'tickangle': 0},
                                       'yaxis': {'title': 'Portfolio Value'}}}
                ),
            ], style=Styles.STYLE(100)),
            ])

    if pathname == "/xxx":
        return html.Div(children=[
            dcc.Tabs(id='tabs-example', value='tab-1', children=[
                dcc.Tab(label='1', value='tab-1'),
                dcc.Tab(label='2', value='tab-2'),
                dcc.Tab(label='3', value='tab-3'),
            ], style=Styles.TAB_STYLE),
            html.Hr(),
            html.Div(id='tabs-example-content')
        ])


@app.callback(Output('tabs-example-content', 'children'),
              Input('tabs-example', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([])
    elif tab == 'tab-2':
        return html.Div([])
    elif tab == 'tab-3':
        return html.Div([])


if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=8080, debug=True)
