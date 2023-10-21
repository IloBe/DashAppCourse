#!/usr/bin/env -S python3 -i

"""
Plotly Dash Course
Assignment 4 - Advanced Apps

Exercise to show graphs and interactions with the 2011_us_ag_exports.csv dataset
(https://github.com/plotly/datasets/blob/master/Dash-Course/US-Exports/2011_us_ag_exports.csv).
This csv file is stored in the general projects data directory.
With the callback’s State argument we display a bar chart when a button is clicked. 

Note:
All relevant Python libraries are stored in the virtual environment which is activated to run this code.

Author: Ilona Brinkmeier
Date: Oct. 2023
"""

##########################
# imports
##########################

from dash import Dash, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

##########################
# coding
##########################

# incorporate data
df_ag = pd.read_csv('../data/2011_us_ag_exports.csv')
state_options = df_ag['state'].unique()
state_value_default = []
for state, i in zip(['Alabama', 'Arkansas'], [0, 1]):
    state_value_default.append(state) if state in state_options else state_options[i]

# initialise the app
# create the components
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
markdown = dcc.Markdown(id='shades-title-markdown',
                        children='My exercise A "US agriculture" advanced app with callback',
                        style={'fontSize': 16, 'textAlign': 'left', 'color': 'blue'})
title = html.Div(id='my-title',
                 children='US Agriculture Exports, 2011')
dropdown = dcc.Dropdown(id='state-dropdown',
                        options=state_options,
                        value=state_value_default,
                        multi=True)
button = dbc.Button(id="state-button",
                    children="Submit",
                    # button’s n_clicks property is None by default,
                    # so, without n_clicks = 0 you get:
                    # TypeError: '>' not supported between instances of 'NoneType' and 'int'
                    n_clicks = 0,)
graph = dcc.Graph(id='graph1',)

# app layout
app.layout = dbc.Container(
    [
        dbc.Row([dbc.Col([markdown], width=8)]),
        html.Br(),
        dbc.Row([dbc.Col([title], width=6)]),
        dbc.Row([dbc.Col([dropdown], width=12)]),
        html.Br(),
        dbc.Row([dbc.Col([button], width=6)]),
        dbc.Row([dbc.Col([graph], width=12)]),
    ]
)


# add controls to build the interaction
@app.callback(
    Output(component_id='graph1', component_property='figure'),
    Input(component_id='state-button', component_property='n_clicks'),
    State(component_id='state-dropdown', component_property='value'),
    prevent_initial_call=True   # without this, bootstrap style is used for empty figure of px.bar()
)
def update_graph(n_clicks, states_selected):
    '''
    Shows beef, pork, fruits fresh distributions as bar chart diagram of selected states,
    if the user has clicked the submit button.
    '''
    if n_clicks > 0:
        df_states = df_ag[df_ag.state.isin(states_selected)]
        fig1 = px.bar(
            data_frame=df_states,
            x='state', y=['beef','pork','fruits fresh'],
            labels={
                     'state': 'State',
                     'variable': 'Food Group',
                     'value': 'Counter',
            },
        )
        return fig1
    else:
        return px.bar()


# run the app
if __name__ == '__main__':
    app.run(debug=True)
