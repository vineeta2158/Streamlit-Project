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

dataframe1 = ''

FirstTime = True

# ========================================================== READ FROM PLC & WRITE TO DB ==========================================================

loop_PLC = True
fileName = 'Node06'
data0 = 'Timestamp,S1, S2,S3,S4,S5,S6,S7,S8,S9,S10,S11,S12,S13,S14,S15,S21,S22,S23,S24,S25,S26,S27,S28,S29,S30,S31,S32,S33,S34,S35,S41,S42,S43,S44,S45,S46,S47,S48,S49,S50,S51,S52,S53,S54,S55\n'


# open the file as write mode

#             data = ''.join(data2)
#       data = ''.join(map(str, data0))

def column_values(comm, str):
    T = comm.Read(str)
    T_data = str(T).split(' ')
    print(T_data[1])
    return T_data[1]


Real = [
    "Real1",
    "Real2",
    "Real3",
    "Real4",
    "Real5",
    "Real6",
    "Real7",
    "Real8",
    "Real9",
    "Real10",
    "Real11",
    "Real12",
    "Real13",
    "Real14",
    "Real15",
]

while loop_PLC:
    try:

        T = list(column_values(comm=comm1, str=real) for real in Real)

        # DATA POLLING FROM PLC 2 - 192.168.0.113

        A = list(column_values(comm=comm2, str=real) for real in Real)

        # DATA POLLING FROM PLC 2 - 192.168.0.116

        X = list(column_values(comm=comm3, str=real) for real in Real)

        S = tuple(T + A + X)
        S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S21, S22, S23, S24, S25, S26, S27, S28, S29, S30, S31, S32, S33, S34, S35, S41, S42, S43, S44, S45, S46, S47, S48, S49, S50, S51, S52, S53, S54, S55 = S
        current_time = datetime.now()
        Timestamp = current_time.strftime("%Y%m%d%H%M%S")
        # data2 = ['\n',Timestamp, '\n',T1_data[1] , ',\n', T2_data[1], '\n',T3_data[1],'\n', T4_data[1],'\n',
        # T5_data[1], '\n', T6_data[1], '\n', T7_data[1], '\n', T8_data[1], '\n', T9_data[1], '\n',
        # T10_data.split(' '), '\n',T11_data[1], '\n',T12_data[1], '\n', T13_data[1], '\n',T14_data[1], '\n',
        # T15_data[1]]
        data1 = [Timestamp, ',', S1, ',', S2, ',', S3, ',', S4, ',', S5, ',', S6, ',', S7, ',', S8, ',', S9, ',',
                 S10, ',', S11, ',', S12, ',', S13, ',', S14, ',', S15, ',', S21, ',', S22, ',', S23, ',', S24, ',',
                 S25, ',', S26, ',', S27, ',', S28, ',', S29, ',', S30, ',', S31, ',', S32, ',', S33, ',', S34, ',',
                 S35, ',', S41, ',', S42, ',', S43, ',', S44, ',', S45, ',', S46, ',', S47, ',', S48, ',', S49, ',',
                 S50, ',', S51, ',', S52, ',', S53, ',', S54, ',', S55, '\n']

        data = ''.join(map(str, data1))
        my_file = open(fileName, 'a')
        if FirstTime:
            my_file.write(data0)
            FirstTime = False
            print(data0)

        my_file.write(data)
        my_file.close()
        print('Writing Complete')

        dataframe1 = pd.read_csv(fileName)
        dataframe1.to_csv(fileName + '.csv', index=False)
        print('CSV DONE')
    except ConnectionError:
        time.sleep(10)
        print('Connection Error caught')
        continue
