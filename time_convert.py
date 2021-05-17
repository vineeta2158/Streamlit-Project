import datetime


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
