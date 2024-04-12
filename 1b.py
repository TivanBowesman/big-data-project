import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Read the CSV files
df = pd.read_csv("Trips_by_Distance.CSV")
df2 = pd.read_csv("Trips_Full Data.CSV")

# Remove rows with empty cells and potential duplicate rows
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
df2.dropna(inplace=True)
df2.drop_duplicates(inplace=True)

# Convert 'Date' column to datetime format with specified format (date only)
df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y %H:%M", errors='coerce')
df2["Date"] = pd.to_datetime(df2["Date"], format="%m/%d/%Y %H:%M", errors='coerce')

# Filtering data for scatter plot
df_10_25_trips = df[df['Number of Trips 10-25'] > 1000]
df2_50_100_trips = df2[df2['Trips 50-100 Miles'] > 10000]

# Plotting the scatter plot
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 2)
plt.scatter(df_10_25_trips['Date'], df_10_25_trips['Number of Trips 10-25'], color='blue', label='10-25 Trips')
plt.scatter(df2_50_100_trips['Date'], df2_50_100_trips['Trips 50-100 Miles'], color='orange', label='50-100 Trips')
plt.xlabel('Date')
plt.ylabel('Number of People')
plt.title('Scatter Plot of People Conducting Trips')
plt.legend()
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()