import random
import plotly_express as px
import plotly.figure_factory as pff
import pandas as pd

list_of_numbers = []
attempt_val = []

df = pd.read_csv("Data/Rating.csv")

rating = df["Avg Rating"].tolist()


distribution_plot = pff.create_distplot([rating], ["Avg Rating"])
distribution_plot.show()

""" bar_graph = px.bar(x= list_of_numbers, y= attempt_val)

bar_graph.show() """