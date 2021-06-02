from datetime import datetime

from pandas._libs.tslibs.offsets import CustomBusinessHour, BusinessHour

from time_convert import datetime_convert, required_format_timestamp
from numpy import datetime64
import pandas as pd
from pandas.core.frame import DataFrame
import streamlit as st
import numpy as np


def period_filter(session_state):
    df: DataFrame = fetch_data(session_state)
    if df.empty:
        pass
    else:
        if session_state.period_type == "Hourly":
            df = period(df, freq="H")
        elif session_state.period_type == "Daily":
            df = period(df, freq="D")
        elif session_state.period_type == "Weekly":
            df = period(df, freq="W")
        elif session_state.period_type == "Per Shift":
            df = period(df, freq="8H")
        elif session_state.period_type == "Monthly":
            df = period(df, freq="M")
    return df


def period(df: DataFrame, freq: str) -> DataFrame:
    df = df.groupby(pd.Grouper(key="Timestamp", axis=1, freq=freq)).mean()
    df = df.dropna(axis=0)
    df.reset_index(inplace=True)
    df = df.rename(columns={'index': 'Timestamp'})
    return df

def fetch_data(session_state):
    df = pd.read_csv(session_state.file_name)
    df = df.loc[(df['Timestamp'] != "Timestamp")]  # Ignore the redundant column names in data, cleans data
    df = df.loc[(df['Timestamp'].astype(np.int64) >= session_state.start) & (
            df['Timestamp'].astype(np.int64) <= session_state.End)]
    # df = data_filter(df,session_state=session_state)# data filter function called
    columns = list(df.columns)
    for col in columns:
        if col != "Timestamp":
            df[col] = df[col].apply(pd.to_numeric, errors='ignore')
    df["Timestamp"] = df["Timestamp"].apply(datetime_convert)
    return df


def data_filter(df: DataFrame, session_state) -> DataFrame:
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
        return df[column_list]


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
