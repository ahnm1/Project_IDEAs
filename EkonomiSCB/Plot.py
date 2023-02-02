from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import os


class PlotXY:
    def __init__(self):
        self.CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))


    def get_data(self, file):
        in_file = self.CURR_DIR_PATH + file
        df      = pd.read_csv(in_file)
        return df


    def set_max_min_color(self, df):
        return ['green' if x == min(df) else 'red' if x == max(df) else 'black' for x in df]


    def plot_data(self, df, x, y, title):
        # fig = go.Figure()

        fig = px.scatter(
            df, 
            x = x,
            y = y,
            color = self.set_max_min_color(df['layoffs']),
            title = title
            )
        return fig


if __name__ == '__main__':
    app = Dash(__name__)

    def set_layout(fig):

        app.layout   = html.Div(
            children = [

                html.H1(children = 'Economy'),
                dcc.Graph(figure = fig)
                ]
            )
    plotting = PlotXY()
    data     = plotting.get_data('/merge/' + 'clean_konkurser_1994-2022_from_api.csv')
    title    = 'Individuals layed off because of bankruptcy'
    set_layout(plotting.plot_data(data, 'date', 'layoffs', title))
    
    app.run_server(debug=True, use_reloader=True)

