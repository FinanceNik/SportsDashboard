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
