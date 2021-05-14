from numpy import column_stack
from pylogix import PLC
from datetime import datetime
import pandas as pd
import time

comm1 = PLC()
comm1.Micro800 = True
comm1.IPAddress = '192.168.0.119'

comm2 = PLC()
comm2.Micro800 = True
comm2.IPAddress = '192.168.0.113'

comm3 = PLC()
comm3.Micro800 = True
comm3.IPAddress = '192.168.0.116'

FirstTime = True


def column_values(comm, string):
    T = comm.Read(string)
    T_data = str(T).split(' ')
    return T_data[1]


Real = list("Real" + str(i + 1) for i in range(15))


def live_data():
    try:

        T = list(column_values(comm=comm1, string=real) for real in Real)

        # DATA POLLING FROM PLC 2 - 192.168.0.113

        A = list(column_values(comm=comm2, string=real) for real in Real)

        # DATA POLLING FROM PLC 2 - 192.168.0.116

        X = list(column_values(comm=comm3, string=real) for real in Real)

        S = tuple(T + A + X)
        S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S21, S22, S23, S24, S25, S26, S27, S28, S29, S30, S31, S32, S33, S34, S35, S41, S42, S43, S44, S45, S46, S47, S48, S49, S50, S51, S52, S53, S54, S55 = S
        current_time = datetime.now()
        Timestamp = current_time.strftime("%Y%m%d%H%M%S")
        Data = {
            "Timestamp": Timestamp,
            "S1": S1,
            "S2": S2,
            "S3": S3,
            "S4": S4,
            "S5": S5,
            "S6": S6,
            "S7": S7,
            "S8": S8,
            "S9": S9,
            "S10": S10,
            "S11": S11,
            "S12": S12,
            "S13": S13,
            "S14": S14,
            "S15": S15,
            "S21": S21,
            "S22": S22,
            "S23": S23,
            "S24": S24,
            "S25": S25,
            "S26": S26,
            "S27": S27,
            "S28": S28,
            "S29": S29,
            "S30": S30,
            "S31": S31,
            "S32": S32,
            "S33": S33,
            "S34": S34,
            "S35": S35,
            "S41": S41,
            "S42": S42,
            "S43": S43,
            "S44": S44,
            "S45": S45,
            "S46": S46,
            "S47": S47,
            "S48": S48,
            "S49": S49,
            "S50": S50,
            "S51": S51,
            "S52": S52,
            "S53": S53,
            "S54": S54,
            "S55": S55,
        }
        df = pd.DataFrame(Data, index=[0])
        if type(df) is None:
            time.sleep(10)
            ds = live_data()
            return ds
        else:
            return df
    except ConnectionError:
        time.sleep(10)
        print('Connection Error caught')
