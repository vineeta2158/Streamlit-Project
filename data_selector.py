import pandas as pd
from pandas import DataFrame

from PLC_live_data import live_data


def select_data(live: bool, Historian: bool, file_path: str) -> DataFrame:
    """
    It selects the required data and provides it!

    :param live: If Passed True returns Live Instance data
    :param Historian: If Passed True returns Historian Data
    :param file_path: File Path for fetching data from specific CSV file
    :return: Return Dataframe according to provided Parameters
    """
    if live:
        df = live_data()  # Live Data Function called
        return df
    if Historian:
        df = pd.read_csv(file_path)
        df = df.loc[(df['Timestamp'] != "Timestamp")]
        return df
    else:
        df = live_data()
        return df
