from dash import html
import Styles
import main


def render_page_content():
    return html.Div(children=[
        html.Div([html.H1('About Our Fitness Insights App...')], style={"textAlign": "left"}),
        html.Hr(),
        html.H2('Empowering Your Fitness Journey'),
        html.P('Welcome to our Fitness Insights App! This application was born out of the idea that everyone should have access to meaningful insights about their fitness activities without any financial barrier. Many fitness enthusiasts use platforms like Strava, but the detailed analysis of your data often comes with a price tag.'),
        html.Hr(),
        html.H2('Bridging the Data Access Gap'),
        html.P("The mission is to bridge this gap and make fitness data accessible to everyone. I believe that understanding your activity patterns, setting goals, and tracking your progress should be available to all, regardless of subscription plans. That's why we created this app – to empower individuals on their fitness journey."),
        html.Hr(),
        html.H2('Motivation and Limits'),
        html.P('Analyzing your fitness data can be a powerful motivator. It not only helps you understand your achievements but also encourages you to push your limits. By providing insights into your activities, we aim to inspire you to take on new challenges, set personal records, and embrace a healthier lifestyle.'),
        html.Hr(),
        html.H2('Key Features'),
        html.P('Comprehensive Data Analysis: Explore detailed analyses of your activities, including types, distances, times, and elevation gains.'),
        html.P('Yearly Comparisons: Compare your performance across different years to track your progress and identify areas for improvement.'),
        html.P('Monthly Breakdowns: Dive into monthly breakdowns to understand your activity patterns and identify trends.'),
        html.P('No Subscription Required: Our app is free to use, with no subscription fees. We believe that everyone should have access to their fitness insights without financial constraints.'),
        html.Hr(),
        html.H2('Get Started'),
        html.P('1. Import your Strava data by going to the import data section and upload your .csv file.'),
        html.P('2. Explore your fitness insights by going to the dashboard section.'),
        html.P('3. Enjoy!'),
        html.Hr(),

    ], style={"width": "40%", "textAlign": "left"})

