import dash_bootstrap_components as dbc
import Styles
import DataHandler as dh
import base64
import io
import dash
from dash.dependencies import Input, Output, State
from dash import dcc, html, dash_table
import page_sportsType
import pandas as pd
import warnings
import page_about

warnings.filterwarnings('ignore')
warnings.simplefilter("ignore", UserWarning)

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
                dbc.NavLink("Introduction", href="/", active="exact"),
                dbc.NavLink("Your Review", href="/review", active="exact"),
                dbc.NavLink("About This App", href="/about", active="exact"),
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
    if pathname == "/":
        return html.Div([
            dcc.Upload(
                id='upload-data',
                children=html.Div([
                    'Drag and Drop or ',
                    html.A('Select Files')
                ]),
                style={
                    'width': '100%',
                    'height': '60px',
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',
                    'textAlign': 'center',
                    'margin': '10px'
                },
                # Allow multiple files to be uploaded
                multiple=True
            ),
            html.Div(id='output-data-upload'),
        ])
    elif pathname == "/review":
        return html.Div(children=[
            dcc.Tabs(id='tabs-example', value='tab-1', children=[
                dcc.Tab(label='All Sports ', value='tab-1'),
                dcc.Tab(label='Select Sports Type', value='tab-2'),
            ], style=Styles.TAB_STYLE),
            html.Hr(),
            html.Div(id='tabs-example-content')])

    elif pathname == "/about":
        return page_about.render_content()


def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    return html.Div([
        html.H5(filename),
        dash_table.DataTable(
            df.to_dict('records'),
            [{'name': i, 'id': i} for i in df.columns]
        ),

        html.Hr(),  # horizontal line

        # For debugging, display the raw contents provided by the web browser
        html.Div('Raw Content'),
        html.Pre(contents[0:200] + '...', style={
            'whiteSpace': 'pre-wrap',
            'wordBreak': 'break-all'
        })
    ])


