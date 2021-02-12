import csv
import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")

mean = df.groupby(['Student Id','Level'], as_index = False)['Attempt'].mean()

fig = px.scatter(mean, x = 'Student Id', y = 'Level', size = 'Attempt', color = 'Attempt',title="Student's Attempts In Each Level")
fig.show()