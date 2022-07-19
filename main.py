import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import Styles
import warnings
warnings.filterwarnings('ignore')
warnings.simplefilter("ignore", UserWarning)


app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP], url_base_pathname='/admin/dash/')


sidebar = html.Div(
    [
        html.H1("Controlling\nDashboard", style={'fontSize': '46px', 'fontWeight': 'bold'}),
        html.Hr(style={'borderColor': Styles.lightgrey}),
        html.H2("Department", className="lead", style={'fontSize': '30px'}),
        html.Hr(style={'borderColor': Styles.lightgrey}),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/home", active="exact"),
                dbc.NavLink("Sales", href="/sales", active="exact"),
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


@app.callback(
    dash.dependencies.Output('dd-output-container', 'children'),
    [dash.dependencies.Input('AgentSelect', 'value')])
def update_outputt(value):
    return ''


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.Div(children=[])
    elif pathname == "/sales":
        return html.Div(children=[])

    if pathname == "/sales":  # --> if has to be changed to elif once the other pages are added back to the main menu!
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
