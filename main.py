import dash_bootstrap_components as dbc
import Styles
import DataHandler as dh
import dash
from dash.dependencies import Input, Output, State
from dash import dcc, html, dash_table
import page_sportsType
import page_sportsOverview
import page_sportsDetails
import page_about
import base64, io
import pandas as pd
import datetime


basePath = ''
app = dash.Dash(__name__, suppress_callback_exceptions=True,
                external_stylesheets=[dbc.themes.BOOTSTRAP],
                url_base_pathname='/', assets_folder='assets')

sidebar = html.Div(
    [
        html.H1(f"Your {dh.currentYear}\n in Review", style={'fontSize': '36px', 'fontWeight': 'bold'}),
        html.Hr(style={'borderColor': Styles.greys[3]}),
        html.H2("Section", className="lead", style={'fontSize': '28px'}),
        html.Hr(style={'borderColor': Styles.greys[3]}),
        dbc.Nav(
            [
                dbc.NavLink("Your Review", href=f"{basePath}/", active="exact"),
                dbc.NavLink("Import Data", href=f"{basePath}/import-data", active="exact"),
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

allActivities_Totals = aat = dh.Totals("all", dh.currentYear - 1)

def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))

            df.to_csv('./assets/activities.csv', index=False)
        elif 'xls' in filename:
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    return html.Div([
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),

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
                dcc.Tab(label='Detailed Analysis', value='tab-3'),
            ], style=Styles.TAB_STYLE),
            html.Hr(),
            html.Div(id='tabs-example-content')])

    elif pathname == f"{basePath}/import-data":
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
    elif tab == 'tab-3':
        return html.Div([
            page_sportsDetails.render_page_content(),
        ])


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
