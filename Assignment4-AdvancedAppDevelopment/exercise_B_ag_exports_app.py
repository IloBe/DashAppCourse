#!/usr/bin/env -S python3 -i

"""
Plotly Dash Course
Assignment 4 - Advanced Apps

Exercise to show graphs and interactions with the 2011_us_ag_exports.csv dataset
(https://github.com/plotly/datasets/blob/master/Dash-Course/US-Exports/2011_us_ag_exports.csv).
This csv file is stored in the general projects data directory.
With dcc.Interval we simulate more data coming into the app from an external database.
Every 2 seconds more states will join the dataset.

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

# initialise the app
# create the components
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# initialise the app
# create the components
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
markdown = dcc.Markdown(id='shades-title-markdown',
                        children='My exercise B "US agriculture" advanced app with callback',
                        style={'fontSize': 16, 'textAlign': 'left', 'color': 'blue'})
title = html.Div(id='my-title',
                 children='US Agriculture Exports, 2011')
graph = dcc.Graph(id='graph1',)
interval = dcc.Interval(id='updates', interval=2000, n_intervals=0)  # update each 2 sec

# app layout
app.layout = dbc.Container(
    [
        dbc.Row([dbc.Col([markdown], width=8)]),
        html.Br(),
        dbc.Row([dbc.Col([title], width=6)]),
        dbc.Row([dbc.Col([graph], width=12)]),
        dbc.Row([dbc.Col([interval], width=12)]),
    ]
)


# add controls to build the interaction
@app.callback(
   Output(component_id='graph1', component_property='figure'),
   Input(component_id='updates', component_property='n_intervals'),
)
def update_graph(n):
    ''' 
    Includes 5 states and shows beef, pork, fruits fresh food type distributions of each state
    as bar chart automatically. Then the app stops showing an empty diagram again.
    
    '''
    if 0 < n < 6:
       state_added = df_ag.state[0:n]  # take rows from zero to n
       df_states = df_ag[df_ag['state'].isin(state_added) ]  # filter the df state column by state_added
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
