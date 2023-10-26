from dash import html
from dash import dash_table

greys = ['#2b2b2b', '#3b3b3b', '#cfcfcf', '#f0f0f0']

colorPalette = {
    0: ['#495C83', '#7A86B6', '#A8A4CE', '#C8B6E2'],  # purple and very nice
    1: ['#06283D', '#1363DF', '#47B5FF', '#DFF6FF'],  # not so nice
    2: ['#354259', '#CDC2AE', '#ECE5C7', '#C2DED1'],  # not so nice
    3: ['#363062', '#4D4C7D', '#827397', '#E9D5CA'],  # other kind of purple, last colour could be better
    4: ['#0B132B', '#1C2541', '#3A506B', '#5BC0BE'],  # not so nice
    5: ['#993955', '#AE76A6', '#A3C3D9', '#CCD6EB'],  # not nice at all
    6: ['#5E5C6C', '#0B5563', '#A2BCE0', '#5299D3'],  # okay, but not great
    7: ['#0D1F2D', '#546A7B', '#9EA3B0', '#FAE1DF'],  # nah
    8: ['#373F51', '#008DD5', '#F56476', '#E43F6F'],  # red and blueish and kinda nice
    9: ['#2A4747', '#439775', '#48BF84', '#E0BAD7'],  # greenish and very nice
    }

purple_list = ['#495C83', '#7A86B6', '#A8A4CE', '#C8B6E2', '#363062', '#4D4C7D',
               '#827397', '#E9D5CA', '#495C83', '#7A86B6', '#A8A4CE', '#C8B6E2']

colorPalette = colorPalette[0]

strongGreen = '#37D151'
strongRed = '#FF5B5B'

graph_padding = '5px'

HEIGHT = 250

boxshadow = '5px 4px 5px 5px lightgrey'

TAB_STYLE = {'boxShadow': boxshadow,
                      'borderStyle': '',
                      'borderColor': greys[2],
                      'fontSize': '20px',
                      'color': greys[2],
                      "backgroundColor": greys[0],
                      'borderRadius': '15px'}

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "12em",
    "padding": "2rem 1rem",
    "backgroundColor": greys[0],
    'color': greys[2],
    'fontSize': '23px',
    'boxShadow': '5px 5px 5px 5px lightgrey'}

CONTENT_STYLE = {"marginLeft": "18rem", "marginRight": "2rem", "padding": "2rem 1rem"}


def STYLE(width):
    return{'width': f'{width}%', 'display': 'inline-block', 'align': 'center', 'padding': '10px',
             'boxShadow': boxshadow,
             'borderRadius': '10px',
             'overflow': 'hidden'}


def STYLE_PIE(width):
    return{'width': f'{width}%', 'display': 'inline-block', 'align': 'center', 'padding': '10px',
           'boxShadow': boxshadow,
           'height': '30vh',
           'borderRadius': '10px',
           'overflow': 'hidden'}


def STYLE_MINI():
    return{'width': '15%', 'display': 'inline-block', 'align': 'right', 'padding': '1px',
           'boxShadow': boxshadow,
           'borderRadius': '10px',
           'overflow': 'hidden',
           'height': 250}


def FILLER():
    return{'width': '2%', 'display': 'inline-block', 'align': 'right', 'padding': '5px'}


def kpiboxes(id, formula, color):
    return html.Div([
        dash_table.DataTable(
            id='kpi_table_TV',
            columns=[{'name': id, 'id': id}],
            style_cell_conditional=[],
            style_as_list_view=False,
            style_cell={'padding': '10px', 'textAlign': 'left'},
            style_header={'fontSize': '18px',
                          'fontFamily': 'sans',
                          'border': '1px solid white',
                          'backgroundColor': color,
                          'fontWeight': 'bold',
                          'color': 'white'},
            style_data={'fontFamily': 'sans',
                        'border': '1px solid white',
                        'backgroundColor': color,
                        'color': 'white',
                        'fontSize': '22px'},
            style_table={'border': '1px solid lightgrey',
                         'borderRadius': '10px',
                         'overflow': 'hidden',
                         'boxShadow': '5px 4px 5px 5px lightgrey'},
            data=[{id: formula}]
        )], style={'width': '25%', 'display': 'inline-block', 'align': 'left', 'padding': "20px"})


def conditional_box(id, formula):
    return html.Div([
        dash_table.DataTable(
            id='kpi_table_TV',
            columns=[{'name': id, 'id': id}],
            style_cell_conditional=[],
            style_as_list_view=False,
            style_cell={'padding': '10px', 'textAlign': 'left'},
            data=[{id: formula}],
            editable=False,
            style_header={'fontSize': '18px',
                          'fontFamily': 'Calibri',
                          'border': '1px solid white',
                          'backgroundColor': colorPalette[0],
                          'fontWeight': 'bold',
                          'color': 'white'},
            style_data={'fontFamily': 'Calibri',
                        'border': '1px solid white',
                        'backgroundColor': colorPalette[0],
                        'color': 'white',
                        'fontSize': '22px'},
            style_table={'border': '1px solid lightgrey',
                         'borderRadius': '10px',
                         'overflow': 'hidden',
                         'boxShadow': '5px 4px 5px 5px lightgrey'},
            style_data_conditional=[{'if': {'filter_query': f'{{{id}}} <= 0',
                                            'column_id': f'{id}'},
                                     'backgroundColor': strongRed, 'color': 'black'},
                                    {'if': {'filter_query': f'{{{id}}} > 0',
                                            'column_id': f'{id}'},
                                     'backgroundColor': strongGreen, 'color': 'black'},
                                    ]

        )], style={'width': '25%', 'display': 'inline-block', 'align': 'left', 'padding': "20px"})