import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import datetime
from graphs import bar_graph, pie_graph
from plotly.subplots import make_subplots

c1, c2, c3 = st.beta_columns(3)

file_path = 'Node06.csv'
df = pd.read_csv(file_path)

graph1 = c1.button('Graph')

with c2:
    view_result = st.button("TABLE")

if view_result:
    st.write(df)

c3.button("OTHER")

sD, sT = st.beta_columns(2)
eD, eT = st.beta_columns(2) 
today = datetime.datetime.now()
tomorrow = today + datetime.timedelta(days=1)
start_date = sD.date_input('Start date', today)
start_time = sT.time_input("Start Time", today)
end_date = eD.date_input('End date', tomorrow)
end_time = eT.time_input("End Time", tomorrow)
if start_date < end_date:
    st.success('Start date: `%s %s`\n\nEnd date:`%s %s`' % (start_date,start_time, end_date,end_time))
else:
    st.error('Error: End date must fall after start date.')


with c1:
    graph = st.selectbox("Available Charts: ",
                        [ 'Bar Chart', 'Pie Chart','Trend Chart'])
    st.write("You have selected : ", graph)


if graph == "Bar Chart":
    bar_graph(data=df,st=st,go=go)

if graph == "Pie Chart":
    pie_graph(data=df,st=st,go=go,make_subplots=make_subplots)


