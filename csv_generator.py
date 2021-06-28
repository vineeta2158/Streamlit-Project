import datetime
from numpy.core.fromnumeric import size
import pandas as pd
from numpy.random import randint
 
# df (empty dataframe with Timestamp, 5 columns)

dtype = {
    "Timestamp": str,
    "S1": float,
    "S2": float,
    "S3": float,
    "S4": float,
    "S5": float,
}

df = pd.DataFrame(
    columns=[
        "Timestamp",
        "S1",
        "S2",
        "S3",
        "S4",
        "S5",
    ],
    
)

# initialize start date (1 st Jan 2020)

START_DATE = datetime.datetime(2020,1,1,0,0,0)
END = datetime.datetime.now()


# Time Format Function
def time_formatter(time: datetime) -> str:
    time = datetime.datetime.strftime(time,'%Y%m%d%H%M%S')
    return time


    
# loop from start date till today
i=0
time = START_DATE
start = datetime.datetime.now()



def while_alt(time):
    i=0
    while True:
        if time <= END:
            formatted_time = datetime.datetime.strftime(time,'%Y%m%d%H%M%S')
            dict = {
                "index": i,
                "Timestamp": formatted_time,
                "S1": int(randint(low=-1,high=1500)),
                "S2": int(randint(low=-1,high=500)),
                "S3": int(randint(low=-1,high=100)),
                "S4": int(randint(low=-1,high=2000)),
                "S5": int(randint(low=-1,high=1500)),
            }
            yield dict
            time += datetime.timedelta(minutes=1)
            i += 1
        else:
            break

data_record = list(i for i in while_alt(time))


df = df.from_records(data_record,index='index')


end = datetime.datetime.now()
print("\n Time consumed : ", end - start)
        
print(df)


# df -> convert to csv
df.to_csv("./Node06_test.csv",index=False)


