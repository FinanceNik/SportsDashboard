import Styles
import DataHandler as dh
from dash import dcc, html


def render_page_content():
    return html.Div([
            html.Hr(),
            html.Div([
                Styles.kpiboxes(f'Current Streak: ',
                                f'{dh.current_workout_streak()}',
                                Styles.colorPalette[0]),
                Styles.kpiboxes(f'Longest Streak: ',
                                f'{dh.longest_workout_streak()}',
                                Styles.colorPalette[1]),
                Styles.kpiboxes('Rain Ratio: ',
                                f"{round(dh.activity_rain_sun_ratio(),2)} %",
                                Styles.colorPalette[2]),
                Styles.kpiboxes(f'XXX',
                                f'0',
                                Styles.colorPalette[3]),
            ]),
            html.Hr()
    ])


