from dash import Dash, html, dcc
from Plot import PlotXY

app = Dash(__name__)

def set_layout(fig):

    app.layout   = html.Div(
        children = [

            html.H1(children = 'Economy'),
            dcc.Graph(figure = fig)
            ]
        )
plotting = PlotXY()
data     = plotting.get_data('/Konkurser/merge/' + 'clean_konkurser_1994-2022_from_api.csv')
set_layout(plotting.plot_data(data, 'date', 'layoffs', 'Individuals layed off because of bankruptcy'))

app.run_server(debug=True, use_reloader=True)