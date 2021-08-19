#12 students attempting lesson 1 of grade 3 and lessson 1 is divided into 4 levels
import pandas as pd 
import plotly.express as px 
import plotly.graph_objects as go 
import csv

df = pd.read_csv("data.csv")
print(df.groupby("level")["attempt"].mean())

# df.loc() will help us filter out all the rows with the given student id. we need to create the filter with df['student_id'] == "TRL_987" and pass it to df.loc() will
student_df = df.loc[df['student_id'] == "TRL_987"]
print(student_df.groupby("level")["attempt"].mean())

fig = go.Figure(go.Bar(
    x = student_df.groupby("level")["attempt"].mean(), 
    y = ['Level 1', 'Level 2', 'Level 3', 'Level 4'],
    orientation = 'h'
    ))

fig.show()