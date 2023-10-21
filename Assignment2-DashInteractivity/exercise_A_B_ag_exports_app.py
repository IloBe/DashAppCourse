#!/usr/bin/env -S python3 -i

"""
Plotly Dash Course
Assignment 2 - Dash interactivity

Horizontal solution
Exercise to create some Dash core components from an US agriculture dataset
(https://github.com/plotly/datasets/blob/master/Dash-Course/US-Exports/2011_us_ag_exports.csv)
This csv file is stored in the general projects data directory.

Author: Ilona Brinkmeier
Date: Oct. 2023
"""

##########################
# imports
##########################
from dash import Dash, dcc, html, callback, Output, Input

import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd

##########################
# coding
##########################

# incorporate data
# US agriculture export csv file as dataframe
# info: even the table includes state names only once and first one is Alabama,
# following coding makes sure even if table content changes the app UI content is the same;
# future toDo: no hard coded path strings - should be part of config concept
df_ag = pd.read_csv('../data/2011_us_ag_exports.csv')
state_options = df_ag['state'].unique()
state_value_default = []
for state, i in zip(['Alabama', 'Arkansas'], [0, 1]):
    state_value_default.append(state) if state in state_options else state_options[i]

# initialise the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# app layout
# create app components
markdown = dcc.Markdown(id='shades-title-markdown',
                        children='My exercise A, B "US agriculture" app',
                        style={'fontSize': 16, 'textAlign': 'left', 'color': 'blue'})
dropdown = dcc.Dropdown(id='state-dropdown',
                        options=state_options,
                        value=state_value_default,
                        multi=True)
title = html.Div(id='my-title',
                 children='US agriculture exports, 2011')
graph = dcc.Graph(id='graph1',
                  figure={})  # empty graph diagram


# app layout
app.layout = dbc.Container(
    [
        dbc.Row([dbc.Col([markdown], width=8)]),
        html.Br(),
        dbc.Row([dbc.Col([title], width=6)]),
        dbc.Row([dbc.Col([dropdown], width=12)]),
        dbc.Row([dbc.Col([graph], width=12)]),
    ]
)


# add controls to build the interaction
@callback(
    Output(component_id='graph1', component_property='figure'),
    Input(component_id='state-dropdown', component_property='value')
)
def update_graph(state_selected):
    ''' 
    Returns the stacked bar chart of beef, pork, fresh fruits exports of the selected states.
    '''

    # for other kind of masking compared to this pandas solution of 1 state selected see:
    # https://plotly.com/python/bar-charts/#bar-charts-with-wide-format-data
    # mask = df_ag['state'] == state_selected
    # px.bar(df[mask], ...)
    #df_country = df_ag.loc[df_ag['state'] == state_selected]

    df_country = df_ag.loc[df_ag['state'].isin(state_selected)]
    # note: pagination for graphs as future toDo
    fig = px.bar(df_country,
                 x='state',
                 y=['beef','pork','fruits fresh'],
                 labels={
                     'state': 'State',
                     'variable': 'Food Group',
                     'value': 'Counter',
                 },
                 height=600,
                )
    
    return fig


# run the app
if __name__ == '__main__':
    app.run(debug=True)