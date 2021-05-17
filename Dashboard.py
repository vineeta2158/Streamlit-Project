from pandas import DataFrame
from streamlit import caching, report_thread
from time_convert import end_time, time_strip, hour_behind
import streamlit as st
import pandas as pd
import datetime
from graphs import bar_graph, pie_graph, trend_line_chart
import numpy as np
from data_selector import select_data
import SessionState

# Page config defines the layout of page which includes params like layout, sidebar_status, title of page.
# Page config should run only once while executing code
st.set_page_config(layout="wide", initial_sidebar_state="auto", page_title="ADMIN PORTAL")

# Session state maintains data that defines the state of our program
# Values are initialized in Session.get

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
    column=[]
)


def main() -> None:
    """
    This is the root function that runs first before any other code.
    As Streamlit requires proper structured flow of functions main function is required.

    :return: It doesn't return anything
    """
    if st.sidebar.button("Refresh"):  # If refresh button is clicked!
        trigger_rerun()  # trigger rerun called

    # Sets the display_type session state for selected input
    session_state.display_type = st.sidebar.selectbox(
        "Display Type ",
        ['Graph', 'Table', 'OTHERS'],
        help="This select box is required to select the Type of Previewing the Data"
    )

    if session_state.display_type == "Table":
        session_state.column = st.sidebar.multiselect("Columns Filter", all_columns())
    elif session_state.display_type == "Graph":
        session_state.graph_type = st.sidebar.selectbox(
            "Graph Type",
            ['Bar Chart', 'Pie Chart', 'Trend Chart']
        )
        session_state.data_type = st.sidebar.selectbox(
            "Data Type",
            ['hist', 'live']
        )
        session_state.column = st.sidebar.multiselect("Columns Filter", all_columns())
        if session_state.data_type == "hist":
            today = datetime.datetime.now()
            session_state.start_date = st.sidebar.date_input('Start date', session_state.start_date)
            session_state.start_time = st.sidebar.time_input("Start Time", session_state.start_time)
            session_state.end_date = st.sidebar.date_input('End date', today)
            if st.sidebar.button("Jump to Current Time"):
                trigger_rerun()
                session_state.end_time = today
                trigger_rerun()
            session_state.end_time = st.sidebar.time_input("End Time", session_state.end_time, help=
            """End Time gets reset to current time if Jump to current time button is clicked! 
                                                           \n If it Doesnt work
                                                           \n Press Refresh before clicking Jump"""
                                                           )
            session_state.start, session_state.End = time_strip(
                session_state.start_date,
                session_state.start_time,
                session_state.end_date,
                session_state.end_time
            )
    run_app()  # App is finally run after all required session states are gathered


def run_app() -> None:
    """
    This function runs the actual portal app on screen for given session state params
    :return: This function doesnt return
    """
    if session_state.display_type == "Graph":
        if session_state.data_type == "hist":
            df = data_provide()  # Gather data according to session state
            render_graph(df)  # render function called
        else:  # Live data
            df = data_provide()
            render_graph(df)
    elif session_state.display_type == "Table":
        st.title(session_state.file_name)
        df = data_provide()
        st.dataframe(df)  # renders the dataframe
    elif session_state.display_type == "OTHERS":
        st.title("Yet to be Developed :)")


def render_graph(df: DataFrame) -> None:
    """
    Displays graph for specific session state
    Graph is displayed according to given dataframe

    :param df: Dataframe for which the graph is to be plotted
    :return: It returns nothing. It just plots and displays graph
    """
    if df.empty:
        st.title("No Data to display")
    else:
        if session_state.display_type == "Graph":
            if session_state.graph_type == "Bar Chart":
                bar_graph(df)
            elif session_state.graph_type == "Pie Chart":
                pie_graph(df)
            elif session_state.graph_type == "Trend Chart":
                trend_line_chart(df)


def data_provide() -> DataFrame:
    """
    It fetches, filters and provides the filtered DataFrame based on current session state.

    :return: It returns with the specific filtered Data required according to the session state
    """
    if session_state.display_type == "Graph":
        if session_state.data_type == "hist":
            df = pd.read_csv(session_state.file_name)  # read the csv of name given in session state
            df = df.loc[(df['Timestamp'] != "Timestamp")]  # Ignore the redundant column names in data, cleans data
            df = data_filter(df)  # data filter function called
            df = df.loc[
                (df['Timestamp'].astype(np.int64) >= session_state.start)
                & (df['Timestamp'].astype(np.int64) <= session_state.End)
                ]
            return df
        else:
            df = select_data(hist=False, live=True, file_path=session_state.file_name)
            df = data_filter(df)
            return df
    elif session_state.display_type == "Table":
        df = pd.read_csv(session_state.file_name)
        df = df.loc[(df['Timestamp'] != "Timestamp")]
        df = data_filter(df)
        return df


def data_provide_raw() -> DataFrame:
    """
    It fetches and provides the Data required according to session state

    :return: It returns raw whole chunk of data required according to session state
    """
    if session_state.display_type == "Graph":
        if session_state.data_type == "hist":
            df = pd.read_csv(session_state.file_name)  # read the csv of name given in session state
            df = df.loc[(df['Timestamp'] != "Timestamp")]
            df = df.loc[
                (df['Timestamp'].astype(np.int64) >= session_state.start)
                & (df['Timestamp'].astype(np.int64) <= session_state.End)
                ]
            return df
        else:
            df = select_data(hist=False, live=True, file_path=session_state.file_name)
            return df
    elif session_state.display_type == "Table":
        df = pd.read_csv(session_state.file_name)
        df = df.loc[(df['Timestamp'] != "Timestamp")]
        return df


def all_columns() -> list:
    """
    Creates a list of all columns for session state based data

    :return: It returns the list of all columns available in Raw data set
    """
    df = data_provide_raw()  # Raw dataframe is fetched
    columns = list(column for column in list(df.columns) if column != "Timestamp")
    return columns


def Enquiry(lis1: list) -> bool:
    """
    It checks whether the list provided is empty

    :param lis1: This is the Provided List

    :return: True: Provided List is empty
            False: Provided List is not empty
    """
    if not lis1:
        return True
    else:
        return False


def trigger_rerun() -> None:
    """
    Reruns the script from start.
    it can be used to refresh the program.

    :return: Doesnt return anything
    """
    ctx = report_thread.get_report_ctx()


def data_filter(df: DataFrame) -> DataFrame:
    """
    It Filters data according to column session state.
    converts the provided Dataframe to required column based dataframe

    :param df: Raw DataFrame is provided

    :return: Returns with filtered Data according to columns selected
    """
    if Enquiry(session_state.column):  # checks if no column is added to column list
        return df  # returns entire provided dataframe if no column is selected
    else:
        column_list = ["Timestamp"] + session_state.column  # adds the "Timestamp" column to local column list
        return df[column_list]  # returns the filtered data accoring to session state


if __name__ == "__main__":  # this defines that main function is root function
    main()
