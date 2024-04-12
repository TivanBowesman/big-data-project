import pandas as pd
import matplotlib.pyplot as plt
import dask.dataframe as dd
import dask.array as da
import dask.bag as db

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

distance_categories = {
    '1-25 Miles': ['Trips 1-25 Miles', 'Trips 1-3 Miles', 'Trips 10-25 Miles'],
    '25-100 Miles': ['Trips 25-100 Miles', 'Trips 25-50 Miles', 'Trips 50-100 Miles'],
    '100-500 Miles': ['Trips 100-250 Miles', 'Trips 100+ Miles', 'Trips 250-500 Miles'],
    '500+ Miles': ['Trips 500+ Miles']
}

# Calculate the total number of participants for each distance category
total_participants_by_category = {}
for category, columns in distance_categories.items():
    total_participants_by_category[category] = df2[columns].sum(axis=1).sum()

# Plotting the bar chart
plt.figure(figsize=(10, 7))
plt.bar(total_participants_by_category.keys(), total_participants_by_category.values(), color='skyblue')
plt.title('Number of Participants of Travelers by Distance-Trip Categories')
plt.xlabel('Distance-Trip Category')
plt.ylabel('Total Number of Participants')
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.7)
plt.tight_layout()
plt.show()