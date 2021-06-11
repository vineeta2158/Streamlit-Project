import datetime
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


Week1 = list(day for day in range(1,8))
Week2 = list(day for day in range(8,15))
Week3 = list(day for day in range(15,22))
Week4 = list(day for day in range(22,30))
Week5 = list(day for day in range(30,32))


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


def time_strip_only_day(start_date: datetime,  end_date: datetime) -> tuple[int, int]:
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


def year_list(df):
    year_list = list(dict.fromkeys(df["Timestamp"].apply(year_return)))
    return year_list


def year_return(time: datetime):
    return time.year

def month_list(df):
    month_list = list(dict.fromkeys(df["Timestamp"].apply(month_return)))
    return month_list


def month_return(time: datetime):
    return months[time.month - 1 ]

def week_return(time:datetime):
    if time.day in Week1:
        return "Week 1"
    elif time.day in Week2:
        return "Week 2"
    elif time.day in Week3:
        return "Week 3"
    elif time.day in Week4:
        return "Week 4"
    elif time.day in Week5:
        return "Week 5"

def week_list(df):
    week_list = list(dict.fromkeys(df["Timestamp"].apply(week_return)))
    return week_list
def quarter_list(df):
    df["Timestamp"] = df["Timestamp"].apply(month_return)
    df["Timestamp"] = df["Timestamp"].apply(quarter_return)
    quarters = list(dict.fromkeys(df["Timestamp"]))
    return quarters

def quarter_return(month_name):
    outstring=" "
    if month_name in quarter_1:
        return "Quarter 1"
    elif month_name in quarter_2:
        return "Quarter 2"
    elif month_name in quarter_3:
        return "Quarter 3"
    elif month_name in quarter_4:
        return "Quarter 4"