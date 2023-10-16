#!/usr/bin/env -S python3 -i

"""
Plotly Dash Course
Assignment 3 - Building Graphs

Exercise to show some graphs, dash ag grid and interactions
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
import dash_ag_grid as dag

##########################
# coding
##########################

# incorporate data
df = pd.read_csv('../data/2011_us_ag_exports.csv')
feat_labels = df.columns
columnDefs = []
for i in range(0, len(feat_labels)):
    columnDefs.append(
        {'field': feat_labels[i]},
    )

# initialise the app
app = Dash(__name__)

# app layout
app.layout = html.Div([
    html.Div(id="my-title",
             children="US Agricultural Exports in 2011"),
    html.Br(),
    dcc.Dropdown(id="state-dropdown",
                 options=df.state.unique(),
                 value=["Alabama","Arkansas"],
                 multi=True),
    dcc.Graph(id="graph1", figure={}),
    html.Div(id='table-here')
])


# add controls to build the interaction
@app.callback(
    Output(component_id='graph1', component_property='figure'),
    Input(component_id='state-dropdown', component_property='value')
)
def update_graph(states_selected):
    ''' 
    Returns the stacked bar chart of beef, pork, fresh fruits exports of the selected states.
    '''
    df_country = df[df.state.isin(states_selected)]
    fig1 = px.bar(data_frame=df_country,
                  x='state',
                  y=['beef','pork','fruits fresh'],
                  labels={
                      'state': 'State',
                      'variable': 'Food Group',
                      'value': 'Counter',
                  },
    )
    return fig1


@app.callback(
    Output(component_id='table-here', component_property='children'),
    Input(component_id='graph1', component_property='hoverData'),
    # ensure the callback is not triggered whenever the app is loaded or refreshed
    prevent_initial_call=True
)
def update_graph(data_hovered):
    '''
    Adds a dataframe of export values from the hovered country in the diagram above.
    '''
    print(f'data_hovered:\n{data_hovered}')
    country = data_hovered['points'][0]['x']
    print(f'country hovered: {country}')
    
    dff = df[df.state.isin([country])]    
    grid = dag.AgGrid(
        id="country-export-table",
        rowData=dff.to_dict("records"),
        columnDefs=columnDefs,
        columnSize="sizeToFit",
        defaultColDef={"resizable": True, "sortable": True, "filter": True},
        dashGridOptions={"pagination": True},
    )
    return grid


if __name__ == '__main__':
    app.run(debug=True)
