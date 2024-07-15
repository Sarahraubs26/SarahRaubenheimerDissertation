import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from tqdm import tqdm



data = pd.read_csv("Working_shift_AP10_min.csv")
data2 = pd.read_csv("2014_A_complete.csv")

#check column headers
print(data.columns)
print(data2.columns)

#remove columns from data 'kWh', 'Peak', 'Percentage_Above_Average' 'Date', 'Load_Shift', 'Shift_10%', 'Shift_20%', 'Shift_30%' 'Shift_40%'
data = data.drop(columns=['Unnamed: 0.1', 'Unnamed: 0', 'Peak', 'Percentage_Above_Average', 'Date', 'Load_Shift', 'Shift_10%', 'Shift_20%', 'Shift_30%', 'Shift_40%'])
print(data.columns)

#add column to data2: New_kWh_10%', 'New_kWh_20%','New_kWh_30%', 'New_kWh_40% mkae then equal to kWh
data2['New_kWh_10%'] = data2['kWh']
data2['New_kWh_20%'] = data2['kWh']
data2['New_kWh_30%'] = data2['kWh']
data2['New_kWh_40%'] = data2['kWh']

data['Hour'] = pd.to_datetime(data['Hour'], format='%H:%M').dt.hour

print(data2.columns)
#remove kWh column from data2
data['Hour'] = pd.to_datetime(merged_data['Hour'], format='%H:%M').dt.hour
merged_data['Hour'] = pd.to_datetime(merged_data['Hour'], format='%H:%M').dt.hour


common_entries = pd.merge(data2, data, on=['ProfileID', 'Unitsread', 'Datefield', 'Hour'], how='inner')
filtered_data = data2[~data2['ProfileID'].isin(common_entries['ProfileID'])]


unique_profile_ids = filtered_data['ProfileID'].unique()
sampled_profile_ids = np.random.choice(unique_profile_ids, size=int(len(unique_profile_ids) * 0.1), replace=False)
filtered_data_10 = filtered_data[filtered_data['ProfileID'].isin(sampled_profile_ids)]


sampled_profile_ids_5 = np.random.choice(unique_profile_ids, size=int(len(unique_profile_ids) * 0.05), replace=False)
filtered_data_5 = filtered_data[filtered_data['ProfileID'].isin(sampled_profile_ids_5)]




#add data and filtered_data by colum
merged_data = pd.concat([filtered_data, data], ignore_index=True)

#check column headers

print(merged_data.columns)
merged_data['Datefield'] = pd.to_datetime(merged_data['Datefield'])
merged_data['Hour'] = pd.to_datetime(merged_data['Hour'], format='%H:%M').dt.hour
merged_data['Hour'] = pd.to_datetime(merged_data['Hour'], format='%H:%M').dt.hour

average_hourly_profile = merged_data.groupby('Hour')['kWh'].mean()
print(average_hourly_profile)
adjusted_hourly_profile_10 = merged_data.groupby('Hour')['New_kWh_10%'].mean()
adjusted_hourly_profile_20 = merged_data.groupby('Hour')['New_kWh_20%'].mean()
adjusted_hourly_profile_30 = merged_data.groupby('Hour')['New_kWh_30%'].mean()
adjusted_hourly_profile_40 = merged_data.groupby('Hour')['New_kWh_40%'].mean()

print(adjusted_hourly_profile_10)

plt.figure(figsize=(10, 6))

plt.plot(average_hourly_profile.index, average_hourly_profile.values, label='Average kWh')
plt.plot(adjusted_hourly_profile_10.index, adjusted_hourly_profile_10.values, label='Adjusted kWh 10%')
plt.plot(adjusted_hourly_profile_20.index, adjusted_hourly_profile_20.values, label='Adjusted kWh 20%')
plt.plot(adjusted_hourly_profile_30.index, adjusted_hourly_profile_30.values, label='Adjusted kWh 30%')
plt.plot(adjusted_hourly_profile_40.index, adjusted_hourly_profile_40.values, label='Adjusted kWh 40%')

plt.title('Hourly kWh Profiles')
plt.xlabel('Hour of the Day')
plt.ylabel('kWh')
plt.legend()
plt.grid(True)

# Show the plot
plt.tight_layout() 
plt.show()



#filter 10 
merged_data_10 = pd.concat([filtered_data_10, data], ignore_index=True)

#check column headers

print(merged_data.columns)
merged_data['Datefield'] = pd.to_datetime(merged_data['Datefield'])
merged_data['Hour'] = pd.to_datetime(merged_data['Hour'], format='%H:%M').dt.hour
merged_data['Hour'] = pd.to_datetime(merged_data['Hour'], format='%H:%M').dt.hour

average_hourly_profile = merged_data_10.groupby('Hour')['kWh'].mean()
print(average_hourly_profile)
adjusted_hourly_profile_10 = merged_data_10.groupby('Hour')['New_kWh_10%'].mean()
adjusted_hourly_profile_20 = merged_data_10.groupby('Hour')['New_kWh_20%'].mean()
adjusted_hourly_profile_30 = merged_data_10.groupby('Hour')['New_kWh_30%'].mean()
adjusted_hourly_profile_40 = merged_data_10.groupby('Hour')['New_kWh_40%'].mean()

print(adjusted_hourly_profile_10)

plt.figure(figsize=(10, 6))

plt.plot(average_hourly_profile.index, average_hourly_profile.values, label='Average kWh')
plt.plot(adjusted_hourly_profile_10.index, adjusted_hourly_profile_10.values, label='Adjusted kWh 10%')
plt.plot(adjusted_hourly_profile_20.index, adjusted_hourly_profile_20.values, label='Adjusted kWh 20%')
plt.plot(adjusted_hourly_profile_30.index, adjusted_hourly_profile_30.values, label='Adjusted kWh 30%')
plt.plot(adjusted_hourly_profile_40.index, adjusted_hourly_profile_40.values, label='Adjusted kWh 40%')

plt.title('Hourly kWh Profiles 33% participation')
plt.xlabel('Hour of the Day')
plt.ylabel('kWh')
plt.legend()
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()



#add data and filtered_data by colum
merged_data_5 = pd.concat([filtered_data_5, data], ignore_index=True)

#check column headers


average_hourly_profile = merged_data_5.groupby('Hour')['kWh'].mean()
print(average_hourly_profile)
adjusted_hourly_profile_10 = merged_data_5.groupby('Hour')['New_kWh_10%'].mean()
adjusted_hourly_profile_20 = merged_data_5.groupby('Hour')['New_kWh_20%'].mean()
adjusted_hourly_profile_30 = merged_data_5.groupby('Hour')['New_kWh_30%'].mean()
adjusted_hourly_profile_40 = merged_data_5.groupby('Hour')['New_kWh_40%'].mean()

print(adjusted_hourly_profile_10)

plt.figure(figsize=(10, 6))

plt.plot(average_hourly_profile.index, average_hourly_profile.values, label='Average kWh')
plt.plot(adjusted_hourly_profile_10.index, adjusted_hourly_profile_10.values, label='Adjusted kWh 10%')
plt.plot(adjusted_hourly_profile_20.index, adjusted_hourly_profile_20.values, label='Adjusted kWh 20%')
plt.plot(adjusted_hourly_profile_30.index, adjusted_hourly_profile_30.values, label='Adjusted kWh 30%')
plt.plot(adjusted_hourly_profile_40.index, adjusted_hourly_profile_40.values, label='Adjusted kWh 40%')

plt.title('Hourly kWh Profiles 50% participation')
plt.xlabel('Hour of the Day')
plt.ylabel('kWh')
plt.legend()
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()





