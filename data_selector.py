import pandas as pd
from PLC_live_data import live_data


def select_data(st, live, hist):
    file_path = 'Node06.csv'
    if live:
        df = live_data()
        return df
    if hist:
        df = pd.read_csv(file_path)
        df = df.loc[(df['Timestamp'] != "Timestamp")]
        return df
    else:
        df = live_data()
        return df
