import statistics

from pandas import DataFrame


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
