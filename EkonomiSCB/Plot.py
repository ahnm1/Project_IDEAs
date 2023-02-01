import plotly.express as px
import pandas as pd
import numpy as np
import os

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))

def get_data():
	in_file = CURR_DIR_PATH + '/merge/' + 'clean_konkurser_1994-2022_from_api.csv'
	df = pd.read_csv(in_file)
	return df

print(len(get_data()))

def plot_data(df):
	fig = px.scatter(
		df, 
		x = 'date',
		y = 'layoffs',
		# color = 'date'
	)
	return fig.show()

plot_data(get_data())

