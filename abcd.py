from pylogix import PLC
from datetime import datetime
import pandas as pd
import time
import re

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

while loop_PLC:
    try:
        Time_now = datetime.now()
        second = Time_now.strftime("%S")

        if (second >= "30" and second <= "30"):

            T1 = comm1.Read('Real1')
            T1_data = str(T1).split(' ')
            print(T1_data[1])
            S1 = T1_data[1]
            T2 = comm1.Read('Real2')
            T2_data = str(T2).split(' ')
            print(T2_data[1])
            S2 = T2_data[1]
            T3 = comm1.Read('Real3')
            T3_data = str(T3).split(' ')
            print(T3_data[1])
            S3 = T3_data[1]
            T4 = comm1.Read('Real4')
            T4_data = str(T4).split(' ')
            print(T4_data[1])
            S4 = T4_data[1]
            T5 = comm1.Read('Real5')
            T5_data = str(T5).split(' ')
            print(T5_data[1])
            S5 = T5_data[1]
            T6 = comm1.Read('Real6')
            T6_data = str(T6).split(' ')
            print(T6_data[1])
            S6 = T6_data[1]
            T7 = comm1.Read('Real7')
            T7_data = str(T7).split(' ')
            print(T7_data[1])
            S7 = T7_data[1]
            T8 = comm1.Read('Real8')
            T8_data = str(T8).split(' ')
            print(T8_data[1])
            S8 = T8_data[1]
            T9 = comm1.Read('Real9')
            T9_data = str(T9).split(' ')
            print(T9_data[1])
            S9 = T9_data[1]
            T10 = comm1.Read('Real10')
            T10_data = str(T10).split(' ')
            print(T10_data[1])
            S10 = T10_data[1]
            T11 = comm1.Read('Real11')
            T11_data = str(T11).split(' ')
            print(T11_data[1])
            S11 = T11_data[1]
            T12 = comm1.Read('Real12')
            T12_data = str(T12).split(' ')
            print(T12_data[1])
            S12 = T12_data[1]
            T13 = comm1.Read('Real13')
            T13_data = str(T13).split(' ')
            print(T13_data[1])
            S13 = T13_data[1]
            T14 = comm1.Read('Real14')
            T14_data = str(T14).split(' ')
            print(T14_data[1])
            S14 = T14_data[1]
            T15 = comm1.Read('Real15')
            T15_data = str(T15).split(' ')
            print(T15_data[1])
            S15 = T15_data[1]

            # DATA POLLING FROM PLC 2 - 192.168.0.113

            A1 = comm2.Read('Real1')
            A1_data = str(A1).split(' ')
            print(A1_data[1])
            S21 = A1_data[1]
            A2 = comm2.Read('Real2')
            A2_data = str(A2).split(' ')
            print(A2_data[1])
            S22 = A2_data[1]
            A3 = comm2.Read('Real3')
            A3_data = str(A3).split(' ')
            print(A3_data[1])
            S23 = A3_data[1]
            A4 = comm2.Read('Real4')
            A4_data = str(A4).split(' ')
            print(A4_data[1])
            S24 = A4_data[1]
            A5 = comm2.Read('Real5')
            A5_data = str(A5).split(' ')
            print(A5_data[1])
            S25 = A5_data[1]
            A6 = comm2.Read('Real6')
            A6_data = str(A6).split(' ')
            print(A6_data[1])
            S26 = A6_data[1]
            A7 = comm2.Read('Real7')
            A7_data = str(A7).split(' ')
            print(A7_data[1])
            S27 = A7_data[1]
            A8 = comm2.Read('Real8')
            A8_data = str(A8).split(' ')
            print(A8_data[1])
            S28 = A8_data[1]
            A9 = comm2.Read('Real9')
            A9_data = str(A9).split(' ')
            print(A9_data[1])
            S29 = A9_data[1]
            A10 = comm2.Read('Real10')
            A10_data = str(A10).split(' ')
            print(A10_data[1])
            S30 = A10_data[1]
            A11 = comm2.Read('Real11')
            A11_data = str(A11).split(' ')
            print(A11_data[1])
            S31 = A11_data[1]
            A12 = comm2.Read('Real12')
            A12_data = str(A12).split(' ')
            print(A12_data[1])
            S32 = A12_data[1]
            A13 = comm2.Read('Real13')
            A13_data = str(A13).split(' ')
            print(A13_data[1])
            S33 = A13_data[1]
            A14 = comm2.Read('Real14')
            A14_data = str(A14).split(' ')
            print(A14_data[1])
            S34 = A14_data[1]
            A15 = comm2.Read('Real15')
            A15_data = str(A15).split(' ')
            print(A15_data[1])
            S35 = A15_data[1]

            # DATA POLLING FROM PLC 2 - 192.168.0.116

            X1 = comm3.Read('Real1')
            X1_data = str(X1).split(' ')
            print(X1_data[1])
            S41 = X1_data[1]
            X2 = comm3.Read('Real2')
            X2_data = str(X2).split(' ')
            print(X2_data[1])
            S42 = X2_data[1]
            X3 = comm3.Read('Real3')
            X3_data = str(X3).split(' ')
            print(X3_data[1])
            S43 = X3_data[1]
            X4 = comm3.Read('Real4')
            X4_data = str(X4).split(' ')
            print(X4_data[1])
            S44 = X4_data[1]
            X5 = comm3.Read('Real5')
            X5_data = str(X5).split(' ')
            print(X5_data[1])
            S45 = X5_data[1]
            X6 = comm3.Read('Real6')
            X6_data = str(X6).split(' ')
            print(X6_data[1])
            S46 = X6_data[1]
            X7 = comm3.Read('Real7')
            X7_data = str(X7).split(' ')
            print(X7_data[1])
            S47 = X7_data[1]
            X8 = comm3.Read('Real8')
            X8_data = str(X8).split(' ')
            print(X8_data[1])
            S48 = X8_data[1]
            X9 = comm3.Read('Real9')
            X9_data = str(X9).split(' ')
            print(X9_data[1])
            S49 = X9_data[1]
            X10 = comm3.Read('Real10')
            X10_data = str(X10).split(' ')
            print(X10_data[1])
            S50 = X10_data[1]
            X11 = comm3.Read('Real11')
            X11_data = str(X11).split(' ')
            print(X11_data[1])
            S51 = X11_data[1]
            X12 = comm3.Read('Real12')
            X12_data = str(X12).split(' ')
            print(X12_data[1])
            S52 = X12_data[1]
            X13 = comm3.Read('Real13')
            X13_data = str(X13).split(' ')
            print(X13_data[1])
            S53 = X13_data[1]
            X14 = comm3.Read('Real14')
            X14_data = str(X14).split(' ')
            print(X14_data[1])
            S54 = X14_data[1]
            X15 = comm3.Read('Real15')
            X15_data = str(X15).split(' ')
            print(X15_data[1])
            S55 = X15_data[1]

            current_time = datetime.now()
            Timestamp = current_time.strftime("%Y%m%d%H%M%S")
            #             data2 = ['\n',Timestamp, '\n',T1_data[1] , ',\n', T2_data[1], '\n',T3_data[1],'\n', T4_data[1],'\n', T5_data[1], '\n', T6_data[1], '\n', T7_data[1], '\n', T8_data[1], '\n', T9_data[1], '\n',T10_data.split(' '), '\n',T11_data[1], '\n',T12_data[1], '\n', T13_data[1], '\n',T14_data[1], '\n', T15_data[1]]
            data1 = [Timestamp, ',', S1, ',', S2, ',', S3, ',', S4, ',', S5, ',', S6, ',', S7, ',', S8, ',', S9, ',',
                     S10, ',', S11, ',', S12, ',', S13, ',', S14, ',', S15, ',', S21, ',', S22, ',', S23, ',', S24, ',',
                     S25, ',', S26, ',', S27, ',', S28, ',', S29, ',', S30, ',', S31, ',', S32, ',', S33, ',', S34, ',',
                     S35, ',', S41, ',', S42, ',', S43, ',', S44, ',', S45, ',', S46, ',', S47, ',', S48, ',', S49, ',',
                     S50, ',', S51, ',', S52, ',', S53, ',', S54, ',', S55, '\n']

            # open the file as write mode

            #             data = ''.join(data2)
            data = ''.join(map(str, data1))
            my_file = open(fileName, 'a')
            if FirstTime == True:
                my_file.write(data0)
                FirstTime = False
                print(data0)

            my_file.write(data)
            my_file.close()
            print('Writing Complete')

            # list_var = ["PT"]
            # current_time = datetime.now()
            # Timestamp = current_time.strftime("%Y%m%d%H%M%S")
            # list1 = [Timestamp, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15]
            # list2 = [Timestamp, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15]
            # dict = {'PARAMETERS': list_var ,'VALUES': listANA}

            # dict = {'values1' : list1, 'values2' : list2 }
            # df = pd.DataFrame(dict)
            dataframe1 = pd.read_csv(fileName)
            dataframe1.to_csv(fileName + '.csv', index=False)
            print('CSV DONE')
            # print(filename) #========================================DELETE============================================================================
            # df.to_csv(r'C:\Users\user\Desktop\DNP\Test_dnp1_' + Timestamp + '.csv', index=False)
            # print('Stored Local') #========================================DELETE============================================================================
            # time.sleep(1)



    except ConnectionError:
        time.sleep(10)
        print('Connection Error caught')
        continue
