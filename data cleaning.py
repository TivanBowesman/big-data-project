import pandas as pd
import matplotlib.pyplot as plt
import dask.dataframe as dd
import dask.array as da
import dask.bag as db
import seaborn as sns

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
#Question 1
#1A)
#groups the avg population by week

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

plt.figure(figsize=(10, 6))
plt.bar(['Total Population Staying at Home', 'Average Distance Traveled per Week'], [df2["Population Staying at Home"].sum(), average_distance_per_week], color=['skyblue', 'salmon'])
plt.title("Comparison of Population Staying at Home and Average Distance Traveled")
plt.ylabel("Value")
plt.show()