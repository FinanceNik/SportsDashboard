import dash_bootstrap_components as dbc
import Styles
import DataHandler as dh
import base64
import io
import dash
from dash.dependencies import Input, Output, State
from dash import dcc, html, dash_table
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
warnings.simplefilter("ignore", UserWarning)

app = dash.Dash(__name__, suppress_callback_exceptions=True,
                external_stylesheets=[dbc.themes.BOOTSTRAP],
                url_base_pathname='/')

sidebar = html.Div(
    [
        html.H1(f"Your {dh.currentYear}\n in Review", style={'fontSize': '46px', 'fontWeight': 'bold'}),
        html.Hr(style={'borderColor': Styles.greys[3]}),
        html.H2("Section", className="lead", style={'fontSize': '30px'}),
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

allActivities_Totals = aat = dh.Totals("all", 2022)


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
            html.Div([
                html.H1('Your Cycling Performance'),
            ], style={'width': '100%', 'display': 'inline-block', 'align': 'right', 'padding': Styles.graph_padding}),
            html.Hr(),
            html.Div(
                dash_table.DataTable(
                    id='stat_table',
                    columns=[{'name': i, 'id': i} for i in dh.mostUsedActivityType(dh.currentYear)[4]],
                    style_cell_conditional=[],
                    style_as_list_view=False,
                    style_cell={'padding': '5px', 'border-radius': '50px'},
                    style_header={'backgroundColor': Styles.colorPalette[0], 'fontWeight': 'bold', 'color': 'white',
                                  'border': '1px solid grey', 'height': '50px', 'font-size': '13px'},
                    style_table={'border': '1px solid lightgrey',
                                 'borderRadius': '10px',
                                 'overflow': 'hidden',
                                 'boxShadow': '5px 4px 5px 5px lightgrey'},
                    style_data={'border': '1px solid grey', 'font-size': '12px'},
                    data=dh.mostUsedActivityType(dh.currentYear)[4].to_dict('records')), style=Styles.STYLE(49)),
            html.Div([''], style=Styles.FILLER()),
            html.Div([
                dcc.Graph(
                    id='Activity Type Distribution',
                    figure={'data': [
                        {'values': dh.mostUsedActivityType(dh.currentYear)[2],
                         'labels': dh.mostUsedActivityType(dh.currentYear)[0],
                         'marker': {'colors': dh.mostUsedActivityType(dh.currentYear)[5]},
                         'type': 'pie', 'layout': {'margin': dict(t=0,b=100,l=0,r=0)}}]}),
            ], style=Styles.STYLE_PIE(49)),
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

    if pathname == "/about":
        return html.Div(children=[
            html.Div([html.H1('About the Creators...')], style={"textAlign": "center"}),
            html.Hr(),
            html.Div([], style={'width': f'{32}%', 'display': 'inline-block'}),
            # Display a picture for each creator of the tool.
            html.Div([
                html.Div([html.Img(src=app.get_asset_url('image.jpg'))], style={'width': f'{17.3}%', 'display': 'inline-block'}),
                ], style={'width': f'{17.3}%', 'display': 'inline-block', 'align': 'center', 'padding': '10px',
                          'box-shadow': Styles.boxshadow,
                          'borderRadius': '10px',
                          'overflow': 'hidden'}),
            html.Div([], style={'width': f'{1}%', 'display': 'inline-block'}),
            html.Div([
                html.Div([html.Img(src=app.get_asset_url('image_2.jpg'))],
                         style={'width': f'{17.3}%', 'display': 'inline-block'}),
            ], style={'width': f'{17.3}%', 'display': 'inline-block', 'align': 'center', 'padding': '10px',
                      'box-shadow': Styles.boxshadow,
                      'borderRadius': '10px',
                      'overflow': 'hidden'}),
            html.Div([], style={'width': f'{32}%', 'display': 'inline-block'}),
            html.Div([], style={'width': f'{32}%', 'display': 'inline-block'}),
            # Short descriptions of the creators and what they are specialized in.
            html.Div([
                html.Div([html.I("HSLU")], style={'textAlign': 'center'}),
                html.Div([html.I("MSc Banking & Finance")], style={'textAlign': 'center'}),
                html.Div([html.I("3rd Semester")], style={'textAlign': 'center'}),
                html.Div(html.Hr()),
                html.Div([html.I("Specialization:")], style={'textAlign': 'center', 'fontWeight': 'bold'}),
                html.Div([html.I("Data Science")], style={'textAlign': 'center'}),
            ], style={'textAlign': 'center', 'width': '17.3%', 'display': 'inline-block'}),
            html.Div([], style={'width': f'{1}%', 'display': 'inline-block'}),
            html.Div([
                html.Div([html.I("HSLU")], style={'textAlign': 'center'}),
                html.Div([html.I("MSc Banking & Finance")], style={'textAlign': 'center'}),
                html.Div([html.I("3rd Semester")], style={'textAlign': 'center'}),
                html.Div(html.Hr()),
                html.Div([html.I("Specialization:")], style={'textAlign': 'center', 'fontWeight': 'bold'}),
                html.Div([html.I("Asset Management")], style={'textAlign': 'center'}),
            ], style={'textAlign': 'center', 'width': '17.3%', 'display': 'inline-block'}),
            html.Hr(),
            html.Div([html.H1('About the Tool...')], style={"textAlign": "center"}),
            # Text body of what this tool was designed for and some background information.
            html.Div([
                html.P([
                    'This tool has been created as the final project for a masters level university course in Banking and',
                    html.Br(),
                    'Finance at the Lucerne School of Business. The subject is called Module 11 and focuses on a',
                    html.Br(),
                    'research project with practical application. The tool is meant as a way for asset managers,',
                    html.Br(),
                    'banks, and brokers to automate the process of creating a client`s portfolio.',
                    html.Br(),
                    html.Br(),
                    'Firstly, during an interview, the bank teller fills out a questionnaire with the respective client.',
                    html.Br(),
                    'This questionnaire establishes the client`s relationship towards risk tolerance and his or hers',
                    html.Br(),
                    'ability to take on risk and to absorb possible downfalls in the financial markets.',
                    html.Br(),
                    html.Br(),
                    'Secondly, the client can select the asset classes in which it is desired to be invested in',
                    html.Br(),
                    'and furthermore give the respective asset classes a minimum weight in the portfolio',
                    html.Br(),
                    'if so is desired.',
                    html.Br(),
                    html.Br(),
                    'Lastly, the inputs can be checked before submitting the data to the portfolio creation algorithm.',
                    html.Br(),
                    'The algorithm back-tests the performance of the selected assets and constraints when combined',
                    html.Br(),
                    'to a portfolio. The tool is calibrated to use the latest, scientifically established',
                    html.Br(),
                    'portfolio theory, namely Markowitz`s Modern Portfolio Theory and the accommodating',
                    html.Br(),
                    'Efficient Frontier. Moreover, the portfolio is selected based on a risk score',
                    html.Br(),
                    'that is established via the questionnaire`s input selections. The ',
                    html.Br(),
                    'selections splits the back-tested portfolios by volatility',
                    html.Br(),
                    'and chooses the portfolio with the highest Sharpe ratio',
                    html.Br(),
                    'that fits within a volatility bracket.',
                        ]),
                html.Hr()
            ], style={'textAlign': 'center', 'width': '100%', 'display': 'inline-block'}),
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
