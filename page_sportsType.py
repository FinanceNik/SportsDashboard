import Styles
import DataHandler as dh
from dash import dcc, html


def render_page_content(value):
    data = dh.Totals(value, dh.currentYear)
    return html.Div([
        html.Hr(),
        html.Div([
            Styles.kpiboxes(f'Total {value} Activities:', data.get_nrOfActivities(), Styles.colorPalette[0]),
            Styles.kpiboxes(f'Total {value} Time (in hrs):', data.get_totalActivityTime(),
                            Styles.colorPalette[1]),
            Styles.kpiboxes(f'Total {value} Distance:', data.get_totalActivityDistance(),
                            Styles.colorPalette[2]),
            Styles.kpiboxes(f'Total {value} Elevation:', data.get_totalElevationGain(),
                            Styles.colorPalette[3]),
        ]),
        html.Hr(),
        html.Div([
            # Dash Core Components Graph element.
            dcc.Graph(
                id='Monthly Activities',
                # Trigger the function in the Data_Handler module that retrieves both the date values as well as
                # the backtesting values.
                figure={'data': [{'x': dh.monthly_kpi_count(activityType=value,
                                                            year=dh.currentYear,
                                                            kpi="Activity Type")[0],
                                  'y': dh.monthly_kpi_count(activityType=value,
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
                figure={'data': [{'x': dh.monthly_kpi_sum(activityType=value,
                                                          year=dh.currentYear,
                                                          kpi="Distance")[0],
                                  'y': dh.monthly_kpi_sum(activityType=value,
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
                figure={'data': [{'x': dh.monthly_kpi_sum(activityType=value,
                                                          year=dh.currentYear,
                                                          kpi="Moving Time")[0],
                                  'y': dh.monthly_kpi_sum(activityType=value,
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
                figure={'data': [{'x': dh.monthly_kpi_sum(activityType=value,
                                                          year=dh.currentYear,
                                                          kpi="Elevation Gain")[0],
                                  'y': dh.monthly_kpi_sum(activityType=value,
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
    ])
