import pandas as pd
import matplotlib.pyplot as plt
import dask.dataframe as dd
import dask.array as da
import dask.bag as db
import time
from dask.distributed import Client,progress
pd.set_option('display.max_columns', 5500)

df = pd.read_csv("Trips_by_Distance.CSV")
#removes rows with empty cells from the file 
df.dropna(inplace=True)
#remove any potential duplicate rows
df.drop_duplicates(inplace=True)
#converts cells in cell to YYYY/MM/DD format
df["Date"] = pd.to_datetime(df["Date"])

df2 = pd.read_csv("Trips_Full Data.CSV")
df2.dropna(inplace=True)
#remove any potential duplicate rows
df2.drop_duplicates(inplace=True)

n_processors = [10,20]
n_processors_time = {}

df2_grouped = df['Week'].nunique() + df2['Week of Date'].nunique()
def your_computation_code():
    df_grouped = df.groupby(by="Week")["Population Staying at Home"]

    print("the total population of people staying at home from 2018: ",df2["Population Staying at Home"].sum())
    df2_grouped = df['Week'].nunique() + df2['Week of Date'].nunique()

    total_distance_traveled = (
        df2['Trips <1 Mile'].sum() + df2['Trips 1-25 Miles'].sum()+ df2['Trips 25-50 Miles'].sum() +
        df2['Trips 50-100 Miles'].sum() + df2['Trips 100-250 Miles'].sum()+
        df2['Trips 250-500 Miles'].sum() + df2['Trips 500+ Miles'].sum()
        
    )

    # Calculate the average distance traveled per week
    average_distance_per_week = total_distance_traveled / df2_grouped
    print ("How average distance travelled when not at home per week",average_distance_per_week,"miles")

    df_10_25_trips = df[df['Number of Trips 10-25'] > 1000]
    dates_10_25_trips = df_10_25_trips['Date']
    df2_50_100_trips = df2[df2['Trips 50-100 Miles'] > 10000]
    dates_50_100_trips = df2_50_100_trips['Date']



if __name__ == "__main__":

    for processor in n_processors:
        print(f"\n\n\nStarting computation with {processor} processors...\n\n\n")

        client = Client(n_workers=processor)

        start = time.time()

        your_computation_code()

        dask_time = time.time() - start

        n_processors_time[processor] = dask_time

        print(f"\n\n\nTime with {processor} processors: {dask_time} seconds\n\n\n")

        # Close the client after computation
        client.close()

print("\n\n\n", n_processors_time, "\n\n\n")

