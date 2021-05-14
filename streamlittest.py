from time_convert import time_strip
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import datetime
from graphs import bar_graph, pie_graph
from plotly.subplots import make_subplots
import numpy as np
from data_selector import select_data
import SessionState

session_state = SessionState.get(
    start_date="",
    start_time="",
    end_date="",
    end_time="",
    display_type="Graph",
    graph_type="Bar Chart",
    data_type="hist",
)

c1, c2, c3 = st.beta_columns(3)
hist, live = st.beta_columns(2)
file_path = 'Node06.csv'
df = pd.read_csv(file_path)
df = df.loc[(df['Timestamp'] != "Timestamp")]

if c1.button("Graph"):
    session_state.display_type = "Graph"
if c2.button("Table"):
    session_state.display_type = "Table"
if c3.button("OTHER"):
    session_state.display_type = "Other"

if session_state.display_type == "Table":
    st.write(df)
if session_state.display_type == "Graph":
    with c1:
        session_state.graph_type = st.selectbox("Available Charts: ",
                                                ['Bar Chart', 'Pie Chart', 'Trend Chart'])
        st.write("You have selected : ", session_state.graph_type)
    if hist.button("hist"):
        session_state.data_type = "hist"
    if session_state.data_type == "hist":
        sD, sT = st.beta_columns(2)
        eD, eT = st.beta_columns(2)
        today = datetime.datetime.now()
        tomorrow = today + datetime.timedelta(days=1)
        session_state.start_date = sD.date_input('Start date', today)
        session_state.start_time = sT.time_input("Start Time")
        session_state.end_date = eD.date_input('End date', tomorrow)
        session_state.end_time = eT.time_input("End Time")

        start, End = time_strip(session_state.start_date, session_state.start_time, session_state.end_date,
                                session_state.end_time)
        # print(df)
        # df = df.loc[df["Timestamp"] != "Timestamp"]

        # types = list(value for value in df["Timestamp"])

        df = df.loc[(df['Timestamp'].astype(np.int64) >= start) & (df['Timestamp'].astype(np.int64) <= End)]

        if start <= End:
            st.success('Start date: `%s %s`\n\nEnd date:`%s %s`' % (
                session_state.start_date, session_state.start_time, session_state.end_date, session_state.end_time))
        else:
            st.error('Error: End date must fall after start date.')
        if session_state.graph_type == "Bar Chart":
            bar_graph(data=df, st=st, go=go)

        if session_state.graph_type == "Pie Chart":
            pie_graph(data=df, st=st, go=go, make_subplots=make_subplots)

    if live.button("live"):
        session_state.data_type = "live"
    if session_state.data_type == "live":
        df = select_data(st, hist=False, live=True)
        if session_state.graph_type == "Bar Chart":
            bar_graph(data=df, st=st, go=go)

        if session_state.graph_type == "Pie Chart":
            pie_graph(data=df, st=st, go=go, make_subplots=make_subplots)

        # st.rerun()
