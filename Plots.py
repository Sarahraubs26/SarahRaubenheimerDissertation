
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("sampled_5_10.csv") 
print(df.head())


#create a column for the hour of the day    
df['Datefield'] = pd.to_datetime(df['Datefield'])


#keep the format of the hour of the day as a time 
df['Hour'] = df['Datefield'].dt.hour
df['Hour'] = df['Datefield'].dt.strftime('%H:00')
print(df.head())


#create plots 
fig, axes = plt.subplots(3, 3, figsize=(15, 15))
axes = axes.flatten()
profile_ids = df['ProfileID'].unique()[:9]



#get the average hourly comsumption for each profile
for i, profile_id in enumerate(profile_ids):
    ax = axes[i]  # Get the subplot axes
    profile_data = df[df['ProfileID'] == profile_id]
    hourly_consumption = profile_data.groupby('Hour')['kWh'].mean()
    ax.plot(hourly_consumption.index, hourly_consumption.values)
    ax.set_xlabel('Time (hours)')
    ax.set_ylabel('Consumption (kWh)')
    ax.set_xticks(np.arange(0, 24, 2))
    ax.set_xticklabels([f'{hour:02d}:00' for hour in np.arange(0, 24, 2)], rotation=45)
    ax.grid(False)   
    ax.text(0.02, 0.98, f'({chr(97 + i)})', transform=ax.transAxes, ha='left', va='top', fontsize=12)

plt.tight_layout()
plt.show()



new_df = pd.read_csv("Data_Simulation.csv")
#column headers
print(new_df.columns)

#add a column for the season of the year 
new_df['Datefield'] = pd.to_datetime(new_df['Datefield'])
new_df['Month'] = new_df['Datefield'].dt.month
new_df['Season'] = new_df['Month'].apply(lambda x: 'Winter' if x in [4,5,6] else 'Summer' if x in [1, 2, 3] else '0')
print(new_df.head())
print(new_df.columns)

#list unique values in the season column
print(new_df['Season'].unique())

fig, axes = plt.subplots(1, 2)
axes = axes.flatten()

#get the average hourly consumption for each season
seasons = new_df['Season'].unique()

for i, season in enumerate(seasons):
    ax = axes[i]  # Get the subplot axes
    season_data = new_df[new_df['Season'] == season]
    hourly_consumption = season_data.groupby('Hour')['kWh'].mean()
    ax.plot(hourly_consumption.index, hourly_consumption.values)
    ax.set_xlabel('Time (hours)')
    ax.set_ylabel('Consumption (kWh)')
    ax.set_xticks(np.arange(0, 24, 2))
    ax.set_xticklabels([f'{hour:02d}:00' for hour in np.arange(0, 24, 2)], rotation=45)
    ax.grid(False)   
    ax.set_title(f'Season: {season}')

plt.tight_layout()
plt.show()



#create a graph like the one above for the overall average hourly consumption
fig, ax = plt.subplots()
hourly_consumption = new_df.groupby('Hour')['kWh'].mean()
ax.plot(hourly_consumption.index, hourly_consumption.values)
ax.set_xlabel('Time (hours)')
ax.set_ylabel('Consumption (kWh)')
ax.set_xticks(np.arange(0, 24, 2))
ax.set_xticklabels([f'{hour:02d}:00' for hour in np.arange(0, 24, 2)], rotation=45)
ax.grid(False)
plt.show()









