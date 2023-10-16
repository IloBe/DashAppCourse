#!/usr/bin/env -S python3 -i

"""
Plotly Dash Course
Assignment 3 - Building Graphs

Exercise to show some graphs and interactions
(https://github.com/plotly/datasets/blob/master/Dash-Course/US-Exports/2011_us_ag_exports.csv)
This csv file is stored in the general projects data directory.

Note:
All relevant Python libraries are stored in the virtual environment which is activated to run this code.

Author: Ilona Brinkmeier
Date: Oct. 2023
"""

##########################
# imports
##########################

from dash import Dash, dcc, html, Input, Output, no_update
import pandas as pd
import plotly.express as px

##########################
# coding
##########################

# incorporate data
df = pd.read_csv('../data/2011_us_ag_exports.csv')

# initialise the app
# create the components
app = Dash(__name__)

fig = px.bar(df,
             x="state", y="pork",
             title="US Agricultural Exports in 2011",
             labels={
                     'state': '',
                     'pork': 'Pork',
             },
             #height=500,  # all values are seen up to >1500
             range_y=[0, 200],  # cut all bars >200
             text_auto=True,
)
# see:
# https://plotly.com/python/creating-and-updating-figures/#magic-underscore-notation
fig.update_layout(
    title=dict(font=dict(size=16),),
)
fig.update_xaxes(title=None)

app.layout = html.Div([
    dcc.Graph(id="graph1", figure=fig),
])


if __name__ == '__main__':
    app.run(debug=True)