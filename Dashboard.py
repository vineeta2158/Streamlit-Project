import statistics
from pandas import DataFrame
from streamlit import report_thread
from time_convert import end_time, time_strip, hour_behind
import streamlit as st
import pandas as pd
import datetime
from graphs import bar_graph, pie_graph, trend_line_chart, doughnut_graph, point_chart, area_chart, x_y_graph
import numpy as np
from data_selector import select_data
import SessionState
import os
from streamlit.server.server import Server
from streamlit.report_thread import get_report_ctx

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
    end_date=end_time(),
    end_time=end_time(),
    display_type="Graph",
    graph_type="Bar Chart",
    data_type="Historian",
    column=[],
    column_statistic=[],
    dynamic=False,
    Live_exlude_graph=['Trend Chart', 'Area Chart',
                       'X-Y Plotter']
)

ctx = get_report_ctx()
# get session id
session_id = ctx.session_id

# get session
server = Server.get_current()
session_info = server._session_info_by_id.get(session_id)
session = session_info.session

# register watcher
session._local_sources_watcher._register_watcher(
    os.path.join(os.path.dirname(__file__), session_state.file_name),
    'dummy:' + session_state.file_name
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
        "Display Type",
        ['Graph', 'CSV Data', 'OTHERS'],
        help="This select box is required to select the Type of Previewing the Data"
    )

    if session_state.display_type == "CSV Data":
        session_state.column = st.sidebar.multiselect("Tag Selection", all_columns())
    elif session_state.display_type == "Graph":
        session_state.graph_type = st.sidebar.selectbox(
            "Type of Chart",
            ['Bar Chart', 'Pie Chart', 'Trend Chart', 'Doughnut Chart', 'Point Chart', 'Area Chart', 'Table',
             'X-Y Plotter']
        )
        session_state.data_type = st.sidebar.selectbox(
            "Data Type",
            ['Historian', 'Live', 'Dynamic Historian']
        )
        if session_state.data_type == "Dynamic Historian":
            session_state.dynamic = True
        else:
            session_state.dynamic = False
        session_state.column = st.sidebar.multiselect("Tag Selection", all_columns())
        if session_state.data_type != "Live":
            today = datetime.datetime.now()
            session_state.start_date = st.sidebar.date_input('Start Date', session_state.start_date)
            session_state.start_time = st.sidebar.time_input("Start Time", session_state.start_time)
            if session_state.data_type != "Dynamic Historian":
                session_state.end_date = st.sidebar.date_input('End Date', today)
                session_state.end_time = st.sidebar.time_input("End Time", session_state.end_time)
            else:
                session_state.end_time = end_time()
            session_state.start, session_state.End = time_strip(
                session_state.start_date,
                session_state.start_time,
                session_state.end_date,
                session_state.end_time
            )
    run_app()  # App is finally run after all required session states are gathered
    trigger_rerun()


def run_app() -> None:
    """
    This function runs the actual portal app on screen for given session state params
    :return: This function doesnt return
    """
    if session_state.display_type == "Graph":
        if session_state.data_type != "Live":
            if session_state.End < session_state.start:
                st.title("End Time must be Greater than Start Time")
            else:
                df = data_provide()  # Gather data according to session state
                render_graph(df)  # render function called
        else:  # Live data
            df = data_provide()
            render_graph(df)
    elif session_state.display_type == "CSV Data":
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
        if session_state.graph_type == "X-Y Plotter" and len(session_state.column) == 1:
            st.error("Please select atleast Two tags in Tag selection")
        if session_state.data_type != "Live":
            session_state.column_statistic = st.multiselect("Select Tags For Statistics", all_columns_filtered())
            if not Enquiry(session_state.column_statistic):
                display_stats(df)
        if session_state.display_type == "Graph":
            if session_state.graph_type == "Bar Chart":
                bar_graph(df)
            elif session_state.graph_type == "Pie Chart":
                pie_graph(df)
            elif session_state.graph_type == "Doughnut Chart":
                doughnut_graph(df)
            elif session_state.graph_type == "Table":
                st.dataframe(df)
            elif session_state.graph_type == "Point Chart":
                point_chart(df)
            if session_state.data_type != "Live":
                if session_state.graph_type == "Trend Chart":
                    trend_line_chart(df)
                elif session_state.graph_type == "Area Chart":
                    area_chart(df)
                elif session_state.graph_type == 'X-Y Plotter':
                    x, y = st.beta_columns(2)
                    List = all_columns_filtered()
                    column1 = x.selectbox("Choose X axis Tag", List)
                    if column1 != "":
                        column2 = y.multiselect("Choose Y axis Tag", list(col for col in List if col != column1))
                        if Enquiry(column2):
                            st.subheader("Choose Y Tag to begin: ")
                        x_y_graph(df, column1, column2)
            else:
                if session_state.graph_type in session_state.Live_exlude_graph:
                    st.error(session_state.graph_type + " Cannot be plotted on Live graph ")


