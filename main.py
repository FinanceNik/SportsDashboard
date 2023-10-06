import dash_bootstrap_components as dbc
import Styles
import DataHandler as dh
import dash
from dash.dependencies import Input, Output
from dash import dcc, html
import page_sportsType
import page_sportsOverview
import page_about

basePath = '/sports-activities'

app = dash.Dash(__name__, suppress_callback_exceptions=True,
                external_stylesheets=[dbc.themes.BOOTSTRAP],
                url_base_pathname='/')

sidebar = html.Div(
    [
        html.H1(f"Your {dh.currentYear}\n in Review", style={'fontSize': '36px', 'fontWeight': 'bold'}),
        html.Hr(style={'borderColor': Styles.greys[3]}),
        html.H2("Section", className="lead", style={'fontSize': '28px'}),
        html.Hr(style={'borderColor': Styles.greys[3]}),
        dbc.Nav(
            [
                dbc.NavLink("Your Review", href=f"{basePath}/", active="exact"),
                dbc.NavLink("About This App", href=f"{basePath}/about", active="exact"),
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

allActivities_Totals = aat = dh.Totals("all", dh.currentYear-1)


@app.callback(
    dash.dependencies.Output('dd-output-container', 'children'),
    [dash.dependencies.Input('SportsSelect', 'value')])
def update_outputt(value):
    return page_sportsType.render_page_content(value)


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == f"{basePath}/":
        return html.Div(children=[
            dcc.Tabs(id='tabs-example', value='tab-1', children=[
                dcc.Tab(label='All Sports ', value='tab-1'),
                dcc.Tab(label='Select Sports Type', value='tab-2'),
            ], style=Styles.TAB_STYLE),
            html.Hr(),
            html.Div(id='tabs-example-content')])

    elif pathname == f"{basePath}/about":
        return page_about.render_page_content()


@app.callback(Output('tabs-example-content', 'children'),
              Input('tabs-example', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            page_sportsOverview.render_page_content(),
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Please select the type of activity you want to analyze:'),
            html.Div([
                dcc.Dropdown(id='SportsSelect', options=[{'label': i, 'value': i}
                                                         for i in dh.uniqueActivityTypes(dh.currentYear)],
                             value='Ride'),
                html.Div(id='dd-output-container'),
            ], style={'width': '100%', 'padding': Styles.graph_padding}),
        ])


if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=8080, debug=True)
