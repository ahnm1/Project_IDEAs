import os
import pandas as pd
from dash import Dash, html, dcc
from Plot import PlotXY
import plotly.express as px
import plotly.graph_objects as go

# app = Dash(__name__)

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))


plotting = PlotXY()

konkurs_data = plotting.get_data(
    '/Konkurser/merge/' + 'clean_konkurser_1994-2022_from_api.csv')

sales_data = plotting.get_data(
    '/Bostader/clean/' + 'clean_forsaljning_bostadsratter_Medelpris_tkr_2000-2021.csv')

smahus_data = pd.read_csv(CURR_DIR_PATH +
    '/Bostader/clean/clean_fastighetsprisindex_fritidshus_1976-2022.csv',
)
print(smahus_data.columns)

fig = go.Figure()

print(smahus_data.columns)
# # konkurs_trace = px.line(konkurs_data, x = 'date', y = 'layoffs')
sales_trace   = px.line(sales_data, x = 'year', y = sales_data['medelpris_tkr'])
amount_trace  = px.line(sales_data, x = 'year', y = sales_data['antal']/48)

smahus_trace = px.line(smahus_data, x = 'år', y = 'Fastighetsprisindex_för_fritidshus_(1981=100)')

# # fig.add_trace(konkurs_trace.data[0])
fig.add_trace(sales_trace.data[0])
fig.add_trace(amount_trace.data[0])

fig.add_trace(smahus_trace.data[0])

fig.show()



# konkurs_fig  = plotting.plot_data(
#     konkurs_data, 'date', 'layoffs', 'Individuals layed off because of bankruptcy')


# print(sales_data.columns)


# sales_fig  = plotting.plot_data(
#     sales_data, 'year', 'medelpris_tkr', 'Apartment Sales') 


# app.layout   = html.Div(
#     children = [

#         html.H1(children = 'Economy'),
#         dcc.Graph(figure = konkurs_fig),
#         # dcc.Graph(figure = sales_fig),
#         ]
#     )

# app.run_server(debug=True, use_reloader=True)