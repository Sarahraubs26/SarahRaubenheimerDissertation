import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tqdm as tqdm

#read in the data 
data_2 = pd.read_csv('sampled_10.csv')

#check the column names
print(data_2.columns)

#remove Percentage_Above_average column
data_2 = data_2.drop(columns=['Percentage_Above_Average'])

#add three columns to the data 
data_2['Above 0.5'] = data_2['kWh'] - 0.5  
data_2['Above 1'] = data_2['kWh'] - 1
data_2['Above 1.5'] = data_2['kWh'] - 1.5

#add three new columns 
#add column, if above above 0.5 > 0 and peak = on-peak, then shift 0.5 = above 0.5 else 0 
data_2['Shift 0.5'] = np.where((data_2['Above 0.5'] > 0) & (data_2['Peak'] == 'On-Peak'), data_2['Above 0.5'], 0)
data_2['Shift 1.0'] = np.where((data_2['Above 1'] > 0) & (data_2['Peak'] == 'On-Peak'), data_2['Above 1'], 0)
data_2['Shift 1.5'] = np.where((data_2['Above 1.5'] > 0) & (data_2['Peak'] == 'On-Peak'), data_2['Above 1.5'], 0)

#add three new columns
data_2['New_kWh_0.5'] = data_2['kWh']
data_2['New_kWh_1.0'] = data_2['kWh']
data_2['New_kWh_1.5'] = data_2['kWh']

data_2['Datefield'] = pd.to_datetime(data_2['Datefield'])
data_2['Date'] = pd.to_datetime(data_2['Date'])



#CREATE THE LOOP FOR 0.5 SHIFT

for profile_id in tqdm.tqdm(data_2['ProfileID'].unique(), desc="054 Loop"):
    profile_df = data_2[data_2['ProfileID'] == profile_id]
    
    # Iterate over unique dates for each profile
    for day in profile_df['Datefield'].dt.date.unique():
        # Create a mask for the current profile ID and date
        day_mask = (data_2['ProfileID'] == profile_id) & (data_2['Datefield'].dt.date == day)
        
        # Iterate over the rows matching the day_mask
        for index, row in data_2.loc[day_mask].iterrows():
            if row['Shift 0.5'] > 0:
                data_2.loc[index, 'New_kWh_0.5'] -= row['Shift 0.5']
                off_peak_rows = data_2[(data_2['Peak'] == 'Off-Peak') & (data_2['Datefield'].dt.date == day)]
                min_kwh_row = off_peak_rows.loc[off_peak_rows['New_kWh_0.5'].idxmin()]
                data_2.loc[min_kwh_row.name, 'New_kWh_0.5'] += row['Shift 0.5']



average_hourly_profile = data_2.groupby('Hour')['kWh'].mean()
print(average_hourly_profile)
adjusted_hourly_profile_05 = data_2.groupby('Hour')['New_kWh_0.5'].mean()

plt.plot(average_hourly_profile, label='Average Kwh')
plt.plot(adjusted_hourly_profile_05, label='Adjusted Kwh 0.5')
plt.xlabel('Hour')
plt.ylabel('Kwh')
plt.title('Average Kwh vs Adjusted Kwh 0.5')
plt.legend()
plt.show()

#print colmumn headings
print(data_2.columns)

#CREATE THE LOOP FOR 1.0 SHIFT
for profile_id in tqdm.tqdm(data_2['ProfileID'].unique(), desc="1.0 Loop"):
    profile_df = data_2[data_2['ProfileID'] == profile_id]
    
    # Iterate over unique dates for each profile
    for day in profile_df['Datefield'].dt.date.unique():
        # Create a mask for the current profile ID and date
        day_mask = (data_2['ProfileID'] == profile_id) & (data_2['Datefield'].dt.date == day)
        
        # Iterate over the rows matching the day_mask
        for index, row in data_2.loc[day_mask].iterrows():
            if row['Shift 1.0'] > 0:
                data_2.loc[index, 'New_kWh_1.0'] -= row['Shift 1.0']
                off_peak_rows = data_2[(data_2['Peak'] == 'Off-Peak') & (data_2['Datefield'].dt.date == day)]
                min_kwh_row = off_peak_rows.loc[off_peak_rows['New_kWh_1.0'].idxmin()]
                data_2.loc[min_kwh_row.name, 'New_kWh_1.0'] += row['Shift 1.0']


