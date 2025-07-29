import Styles
import DataHandler as dh
from dash import dcc, html


def render_page_content():
    return html.Div([
        html.Div(children=[
            html.Div([
                html.H1('Your Overall Performance Across All Activities'),
            ], style={'width': '100%', 'display': 'inline-block', 'align': 'right',
                      'padding': Styles.graph_padding}),
            html.Hr(),
            html.Div([
                html.H4(f"{dh.currentYear - 1}"),
                dcc.Graph(
                    id='Activity Type Distribution',
                    figure={'data': [
                        {'values': dh.mostUsedActivityType(dh.currentYear - 1)[2],
                         'labels': dh.mostUsedActivityType(dh.currentYear - 1)[0],
                         'marker': {'colors': dh.mostUsedActivityType(dh.currentYear - 1)[5]},
                         'type': 'pie', 'layout': {'margin': dict(t=0, b=100, l=0, r=0)}}]}),
            ], style=Styles.STYLE(49)),
            html.Div([''], style=Styles.FILLER()),
            html.Div([
                html.H4(f"{dh.currentYear}"),
                dcc.Graph(
                    id='Activity Type Distribution',
                    figure={'data': [
                        {'values': dh.mostUsedActivityType(dh.currentYear)[2],
                         'labels': dh.mostUsedActivityType(dh.currentYear)[0],
                         'marker': {'colors': dh.mostUsedActivityType(dh.currentYear)[5]},
                         'type': 'pie', 'layout': {'margin': dict(t=0, b=100, l=0, r=0)}}]}),
            ], style=Styles.STYLE(49)),
            html.Div([
                Styles.kpiboxes(f'Total Activities ({dh.currentYear - 1} / {dh.currentYear}):',
                                f'{int(dh.Totals("all", dh.currentYear - 1).get_nrOfActivities())} '
                                f'/ {int(dh.Totals("all", dh.currentYear).get_nrOfActivities())}',
                                Styles.colorPalette[0]),
                Styles.kpiboxes(f'Total Time (in h.) ({dh.currentYear - 1} / {dh.currentYear}):',
                                f'{int(dh.Totals("all", dh.currentYear - 1).get_totalActivityTime())} '
                                f'/ {int(dh.Totals("all", dh.currentYear).get_totalActivityTime())}',
                                Styles.colorPalette[1]),
                Styles.kpiboxes(f'Total Distance ({dh.currentYear - 1} / {dh.currentYear}):',
                                f'{dh.thousands(dh.Totals("all", dh.currentYear - 1).get_totalActivityDistance())} '
                                f'/ {dh.thousands(dh.Totals("all", dh.currentYear).get_totalActivityDistance())}',
                                Styles.colorPalette[2]),
                Styles.kpiboxes(f'Total Elevation ({dh.currentYear - 1} / {dh.currentYear}):',
                                f'{dh.thousands(dh.Totals("all", dh.currentYear - 1).get_totalElevationGain())} '
                                f'/ {dh.thousands(dh.Totals("all", dh.currentYear).get_totalElevationGain())}',
                                Styles.colorPalette[3]),
            ]),
            html.Hr(),
            html.Div([
                dcc.Graph(
                    id='Monthly Activities',
                    figure={
                        'data': [
                            {
                                'x': dh.monthly_kpi_count(activityType="all",
                                                          year=dh.currentYear - 1,
                                                          kpi="Activity Type")[0],
                                'y': dh.monthly_kpi_count(activityType="all",
                                                          year=dh.currentYear - 1,
                                                          kpi="Activity Type")[1],
                                'type': 'bar',
                                'name': f"{dh.currentYear - 1}",
                                'marker': {'color': Styles.greys[2]},  # Keep previous year color as is
                            },
                            {
                                'x': dh.monthly_kpi_count(activityType="all",
                                                          year=dh.currentYear-0,
                                                          kpi="Activity Type")[0],
                                'y': dh.monthly_kpi_count(activityType="all",
                                                          year=dh.currentYear-0,
                                                          kpi="Activity Type")[1],
                                'type': 'bar',
                                'name': f"{dh.currentYear}",
                                'marker': {'color': dh.higher_or_lower("all","Activity Type" , "count")},
                            }
                        ],
                        'layout': {
                            'title': {'text':f'Number of Activities per Month in {dh.currentYear - 1} vs {dh.currentYear}'},
                            'xaxis': {'title': {"text":'Months'}},
                            'yaxis': {'title': {"text":'Number of Activities'}}
                        }
                    }
                ),
            ], style=Styles.STYLE(49)),
            html.Div([''], style=Styles.FILLER()),
            html.Div([
                dcc.Graph(
                    id='Monthly Distance',
                    figure={'data': [{'x': dh.monthly_kpi_sum(activityType="all",
                                                                year=dh.currentYear-1,
                                                                kpi="Distance")[0],
                                      'y': dh.monthly_kpi_sum(activityType="all",
                                                                year=dh.currentYear - 1,
                                                                kpi="Distance")[1],
                                      'type': 'bar', 'name': f"{dh.currentYear-1}",
                                      'marker': {'color': Styles.greys[2]},
                                      },
                                     {'x': dh.monthly_kpi_sum(activityType="all",
                                                                year=dh.currentYear,
                                                                kpi="Distance")[0],
                                      'y': dh.monthly_kpi_sum(activityType="all",
                                                                year=dh.currentYear,
                                                                kpi="Distance")[1],
                                      'type': 'bar', 'name': f"{dh.currentYear}",
                                      'marker': {'color': dh.higher_or_lower("all","Distance" , "sum")},
                                      }
                                     ],
                            'layout': {
                                'title': {'text':f'Distance per Month in {dh.currentYear - 1} vs {dh.currentYear}'},
                                'xaxis': {'title': {"text":'Months'}},
                                'yaxis': {'title': {"text":'Distance in km'}}}}
                ),
            ], style=Styles.STYLE(49)),
            html.Hr(),
            html.Div([
                dcc.Graph(
                    id='Monthly Time',
                    figure={'data': [{'x': dh.monthly_kpi_sum(activityType="all",
                                                                year=dh.currentYear-1,
                                                                kpi="Moving Time")[0],
                                      'y': dh.monthly_kpi_sum(activityType="all",
                                                                year=dh.currentYear - 1,
                                                                kpi="Moving Time")[1],
                                      'type': 'bar', 'name': f"{dh.currentYear-1}",
                                      'marker': {'color': Styles.greys[2]},
                                      },
                                     {'x': dh.monthly_kpi_sum(activityType="all",
                                                                year=dh.currentYear,
                                                                kpi="Moving Time")[0],
                                      'y': dh.monthly_kpi_sum(activityType="all",
                                                                year=dh.currentYear,
                                                                kpi="Moving Time")[1],
                                      'type': 'bar', 'name': f"{dh.currentYear}",
                                      'marker': {'color': dh.higher_or_lower("all","Moving Time" , "sum")},
                                      }
                                     ],
                            'layout': {
                                'title': {'text':f'Moving Time per Month in {dh.currentYear - 1} vs {dh.currentYear}'},
                                'xaxis': {'title': {"text":'Months'}},
                                'yaxis': {'title': {"text":'Moving Time in h'}}}}
                ),
            ], style=Styles.STYLE(49)),
            html.Div([''], style=Styles.FILLER()),
            html.Div([
                # Dash Core Components Graph element.
                dcc.Graph(
                    id='Monthly Elevation Gain',
                    figure={'data': [{'x': dh.monthly_kpi_sum(activityType="all",
                                                                year=dh.currentYear-1,
                                                                kpi="Elevation Gain")[0],
                                      'y': dh.monthly_kpi_sum(activityType="all",
                                                                year=dh.currentYear - 1,
                                                                kpi="Elevation Gain")[1],
                                      'type': 'bar', 'name': f"{dh.currentYear-1}",
                                      'marker': {'color': Styles.greys[2]},
                                      },
                                     {'x': dh.monthly_kpi_sum(activityType="all",
                                                                year=dh.currentYear,
                                                                kpi="Elevation Gain")[0],
                                      'y': dh.monthly_kpi_sum(activityType="all",
                                                                year=dh.currentYear,
                                                                kpi="Elevation Gain")[1],
                                      'type': 'bar', 'name': f"{dh.currentYear}",
                                      'marker': {'color': dh.higher_or_lower("all","Elevation Gain" , "sum")},
                                      }
                                     ],
                            'layout': {
                                'title': {'text':f'Elevation Gain per Month in {dh.currentYear - 1} vs {dh.currentYear}'},
                                'xaxis': {'title': {"text":'Months'}},
                                'yaxis': {'title': {"text":'Elevation Gain in M'}}}}
                ),
            ], style=Styles.STYLE(49)),
        ])])
