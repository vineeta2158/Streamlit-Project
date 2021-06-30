import datetime
import numpy as np
import pandas as pd
from pandas import DataFrame

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

quarter_1 = [
    "January",
    "February",
    "March",
]

quarter_2 = [
    "April",
    "May",
    "June",
]

quarter_3 = [
    "July",
    "August",
    "September",
]

quarter_4 = [
    "October",
    "November",
    "December",
]

Quarters = [
    "Quarter 1",
    "Quarter 2",
    "Quarter 3",
    "Quarter 4"
]

Week1 = list(day for day in range(1, 8))
Week2 = list(day for day in range(8, 15))
Week3 = list(day for day in range(15, 22))
Week4 = list(day for day in range(22, 30))
Week5 = list(day for day in range(30, 32))


def double_digit_convert(string2: str) -> str:
    """
    converts single digit string to double digit

    :param string2: the input string to be converted
    :return: converted string is returned
    """
    if len(string2) == 1:
        double_digit_string = "0" + string2
        return double_digit_string
    else:
        return string2


def datetime_convert(time):
    time = str(time)
    return datetime.datetime.strptime(time, "%Y%m%d%H%M%S")


def time_strip(start_date: datetime, start_time: datetime, end_date: datetime, End_time: datetime) -> tuple[int, int]:
    """
    It strips time into integer tuple of start and end time

    :param start_date: start date selected
    :param start_time: start time selected
    :param end_date: end date selected
    :param End_time: end time selected
    :return: returns the packed integer values of converted datetime
    """
    start_day = double_digit_convert(str(start_date.day))
    start_month = double_digit_convert(str(start_date.month))
    start_year = double_digit_convert(str(start_date.year))

    start_hour = double_digit_convert(str(start_time.hour))
    start_minute = double_digit_convert(str(start_time.minute))
    start_second = double_digit_convert(str(start_time.second))

    end_day = double_digit_convert(str(end_date.day))
    end_month = double_digit_convert(str(end_date.month))
    end_year = double_digit_convert(str(end_date.year))

    end_hour = double_digit_convert(str(End_time.hour))
    end_minute = double_digit_convert(str(End_time.minute))
    end_second = double_digit_convert(str(End_time.second))

    start = start_year + start_month + start_day + start_hour + start_minute + start_second
    end = end_year + end_month + end_day + end_hour + end_minute + end_second
    return (int(start), int(end))


def time_strip_only_day(start_date: datetime, end_date: datetime) -> tuple[int, int]:
    """
    It strips time into integer tuple of start and end time

    :param start_date: start date selected
    :param start_time: start time selected
    :param end_date: end date selected
    :param End_time: end time selected
    :return: returns the packed integer values of converted datetime
    """
    start_day = double_digit_convert(str(start_date.day))
    start_month = double_digit_convert(str(start_date.month))
    start_year = double_digit_convert(str(start_date.year))

    end_day = double_digit_convert(str(end_date.day))
    end_month = double_digit_convert(str(end_date.month))
    end_year = double_digit_convert(str(end_date.year))

    start = start_year + start_month + start_day
    end = end_year + end_month + end_day
    return (int(start), int(end))


def required_format_timestamp(time: datetime):
    if time in Quarters:
        return time
    else:
        day = double_digit_convert(str(time.day))
        month = double_digit_convert(str(time.month))
        year = double_digit_convert(str(time.year))
        hour = double_digit_convert(str(time.hour))
        minute = double_digit_convert(str(time.minute))
        second = double_digit_convert(str(time.second))
        # timestamp = year + month + day + hour + minute + second
        # return int(timestamp)
        timestamp = day + "/" + month + "/" + year + " " + hour + ":" + minute + ":" + second
        return timestamp


def hour_behind() -> datetime:
    """
    returns time one hour behind from current time

    :return: datetime for one hour behind current time
    """
    today = datetime.datetime.now()
    hour_behind = today - datetime.timedelta(hours=1)
    return hour_behind


def end_time() -> datetime:
    """
    Provides the current time in datetime format
    :return: Provides the current time
    """
    today = datetime.datetime.now()
    return today


def today() -> datetime:
    """
    Provides time for current moment

    :return: current time in datetime data type
    """
    return datetime.datetime.now()


def hour_rename(time):
    year = str(time.year)
    day = str(time.day)
    month_name = month_return(time)
    hour = time.hour
    hour_plus_1 = time.hour + 1
    name = day + " " + month_name + " " + year + " " + double_digit_convert(
        str(hour)) + ":00 - " + double_digit_convert(str(hour_plus_1)) + ":00"
    return name


def daily_rename(time):
    name = "{0}/{1}/{2}".format(str(time.year), month_return(time), str(time.day))
    return name


def hour_list():
    hours = list(datetime.time(hr, 0).strftime('%H:%M') for hr in range(0, 24))
    return hours


def year_list(df):
    year_list = list(dict.fromkeys(df["Timestamp"].apply(year_return)))
    return year_list


def year_return(time: datetime):
    return time.year


def month_list(df):
    month_list = list(dict.fromkeys(df["Timestamp"].apply(month_return)))
    return month_list


def month_rename(time):
    year = str(time.year)
    month_name = month_return(time)
    name = year + " " + month_name
    return name


def month_return(time: datetime):
    return months[time.month - 1]


def fortnight_return(time):
    year = str(time.year)
    month_name = month_return(time)
    if time.day < 16:
        return year + " " + month_name + " 1st half"
    else:
        return year + " " + month_name + " 2nd half"


def pershift_time_converter(time: datetime):
    month_name = month_return(time)
    day = str(time.day)
    shift = shift_return(time)
    return month_name + " " + day + " " + shift


def pershift_list(df, session_state):
    if session_state.start_date >= session_state.end_date:
        return []
    else:
        df = df.loc[
            (df["Timestamp"] >= np.datetime64(session_state.start_date))
        ]
        df = df.loc[
            (df["Timestamp"] <= np.datetime64(session_state.end_date))
        ]
        pershift = list(dict.fromkeys(df["Timestamp"].apply(pershift_time_converter)))
        return pershift


def shift_return(time: datetime):
    if time.hour < 8:
        return "Shift 1"
    elif time.hour >= 8 and time.hour < 16:
        return "Shift 2"
    else:
        return "Shift 3"


def fortnight_list(df):
    fortnight_list = list(dict.fromkeys(df["Timestamp"].apply(fortnight_return)))
    return fortnight_list


def week_return(time: datetime):
    month_name = month_return(time)
    year = str(time.year)
    name = year + " " + month_name
    if time.day in Week1:
        return name + " Week 1"
    elif time.day in Week2:
        return name + " Week 2"
    elif time.day in Week3:
        return name + " Week 3"
    elif time.day in Week4:
        return name + " Week 4"
    else:
        return name + " Week 5"


def week_list(df):
    week_list = list(dict.fromkeys(df["Timestamp"].apply(week_return)))
    return week_list


def quarter_list(df):
    df["Timestamp"] = df["Timestamp"].apply(quarter_return)
    quarters = list(dict.fromkeys(df["Timestamp"]))
    return quarters


def quarter_return(time: datetime):
    year = str(time.year)
    month_name = month_return(time)
    if month_name in quarter_1:
        return year + " Quarter 1"
    elif month_name in quarter_2:
        return year + " Quarter 2"
    elif month_name in quarter_3:
        return year + " Quarter 3"
    elif month_name in quarter_4:
        return year + " Quarter 4"
