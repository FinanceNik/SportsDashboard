from dash import html
import Styles
import main


def render_page_content():
    return html.Div(children=[
        html.Div([html.H1('About the Creators...')], style={"textAlign": "center"}),
        html.Hr(),
        html.Div([], style={'width': f'{32}%', 'display': 'inline-block'}),
        # Display a picture for each creator of the tool.
        html.Div([
            html.Div([html.Img(src=main.app.get_asset_url('image.jpg'))],
                     style={'width': f'{17.3}%', 'display': 'inline-block'}),
        ], style={'width': f'{17.3}%', 'display': 'inline-block', 'align': 'center', 'padding': '10px',
                  'box-shadow': Styles.boxshadow,
                  'borderRadius': '10px',
                  'overflow': 'hidden'}),
        html.Div([], style={'width': f'{1}%', 'display': 'inline-block'}),
        html.Div([
            html.Div([html.Img(src=main.app.get_asset_url('image_2.jpg'))],
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
        # Create a text about this project





    ])

# create a text

