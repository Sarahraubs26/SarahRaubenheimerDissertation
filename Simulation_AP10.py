import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from tqdm import tqdm

data = pd.read_csv('sampled_5_10.csv')

#print column names
print(data.columns)


data['Datefield'] = pd.to_datetime(data['Datefield'])
data['Date'] = pd.to_datetime(data['Date'])

#length of the data
print(len(data))

#for 10% shift 
for profile_id in tqdm(data['ProfileID'].unique(), desc="10% Loop"):
    profile_df = data[data['ProfileID'] == profile_id]
    
    # Iterate over unique dates for each profile
    for day in profile_df['Datefield'].dt.date.unique():
        # Create a mask for the current profile ID and date
        day_mask = (data['ProfileID'] == profile_id) & (data['Datefield'].dt.date == day)
        
        # Iterate over the rows matching the day_mask
        for index, row in data.loc[day_mask].iterrows():
            if row['Shift_10%'] > 0:
                data.loc[index, 'New_kWh_10%'] -= row['Shift_10%']
                off_peak_rows = data[(data['Peak'] == 'Off-Peak') & (data['Datefield'].dt.date == day)]
                min_kwh_row = off_peak_rows.loc[off_peak_rows['New_kWh_10%'].idxmin()]
                data.loc[min_kwh_row.name, 'New_kWh_10%'] += row['Shift_10%']


#for 20% shift
for profile_id in tqdm(data['ProfileID'].unique(), desc="20% Loop"):
    profile_df = data[data['ProfileID'] == profile_id]
    
    # Iterate over unique dates for each profile
    for day in profile_df['Datefield'].dt.date.unique():
        # Create a mask for the current profile ID and date
        day_mask = (data['ProfileID'] == profile_id) & (data['Datefield'].dt.date == day)
        
        # Iterate over the rows matching the day_mask
        for index, row in data.loc[day_mask].iterrows():
            if row['Shift_20%'] > 0:
                data.loc[index, 'New_kWh_20%'] -= row['Shift_20%']
                off_peak_rows = data[(data['Peak'] == 'Off-Peak') & (data['Datefield'].dt.date == day)]
                min_kwh_row = off_peak_rows.loc[off_peak_rows['New_kWh_20%'].idxmin()]
                data.loc[min_kwh_row.name, 'New_kWh_20%'] += row['Shift_20%']


#for 30% shift
for profile_id in tqdm(data['ProfileID'].unique(), desc="30% Loop"):
    profile_df = data[data['ProfileID'] == profile_id]
    
    # Iterate over unique dates for each profile
    for day in profile_df['Datefield'].dt.date.unique():
        # Create a mask for the current profile ID and date
        day_mask = (data['ProfileID'] == profile_id) & (data['Datefield'].dt.date == day)
        
        # Iterate over the rows matching the day_mask
        for index, row in data.loc[day_mask].iterrows():
            if row['Shift_30%'] > 0:
                data.loc[index, 'New_kWh_30%'] -= row['Shift_30%']
                off_peak_rows = data[(data['Peak'] == 'Off-Peak') & (data['Datefield'].dt.date == day)]
                min_kwh_row = off_peak_rows.loc[off_peak_rows['New_kWh_30%'].idxmin()]
                data.loc[min_kwh_row.name, 'New_kWh_30%'] += row['Shift_30%']


#for 40% shift
for profile_id in tqdm(data['ProfileID'].unique(), desc="40% Loop"):
    profile_df = data[data['ProfileID'] == profile_id]
    
    # Iterate over unique dates for each profile
    for day in profile_df['Datefield'].dt.date.unique():
        # Create a mask for the current profile ID and date
        day_mask = (data['ProfileID'] == profile_id) & (data['Datefield'].dt.date == day)
        
        # Iterate over the rows matching the day_mask
        for index, row in data.loc[day_mask].iterrows():
            if row['Shift_40%'] > 0:
                data.loc[index, 'New_kWh_40%'] -= row['Shift_40%']
                off_peak_rows = data[(data['Peak'] == 'Off-Peak') & (data['Datefield'].dt.date == day)]
                min_kwh_row = off_peak_rows.loc[off_peak_rows['New_kWh_40%'].idxmin()]
                data.loc[min_kwh_row.name, 'New_kWh_40%'] += row['Shift_40%']


#create a csv file for the new profiles
data.to_csv('Working_shift_AP10_min.csv', index=False)


average_hourly_profile = data.groupby('Hour')['kWh'].mean()
print(average_hourly_profile)
adjusted_hourly_profile_10 = data.groupby('Hour')['New_kWh_10%'].mean()
adjusted_hourly_profile_20 = data.groupby('Hour')['New_kWh_20%'].mean()
adjusted_hourly_profile_30 = data.groupby('Hour')['New_kWh_30%'].mean()
adjusted_hourly_profile_40 = data.groupby('Hour')['New_kWh_40%'].mean()

plt.plot(average_hourly_profile, label='Average Kwh')
plt.plot(adjusted_hourly_profile_10, label='Adjusted Kwh 10%')
plt.plot(adjusted_hourly_profile_20, label='Adjusted Kwh 20%')
plt.plot(adjusted_hourly_profile_30, label='Adjusted Kwh 30%')
plt.plot(adjusted_hourly_profile_40, label='Adjusted Kwh 40%')
plt.xlabel('Hour')
plt.ylabel('Kwh')
plt.title('Average Kwh vs Adjusted Kwh 10%')
plt.legend()
plt.show()

data_10 = pd.read_csv('Working_shift_AP10.csv')
#column names 
print(data_10.columns)

#average values of the last 4 columns
print(data_10[['New_kWh_10%', 'New_kWh_20%', 'New_kWh_30%', 'New_kWh_40%']].mean())
print(data_10[['Shift_10%', 'Shift_20%', 'Shift_30%', 'Shift_40%']].mean())



data_20 = pd.read_csv('Working_shift_AP20.csv')
print(data_20[['New_kWh_10%', 'New_kWh_20%', 'New_kWh_30%', 'New_kWh_40%']].mean())
print(data_20[['Shift_10%', 'Shift_20%', 'Shift_30%', 'Shift_40%']].mean())
























