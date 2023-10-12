#!/usr/bin/env -S python3 -i

"""
Plotly Dash Course
Assignment 1 - Dash Fundamentals

Exercise to show a data table of a 'Pudding' dataset
(https://github.com/the-pudding/data/tree/master/makeup-shades)

Author: Ilona Brinkmeier
Date: Oct. 2023
"""

##########################
# imports
##########################
from dash import Dash, dcc, html

import dash_ag_grid as dag
import dash_bootstrap_components as dbc
import pandas as pd

##########################
# coding
##########################

# incorporate data
# shades csv file as dataframe
# info see: https://github.com/plotly/datasets/blob/master/Dash-Course/makeup-shades/README-shades.md
df_shades = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Dash-Course/makeup-shades/shades.csv')
feat_labels = df_shades.columns
columnDefs = []
for i in range(0, len(feat_labels)):
    columnDefs.append(
        {'field': feat_labels[i]},
    )

# initialise the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# app layout
# create app components
markdown = dcc.Markdown(id='shades-title-markdown',
                        children='### My exercise B "shades" app',
                        style={'fontSize': 16, 'textAlign': 'left', 'color': 'black'})
grid = dag.AgGrid(
    id="shades-dag-example",
    rowData=df_shades.to_dict("records"),
    columnDefs=columnDefs,
    columnSize="sizeToFit",
    defaultColDef={"resizable": True, "sortable": True, "filter": True},
    dashGridOptions={"pagination": True},
)

# app Layout
app.layout = dbc.Container(
    [
        dbc.Row([dbc.Col([markdown], width=8)]),
        html.Br(),
        dbc.Row([dbc.Col(html.Div([grid]), width=12)]),
    ]
)

# run the app
if __name__ == '__main__':
    app.run(debug=True)
