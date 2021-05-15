from streamlit import caching, report_thread
from time_convert import end_time, time_strip,hour_behind
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import datetime
from graphs import bar_graph, pie_graph
from plotly.subplots import make_subplots
import numpy as np
from data_selector import select_data
import SessionState

st.set_page_config(layout="wide",initial_sidebar_state="auto",page_title="ADMIN PORTAL")


session_state = SessionState.get(
    file_name="Node06.csv",
    start=0,
    End=0,
    start_date=hour_behind(),
    start_time=hour_behind(),
    end_date="",
    end_time=end_time(),
    display_type="Graph",
    graph_type="Bar Chart",
    data_type="hist",
    column = []
)

def main():
    if st.sidebar.button("Refresh"):
         st.experimental_rerun()
    session_state.display_type = st.sidebar.selectbox(
        "Display Type ",
        ['Graph', 'Table', 'OTHERS']
    )
    if session_state.display_type == "Table":
        session_state.column = st.sidebar.multiselect("Columns Filter",all_columns())
    elif session_state.display_type == "Graph":
        session_state.graph_type = st.sidebar.selectbox(
            "Graph Type",
            ['Bar Chart', 'Pie Chart', 'Trend Chart']
        )
        session_state.data_type = st.sidebar.selectbox(
            "Data Type",
            ['hist', 'live']
        )
        session_state.column = st.sidebar.multiselect("Columns Filter",all_columns(),default=session_state.column)
        if session_state.data_type == "hist":
            today = datetime.datetime.now()
            session_state.start_date = st.sidebar.date_input('Start date', session_state.start_date)
            session_state.start_time = st.sidebar.time_input("Start Time",session_state.start_time)
            session_state.end_date = st.sidebar.date_input('End date', today)
            if st.sidebar.button("Jump to Real Time"):
                session_state.end_time = today
                trigger_rerun()
                caching.clear_cache()
                st.experimental_rerun()
            session_state.end_time = st.sidebar.time_input("End Time",session_state.end_time,help="End Time gets reset to current time if Jump to real time button is clicked!")
            session_state.start, session_state.End = time_strip(
                session_state.start_date, 
                session_state.start_time, 
                session_state.end_date,
                session_state.end_time
            )
    run_app()



def run_app():
    
    if session_state.display_type == "Graph":
        if session_state.data_type == "hist":
            df = data_provide()
            print(df)
            print(
                session_state.file_name,
                session_state.start,
                session_state.End,
                session_state.start_date,
                session_state.start_time,
                session_state.end_date,
                session_state.end_time,
                session_state.display_type,
                session_state.graph_type,
                session_state.data_type,
                session_state.column
            )
            render_graph(df)
        else: # Live data
            df = data_provide()
            render_graph(df)
    elif session_state.display_type == "Table":
            st.title(session_state.file_name)
            df = data_provide()
            st.dataframe(df) # Needs Dataframe 
            
    else:
        st.title("Yet to be Developed :)")
 
       

def render_graph(df):
    if session_state.display_type == "Graph":
        if session_state.graph_type == "Bar Chart":
            bar_graph(data=df, st=st, go=go)
        elif session_state.graph_type == "Pie Chart":
            pie_graph(data=df, st=st, go=go, make_subplots=make_subplots)
        elif session_state.graph_type == "Trend Chart":
            st.title("Yet to be Developed :)")
            


def data_provide():
    if session_state.display_type == "Graph":
        if session_state.data_type == "hist":
            df = pd.read_csv(session_state.file_name)
            df = df.loc[(df['Timestamp'] != "Timestamp")]
            df = data_filter(df)
            df = df.loc[
                (df['Timestamp'].astype(np.int64) >= session_state.start) 
                & (df['Timestamp'].astype(np.int64) <= session_state.End)
            ]
            return df
        else:
            df = select_data(st, hist=False, live=True)
            df = data_filter(df)
            return df
    elif session_state.display_type == "Table":
        df = pd.read_csv(session_state.file_name)
        df = df.loc[(df['Timestamp'] != "Timestamp")]
        df = data_filter(df)
        return df



def data_provide_raw():
    if session_state.display_type == "Graph":
        if session_state.data_type == "hist":
            df = pd.read_csv(session_state.file_name)
            df = df.loc[(df['Timestamp'] != "Timestamp")]
            df = df.loc[
                (df['Timestamp'].astype(np.int64) >= session_state.start) 
                & (df['Timestamp'].astype(np.int64) <= session_state.End)
            ]
            return df
        else:
            df = select_data(st, hist=False, live=True)
            return df
    elif session_state.display_type == "Table":
        df = pd.read_csv(session_state.file_name)
        df = df.loc[(df['Timestamp'] != "Timestamp")]
        return df



def all_columns():
    df = data_provide_raw()
    print(df,"all columns data")
    columns = list(column for column in list(df.columns) if column != "Timestamp")
    print(columns)
    return columns



def Enquiry(lis1):
    if not lis1:
        return 1
    else:
        return 0
  
def trigger_rerun():
    ctx = report_thread.get_report_ctx()   

def data_filter(df):
    if Enquiry(session_state.column):
        return df
    else:
        column_list = ["Timestamp"] + session_state.column
        return df[column_list]



if __name__ == "__main__":
    main()