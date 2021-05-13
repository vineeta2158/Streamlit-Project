import numpy as np


def double_digit_convert(str):
    if len(str) == 1:
        double_digit_string = "0" + str
        return double_digit_string
    else:
        return str


def time_strip(start_date, start_time, end_date, end_time):
    start_day = double_digit_convert(str(start_date.day))
    start_month = double_digit_convert(str(start_date.month))
    start_year = double_digit_convert(str(start_date.year))

    start_hour = double_digit_convert(str(start_time.hour))
    start_minute = double_digit_convert(str(start_time.minute))
    start_second = double_digit_convert(str(start_time.second))

    end_day = double_digit_convert(str(end_date.day))
    end_month = double_digit_convert(str(end_date.month))
    end_year = double_digit_convert(str(end_date.year))

    end_hour = double_digit_convert(str(end_time.hour))
    end_minute = double_digit_convert(str(end_time.minute))
    end_second = double_digit_convert(str(end_time.second))

    start = start_year + start_month + start_day + start_hour + start_minute + start_second
    end = end_year + end_month + end_day + end_hour + end_minute + end_second
    return (np.int64(start), np.int64(end))
