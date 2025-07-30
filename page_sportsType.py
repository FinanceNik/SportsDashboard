import Styles
import DataHandler as dh
from dash import dcc, html





def render_page_content(value):
    data = dh.Totals(value, dh.currentYear)
    thousandSeparator = lambda x: "{:,}".format(x)
    tAD = thousandSeparator(int(data.get_totalActivityDistance()))
    tEG = thousandSeparator(int(data.get_totalElevationGain()))
    return html.Div([
        html.Hr(),
        html.Div([
            Styles.kpiboxes(f'Total {value} Activities:',
                            data.get_nrOfActivities(),
                            Styles.colorPalette[0]),
            Styles.kpiboxes(f'Total {value} Time (in hrs):',
                            data.get_totalActivityTime(),
                            Styles.colorPalette[1]),
            Styles.kpiboxes(f'Total {value} Distance (in km):',
                            tAD,
                            Styles.colorPalette[2]),
            Styles.kpiboxes(f'Total {value} Elevation (in m):',
                            tEG,
                            Styles.colorPalette[3]),
        ]),
        html.Hr(),
        html.Div([
            dcc.Graph(
                id='Monthly Activities',
                figure={'data':
                            [
                                {'x': dh.monthly_kpi_count(activityType=value,
                                                            year=dh.currentYear-1,
                                                            kpi="Activity Type")[0],
                                  'y': dh.monthly_kpi_count(activityType=value,
                                                            year=dh.currentYear-1,
                                                            kpi="Activity Type")[1],
                                  'type': 'bar', 'title': {"text":f"Number of Activities per Month in {dh.currentYear}"},
                                  'mode': 'line',
                                  'marker': {'color': Styles.greys[2]},
                                  'line': {'width': 8}},
                                {'x': dh.monthly_kpi_count(activityType=value,
                                                           year=dh.currentYear,
                                                           kpi="Activity Type")[0],
                                 'y': dh.monthly_kpi_count(activityType=value,
                                                           year=dh.currentYear,
                                                           kpi="Activity Type")[1],
                         'type': 'bar', 'title': f"Number of Activities per Month in {dh.currentYear}",
                         'mode': 'line',
                         'marker': {'color': dh.higher_or_lower(value,"Activity Type" , "count")},
                         'line': {'width': 8}}],
                        'layout': {'title': {"text": f"Number of Activities per Month"},
                                   'xaxis': {'title': {"text":'Months', 'tickangle': 0}},
                                   'yaxis': {'title': {"text":'Number of Activies'}}
                                   }
                        }

            ),
        ], style=Styles.STYLE(49)),
        html.Div([''], style=Styles.FILLER()),
        html.Div([
            dcc.Graph(
                id='Monthy Distance',
                figure={'data': [{'x': dh.monthly_kpi_sum(activityType=value,
                                                          year=dh.currentYear-1,
                                                          kpi="Distance")[0],
                                  'y': dh.monthly_kpi_sum(activityType=value,
                                                          year=dh.currentYear-1,
                                                          kpi="Distance")[1],
                                  'type': 'bar',
                                  'mode': 'line',
                                  'marker': {'color': Styles.greys[2]},
                                  'line': {'width': 8}},
                                  {'x': dh.monthly_kpi_sum(activityType=value,
                                                         year=dh.currentYear,
                                                         kpi="Distance")[0],
                                  'y': dh.monthly_kpi_sum(activityType=value,
                                                         year=dh.currentYear,
                                                         kpi="Distance")[1],
                                 'type': 'bar',
                                 'mode': 'line',
                                 'marker': {'color': dh.higher_or_lower(value,"Distance" , "sum")},
                                 'line': {'width': 8}}],
                        'layout': {'title': {"text": "Monthly Distance"},
                                   'xaxis': {'title': {"text": 'Months'}, 'tickangle': 0},
                                   'yaxis': {'title': {"text": 'Distance in KM'}}}}
            ),
        ], style=Styles.STYLE(49)),
        html.Hr(),
        html.Div([
            dcc.Graph(
                id='Monthy Moving Time',
                figure={'data': [{'x': dh.monthly_kpi_sum(activityType=value,
                                                          year=dh.currentYear - 1,
                                                          kpi="Moving Time")[0],
                                  'y': dh.monthly_kpi_sum(activityType=value,
                                                          year=dh.currentYear - 1,
                                                          kpi="Moving Time")[1],
                                  'type': 'bar',
                                  'mode': 'line',
                                  'marker': {'color': Styles.greys[2]},
                                  'line': {'width': 8}},
                                 {'x': dh.monthly_kpi_sum(activityType=value,
                                                          year=dh.currentYear,
                                                          kpi="Moving Time")[0],
                                  'y': dh.monthly_kpi_sum(activityType=value,
                                                          year=dh.currentYear,
                                                          kpi="Moving Time")[1],
                                  'type': 'bar',
                                  'mode': 'line',
                                  'marker': {'color': dh.higher_or_lower(value,"Moving Time" , "sum")},
                                  'line': {'width': 8}}],
                        'layout': {'title': {"text": "Monthly Moving Time"},
                                   'xaxis': {'title': {"text":'Months'}, 'tickangle': 0},
                                   'yaxis': {'title': {"text":'Moving time in Hours'}}}}
            ),
        ], style=Styles.STYLE(49)),
        html.Div([''], style=Styles.FILLER()),
        html.Div([
            dcc.Graph(
                id='Monthy Elevation',
                figure={'data': [{'x': dh.monthly_kpi_sum(activityType=value,
                                                          year=dh.currentYear - 1,
                                                          kpi="Elevation Gain")[0],
                                  'y': dh.monthly_kpi_sum(activityType=value,
                                                          year=dh.currentYear - 1,
                                                          kpi="Elevation Gain")[1],
                                  'type': 'bar',
                                  'mode': 'line',
                                  'marker': {'color': Styles.greys[2]},
                                  'line': {'width': 8}},
                                  {'x': dh.monthly_kpi_sum(activityType=value,
                                                          year=dh.currentYear,
                                                          kpi="Elevation Gain")[0],
                                  'y': dh.monthly_kpi_sum(activityType=value,
                                                          year=dh.currentYear,
                                                          kpi="Elevation Gain")[1],
                                  'type': 'bar',
                                  'mode': 'line',
                                  'marker': {'color': dh.higher_or_lower(value,"Elevation Gain" , "sum")},
                                  'line': {'width': 8}}],
                        'layout': {'title': {"text": "Monthly Elevation"},
                                   'xaxis': {'title': {"text": 'Months'}, 'tickangle': 0},
                                   'yaxis': {'title': {"text": 'Elevation Gain in m'}}}}
            ),
        ], style=Styles.STYLE(49)),
    ])
