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