import dash_bootstrap_components as dbc
import Styles
import DataHandler as dh
import dash
from dash.dependencies import Input, Output, State
from dash import dcc, html, dash_table
import page_about


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

    ])
