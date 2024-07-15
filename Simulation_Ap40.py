import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from tqdm import tqdm

data = pd.read_csv('sampled_5_40.csv')
#create a subset of the first five unique profile ids 

##############################################
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
data.to_csv('Working_shift_AP40_min.csv', index=False)


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
plt.title('Average Kwh vs Adjusted Kwh 40%')
plt.legend()
plt.show()



##############################################################################



rate = 100
#make a cost column which calculates the cost if the off-peak is 0.8*rate and on-peak price is 1.2*rate
data['Cost_40'] = np.where(data['Peak'] == 'Off-Peak', data['New_kWh_40%']*rate*0.8, data['New_kWh_40%']*rate*1.2)
data['Cost_30'] = np.where(data['Peak'] == 'Off-Peak', data['New_kWh_30%']*rate*0.8, data['New_kWh_30%']*rate*1.2)
data['Cost_20'] = np.where(data['Peak'] == 'Off-Peak', data['New_kWh_20%']*rate*0.8, data['New_kWh_20%']*rate*1.2)
data['Cost_10'] = np.where(data['Peak'] == 'Off-Peak', data['New_kWh_10%']*rate*0.8, data['New_kWh_10%']*rate*1.2)
data['Cost'] = np.where(data['Peak'] == 'Off-Peak', data['kWh']*rate*0.8, data['kWh']*rate*1.2)

#print column headings 
print(data.columns)

#box plot for cost for 40% each shift 
data.boxplot(column=['Cost_40', 'Cost_30', 'Cost_20', 'Cost_10', 'Cost'], grid=False)
plt.show()

#average cost for each shift
average_cost_40 = data['Cost_40'].mean()
average_cost_30 = data['Cost_30'].mean()
average_cost_20 = data['Cost_20'].mean()
average_cost_10 = data['Cost_10'].mean()
average_cost = data['Cost'].mean()


#print all the average costs 
print(f"Average cost for 40% shift: {average_cost_40}")
print(f"Average cost for 30% shift: {average_cost_30}")
print(f"Average cost for 20% shift: {average_cost_20}")
print(f"Average cost for 10% shift: {average_cost_10}")
print(f"Average cost for no shift: {average_cost}")



#Create graphs of the new profiles: 
#create graphs for average Kwh, adjusted Kwh for 10%, 20%, 30%, 40% for average hourly profile 
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
plt.title('Average Kwh vs Adjusted Kwh')
plt.legend()
plt.show()

#just plot the adjusted Kwh for 10% shift
plt.plot(adjusted_hourly_profile_10, label='Adjusted Kwh 40%')
plt.xlabel('Hour')
plt.ylabel('Kwh')
plt.title('Adjusted Kwh 40%')
plt.legend()
plt.show()