def data_provide() -> DataFrame:
    """
    It fetches, filters and provides the filtered DataFrame based on current session state.

    :return: It returns with the specific filtered Data required according to the session state
    """
    if session_state.display_type == "Graph":
        if session_state.data_type != "Live":
            df = pd.read_csv(session_state.file_name)  # read the csv of name given in session state
            df = data_freshness_check(df)
            df = df.loc[(df['Timestamp'] != "Timestamp")]  # Ignore the redundant column names in data, cleans data
            df = data_filter(df)  # data filter function called
            if session_state.dynamic:
                df = df.loc[
                    (df['Timestamp'].astype(np.int64) >= session_state.start)
                ]
            else:
                df = df.loc[
                    (df['Timestamp'].astype(np.int64) >= session_state.start)
                    & (df['Timestamp'].astype(np.int64) <= session_state.End)
                    ]
            return df
        else:
            # df = select_data(Historian=False, live=True, file_path=session_state.file_name)
            df = pd.read_csv(session_state.file_name)
            df = df.loc[(df['Timestamp'] != "Timestamp")]
            row_1 = df.tail(1)
            row_1 = data_filter(row_1)
            return row_1
    elif session_state.display_type == "CSV Data":
        df = pd.read_csv(session_state.file_name)
        df = data_freshness_check(df)
        df = df.loc[(df['Timestamp'] != "Timestamp")]
        df = data_filter(df)
        return df


def data_provide_raw() -> DataFrame:
    """
    It fetches and provides the Data required according to session state

    :return: It returns raw whole chunk of data required according to session state
    """
    if session_state.display_type == "Graph":
        if session_state.data_type != "Live":
            df = pd.read_csv(session_state.file_name)  # read the csv of name given in session state
            df = df.loc[(df['Timestamp'] != "Timestamp")]
            if session_state.dynamic:
                df = df.loc[
                    (df['Timestamp'].astype(np.int64) >= session_state.start)
                ]
            else:
                df = df.loc[
                    (df['Timestamp'].astype(np.int64) >= session_state.start)
                    & (df['Timestamp'].astype(np.int64) <= session_state.End)
                    ]
            return df
        else:
            df = select_data(Historian=False, live=True, file_path=session_state.file_name)
            return df
    elif session_state.display_type == "CSV Data":
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


def all_columns_filtered() -> list:
    """
    Creates a list of all columns that are selected in multiselect

    :return: It returns the list of all columns available in Filtered data set
    """
    df = data_provide()  # Raw dataframe is fetched
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
    report_thread.get_report_ctx()


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
        return df[column_list]  # returns the filtered data according to session state


def display_stats(df: DataFrame) -> None:
    """
    Displays data for each selected column stored in session state

    :param df: Current Data
    :return: Returns nothing
    """
    for name in session_state.column_statistic:
        mini = minimum(df, name)
        maxi = maximum(df, name)
        aver = average(df, name)
        st.header('Statistics for %s :' % name)
        st.subheader(' Minimum : `%d`  Maximum : `%d`  Average : `%d` \n ' % (
            mini, maxi, aver
        ))


def data_freshness_check(df: DataFrame) -> DataFrame:
    d2 = pd.read_csv(session_state.file_name)
    df_diff = pd.concat([df, d2]).drop_duplicates(keep=False)
    if df_diff.empty:
        return df
    else:
        return d2


def minimum(df: DataFrame, column_name: str) -> float:
    """
    generates minimum value for specified dataframe and column

    :param df: Given Dataframe
    :param column_name: Name of column
    :return: Returns a float minimum value
    """
    List = list(float(val) for val in df[column_name])
    return min(List)


def maximum(df: DataFrame, column_name: str) -> float:
    """
    generates maximum value for specified dataframe and column

    :param df: Given Dataframe
    :param column_name: Name of column
    :return: Returns a float maximum value
    """
    List = list(float(val) for val in df[column_name])
    return max(List)


def average(df: DataFrame, column_name: str) -> float:
    """
    generates average value for specified dataframe and column

    :param df: Given Dataframe
    :param column_name: Name of column
    :return: Returns a float average value
    """
    List = list(float(val) for val in df[column_name])
    return statistics.mean(List)


if __name__ == "__main__":  # this defines that main function is root function
    main()
