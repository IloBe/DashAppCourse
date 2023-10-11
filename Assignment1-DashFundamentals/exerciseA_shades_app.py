# import packages
from dash import Dash, dcc, html

import dash_bootstrap_components as dbc
import pandas as pd

##########################
# coding
##########################

# incorporate data
# shades csv file as dataframe
# info see: https://github.com/plotly/datasets/blob/master/Dash-Course/makeup-shades/README-shades.md
df_shades = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Dash-Course/makeup-shades/shades.csv')
brand_options = df_shades['brand'].unique()
brand_value_default = 'Revlon' if 'Revlon' in brand_options else brand_options[0]

# initialise the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# app layout
# Create app components
markdown = dcc.Markdown(id='shades-title-markdown',
                        children='My exercise A "shades" app',
                        style={'fontSize': 16, 'textAlign': 'left', 'color': 'blue'})
dropdown = dcc.Dropdown(id='shades-brand-dropdown',
                        options=brand_options,
                        value=brand_value_default)
radioitems = dcc.RadioItems(id='shades-group-radio',
                            options=[
                                {'label': " Fenty Beauty's PRO FILT'R Foundation Only", 'value': 0},
                                {'label': " Make Up For Ever's Ultra HD Foundation Only", 'value': 1},
                                {'label': " US Best Sellers", 'value': 2},
                                {'label': " BIPOC-recommended Brands with BIPOC Founders", 'value': 3},
                                {'label': " BIPOC-recommended Brands with White Founders", 'value': 4},
                                {'label': " Nigerian Best Sellers", 'value': 5},
                                {'label': " Japanese Best Sellers", 'value': 6},
                                {'label': " Indian Best Sellers", 'value': 7},
                            ],
)

# app Layout
app.layout = dbc.Container(
    [
        dbc.Row([dbc.Col([markdown], width=8)]),
        dbc.Row([dbc.Col([dropdown], width=6)]),
        html.Br(),
        dbc.Row([dbc.Col([radioitems], width=8)]),
    ]
)

# run the app
if __name__ == '__main__':
    app.run(debug=True)