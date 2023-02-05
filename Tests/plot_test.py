import os
import pandas as pd
from dash import Dash, html, dcc
from Plot import PlotXY
import plotly.express as px
import plotly.graph_objects as go

# app = Dash(__name__)

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
file_path = CURR_DIR_PATH + '/Bostader/clean/'
files     = os.listdir(file_path)
df_list   = [] 

for file in files:
    if file.startswith('clean'):
        # print(file_path + file)
        df = pd.read_csv(
            file_path + file,
            index_col  = False,
            engine     = 'python',
            skipfooter = 6)
        df_list.append(df)

# big_df = pd.(df_list, ignore_index = True)
print(len(df_list)) # .join(df_list[1:].drop('year', axis = 1))
# print(big_df)

# for df in df_list:
#     print(df.shape)

# new_df = pd.merge(df_list[0], df_list[1], 'right', 'år')
# print(new_df)
# print((df_list[0].shape[0] < df_list[1].shape[0]))

def merge_dfs(df_list):

    for i in range(len(df_list)):
        if 'år' in df_list[i].columns:
            print('yes')
    #     try:
    #         if df_list[i].shape[0] < df_list[i+1].shape[0]:
    #             df = pd.merge(df_list[i], df_list[i+1], 'right', 'år')
    #             # print(df_list[i].shape[0])
    #         else:
    #             df = pd.merge(df_list[i], df_list[i+1], 'left', 'år')
    #             pass
    #     except:
    #         if i >= len(df_list):
    #             # return df
    #             pass
            
    #         else:
    #             try:
    #                 df = pd.merge(df_list[i], df_list[i+1])
    #             except:
    #                 print('EXCEPT')
                
    return df

a = merge_dfs(df_list)
print(a)

# fig = go.Figure()

# print(smahus_data.columns)
# # # konkurs_trace = px.line(konkurs_data, x = 'date', y = 'layoffs')
# sales_trace   = px.line(sales_data, x = 'year', y = sales_data['medelpris_tkr'])
# amount_trace  = px.line(sales_data, x = 'year', y = sales_data['antal']/48)

# smahus_trace = px.line(smahus_data, x = 'år', y = 'Fastighetsprisindex_för_fritidshus_(1981=100)')

# # # fig.add_trace(konkurs_trace.data[0])
# fig.add_trace(sales_trace.data[0])
# fig.add_trace(amount_trace.data[0])

# fig.add_trace(smahus_trace.data[0])

# fig.show()



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

# s1 = [
#     ['a','b','c','d'],
#     ['a','b','c','d'],
#     ['a','b','c','d'],
#     ['a','b','c','d'],
#     ['a','b','c','d'],
# ]

# s2 = [
#     ['a','b'],
#     ['a','b'],
#     ['a','b'],
#     ['a','b'],
#     ['a','b']
# ]
# df1 = pd.DataFrame(s1)
# df2 = pd.DataFrame(s2)
# print(df1.shape)
# print(df2.shape)
# print(df1.shape[0] == df2.shape[0])