average_hourly_profile = data_2.groupby('Hour')['kWh'].mean()
print(average_hourly_profile)
adjusted_hourly_profile_05 = data_2.groupby('Hour')['New_kWh_1.0'].mean()

plt.plot(average_hourly_profile, label='Average Kwh')
plt.plot(adjusted_hourly_profile_05, label='Adjusted Kwh 1.0')
plt.xlabel('Hour')
plt.ylabel('Kwh')
plt.title('Average Kwh vs Adjusted Kwh 1.0')
plt.legend()
plt.show()


#CREATE THE LOOP FOR 1.5 SHIFT

for profile_id in tqdm.tqdm(data_2['ProfileID'].unique(), desc="1.5 Loop"):
    profile_df = data_2[data_2['ProfileID'] == profile_id]
    
    # Iterate over unique dates for each profile
    for day in profile_df['Datefield'].dt.date.unique():
        # Create a mask for the current profile ID and date
        day_mask = (data_2['ProfileID'] == profile_id) & (data_2['Datefield'].dt.date == day)
        
        # Iterate over the rows matching the day_mask
        for index, row in data_2.loc[day_mask].iterrows():
            if row['Shift 1.5'] > 0:
                data_2.loc[index, 'New_kWh_1.5'] -= row['Shift 1.5']
                off_peak_rows = data_2[(data_2['Peak'] == 'Off-Peak') & (data_2['Datefield'].dt.date == day)]
                min_kwh_row = off_peak_rows.loc[off_peak_rows['New_kWh_1.5'].idxmin()]
                data_2.loc[min_kwh_row.name, 'New_kWh_1.5'] += row['Shift 1.5']


average_hourly_profile = data_2.groupby('Hour')['kWh'].mean()
print(average_hourly_profile)
adjusted_hourly_profile_05 = data_2.groupby('Hour')['New_kWh_1.5'].mean()

plt.plot(average_hourly_profile, label='Average Kwh')
plt.plot(adjusted_hourly_profile_05, label='Adjusted Kwh 1.5')
plt.xlabel('Hour')
plt.ylabel('Kwh')
plt.title('Average Kwh vs Adjusted Kwh 1.5')
plt.legend()
plt.show()

data_2.columns 

data_2.to_csv('Working_shift_LLC.csv', index=False)

data_2['Datefield'] = pd.to_datetime(data_2['Datefield'])
data_2['Month'] = data_2['Datefield'].dt.month


monthly_shift_05 = data_2.groupby(['ProfileID', 'Month'])['Shift 0.5'].sum()
average_monthly_shift_05 = monthly_shift_05.groupby('ProfileID').mean()

monthly_shift_10 = data_2.groupby(['ProfileID', 'Month'])['Shift 1.0'].sum()
average_monthly_shift_10 = monthly_shift_10.groupby('ProfileID').mean()

monthly_shift_15 = data_2.groupby(['ProfileID', 'Month'])['Shift 1.5'].sum()
average_monthly_shift_15 = monthly_shift_15.groupby('ProfileID').mean()


average_monthly_LLC = [monthly_shift_05, monthly_shift_10, monthly_shift_15]
labels = ['0.5', '1.0 ', '1.5 ',]

# Create the box plot
plt.figure(figsize=(10, 6))
plt.boxplot(average_monthly_LLC, labels=labels)
plt.title('Average Monthly Shift kWh')
plt.ylabel('Average Monthly Shift (kWh)')
plt.xlabel('Shift threshold (kWh)')
plt.grid(True)

# Show the plot
plt.show()