@app.callback(Output('tabs-example-content', 'children'),
              Input('tabs-example', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.Div(children=[
                html.Div([
                    html.H1('Your Overall Performance Across All Activities'),
                ], style={'width': '100%', 'display': 'inline-block', 'align': 'right',
                          'padding': Styles.graph_padding}),
                html.Hr(),
                html.Div([
                    dcc.Graph(
                        id='Activity Type Distribution',
                        figure={'data': [
                            {'values': dh.mostUsedActivityType(dh.currentYear)[2],
                             'labels': dh.mostUsedActivityType(dh.currentYear)[0],
                             'marker': {'colors': dh.mostUsedActivityType(dh.currentYear)[5]},
                             'type': 'pie', 'layout': {'margin': dict(t=0, b=100, l=0, r=0)}}]}),
                ], style=Styles.STYLE(100)),
                html.Div([
                    Styles.kpiboxes('Total Activities:', dh.allActivities.get_nrOfActivities(), Styles.colorPalette[0]),
                    Styles.kpiboxes('Total Time (in hrs):', dh.allActivities.get_totalActivityTime(),
                                    Styles.colorPalette[1]),
                    Styles.kpiboxes('Total Distance:', dh.allActivities.get_totalActivityDistance(),
                                    Styles.colorPalette[2]),
                    Styles.kpiboxes('Total Elevation:', dh.allActivities.get_totalElevationGain(),
                                    Styles.colorPalette[3]),
                ]),
                html.Hr(),
                html.Div([
                    # Dash Core Components Graph element.
                    dcc.Graph(
                        id='Monthly Activities',
                        # Trigger the function in the Data_Handler module that retrieves both the date values as well as
                        # the backtesting values.
                        figure={'data': [{'x': dh.monthly_kpi_count(activityType="all",
                                                                    year=dh.currentYear,
                                                                    kpi="Activity Type")[0],
                                          'y': dh.monthly_kpi_count(activityType="all",
                                                                    year=dh.currentYear,
                                                                    kpi="Activity Type")[1],
                                          'type': 'bar', 'title': f"Number of Activities per Month in {dh.currentYear}",
                                          'mode': 'line',
                                          'marker': {'color': Styles.colorPalette[0]},
                                          'line': {'width': 8}}],
                                'layout': {'title': f"Number of Activities per Month in {dh.currentYear}",
                                           'xaxis': {'title': 'Time in Months', 'tickangle': 0},
                                           'yaxis': {'title': 'Number of Activies'}}}
                    ),
                ], style=Styles.STYLE(49)),
                html.Div([''], style=Styles.FILLER()),
                html.Div([
                    # Dash Core Components Graph element.
                    dcc.Graph(
                        id='Monthy Distance',
                        # Trigger the function in the Data_Handler module that retrieves both the date values as well as
                        # the backtesting values.
                        figure={'data': [{'x': dh.monthly_kpi_sum(activityType="all",
                                                                  year=dh.currentYear,
                                                                  kpi="Distance")[0],
                                          'y': dh.monthly_kpi_sum(activityType="all",
                                                                  year=dh.currentYear,
                                                                  kpi="Distance")[1],
                                          'type': 'bar', 'title': f"Monthly Distance in {dh.currentYear}",
                                          'mode': 'line',
                                          'marker': {'color': Styles.colorPalette[1]},
                                          'line': {'width': 8}}],
                                'layout': {'title': f"Monthly Distance in {dh.currentYear}",
                                           'xaxis': {'title': 'Time in Months', 'tickangle': 0},
                                           'yaxis': {'title': 'Distance in KM'}}}
                    ),
                ], style=Styles.STYLE(49)),
                html.Hr(),
                html.Div([
                    # Dash Core Components Graph element.
                    dcc.Graph(
                        id='Monthy Moving Time',
                        # Trigger the function in the Data_Handler module that retrieves both the date values as well as
                        # the backtesting values.
                        figure={'data': [{'x': dh.monthly_kpi_sum(activityType="all",
                                                                  year=dh.currentYear,
                                                                  kpi="Moving Time")[0],
                                          'y': dh.monthly_kpi_sum(activityType="all",
                                                                  year=dh.currentYear,
                                                                  kpi="Moving Time")[1],
                                          'type': 'bar', 'title': f"Monthly Moving Time in {dh.currentYear}",
                                          'mode': 'line',
                                          'marker': {'color': Styles.colorPalette[2]},
                                          'line': {'width': 8}}],
                                'layout': {'title': f"Monthly Moving Time in {dh.currentYear}",
                                           'xaxis': {'title': 'Time in Months', 'tickangle': 0},
                                           'yaxis': {'title': 'Moving time in Hours'}}}
                    ),
                ], style=Styles.STYLE(49)),
                html.Div([''], style=Styles.FILLER()),
                html.Div([
                    # Dash Core Components Graph element.
                    dcc.Graph(
                        id='Monthy Elevation',
                        # Trigger the function in the Data_Handler module that retrieves both the date values as well as
                        # the backtesting values.
                        figure={'data': [{'x': dh.monthly_kpi_sum(activityType="all",
                                                                  year=dh.currentYear,
                                                                  kpi="Elevation Gain")[0],
                                          'y': dh.monthly_kpi_sum(activityType="all",
                                                                  year=dh.currentYear,
                                                                  kpi="Elevation Gain")[1],
                                          'type': 'bar', 'title': f"Monthly Elevation in {dh.currentYear}",
                                          'mode': 'line',
                                          'marker': {'color': Styles.colorPalette[3]},
                                          'line': {'width': 8}}],
                                'layout': {'title': f"Monthly Elevation in {dh.currentYear}",
                                           'xaxis': {'title': 'Time in Months', 'tickangle': 0},
                                           'yaxis': {'title': 'Elevation Gain in m'}}}
                    ),
                ], style=Styles.STYLE(49)),
            ])])
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


@app.callback(Output('output-data-upload', 'children'),
              Input('upload-data', 'contents'),
              State('upload-data', 'filename'),
              State('upload-data', 'last_modified'))
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children


if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=8080, debug=True)
