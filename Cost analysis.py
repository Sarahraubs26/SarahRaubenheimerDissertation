import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data10 = pd.read_csv("Working_shift_AP10_min.csv")
data20 = pd.read_csv("Working_shift_AP20_min.csv")
data30 = pd.read_csv("Working_shift_AP30_min.csv")
data40 = pd.read_csv("Working_shift_AP40_min.csv")


#column headers


#add a cost column to each dataframe
rate = 2.8 #cost of electricity per kWh in 2014

######################## AP = 10 ############################

data10['Cost'] = data10['kWh'] * rate
data10['Cost_10'] = data10['New_kWh_10%'] * rate
data10['Cost_20'] = data10['New_kWh_20%'] * rate
data10['Cost_30'] = data10['New_kWh_30%'] * rate
data10['Cost_40'] = data10['New_kWh_40%'] * rate

data10['Cost_10'] = data10['Cost_10'] * np.where(data10['Peak'] == 'On-peak', 6, 1)
data10['Cost_20'] = data10['Cost_20'] * np.where(data10['Peak'] == 'On-peak', 6, 1)
data10['Cost_30'] = data10['Cost_30'] * np.where(data10['Peak'] == 'On-peak', 6, 1)
data10['Cost_40'] = data10['Cost_40'] * np.where(data10['Peak'] == 'On-peak', 6, 1)


#calculate the average monthly cost for each ProfileID 
data10['Datefield'] = pd.to_datetime(data10['Datefield'])
data10['Month'] = data10['Datefield'].dt.month

monthly_cost = data10.groupby(['ProfileID', 'Month'])['Cost'].sum()
average_monthly_cost = monthly_cost.groupby('ProfileID').mean()

monthly_cost_10 = data10.groupby(['ProfileID', 'Month'])['Cost_10'].sum()
average_monthly_cost_10 = monthly_cost_10.groupby('ProfileID').mean()

monthly_cost_20 = data10.groupby(['ProfileID', 'Month'])['Cost_20'].sum()
average_monthly_cost_20 = monthly_cost_20.groupby('ProfileID').mean()

monthly_cost_30 = data10.groupby(['ProfileID', 'Month'])['Cost_30'].sum()
average_monthly_cost_30 = monthly_cost_30.groupby('ProfileID').mean()

monthly_cost_40 = data10.groupby(['ProfileID', 'Month'])['Cost_40'].sum()
average_monthly_cost_40 = monthly_cost_40.groupby('ProfileID').mean()

#create a boxplot for the average monthly cost 10, 20, 30, 40 on the same plot 

average_monthly_ap_10 = [average_monthly_cost, average_monthly_cost_10, average_monthly_cost_20, average_monthly_cost_30, average_monthly_cost_40]
labels = ['No shift','10 %', '20 %', '30 %', '40 %']

# Create the box plot
plt.figure(figsize=(10, 6))
plt.boxplot(average_monthly_ap_10, labels=labels)
plt.title('Average electricity cost')
plt.ylabel('Average Monthly Cost (R)')
plt.xlabel('Load Shift Factor')
plt.grid(True)

# Show the plot
plt.show()


#column headers
print(data10.columns)

#calculate the average monthly shift for each ProfileID
monthly_shift_10 = data10.groupby(['ProfileID', 'Month'])['Shift_10%'].sum()
average_monthly_shift_10 = monthly_shift_10.groupby('ProfileID').mean()

monthly_shift_20 = data10.groupby(['ProfileID', 'Month'])['Shift_20%'].sum()
average_monthly_shift_20 = monthly_shift_20.groupby('ProfileID').mean()

monthly_shift_30 = data10.groupby(['ProfileID', 'Month'])['Shift_30%'].sum()
average_monthly_shift_30 = monthly_shift_30.groupby('ProfileID').mean()

monthly_shift_40 = data10.groupby(['ProfileID', 'Month'])['Shift_40%'].sum()
average_monthly_shift_40 = monthly_shift_40.groupby('ProfileID').mean()


average_monthly_shift_AP10 = [monthly_shift_10, monthly_shift_20, monthly_shift_30, monthly_shift_40]
labels = ['10 %', '20 %', '30 %', '40 %']

# Create the box plot
plt.figure(figsize=(10, 6))
plt.boxplot(average_monthly_shift_AP10, labels=labels)
plt.title('Average Monthly Shift when AP 10%')
plt.ylabel('Average Monthly Shift (kWh)')
plt.xlabel('Load Shift Factor')
plt.grid(True)
plt.show()



################ AP 20 ############################
data20['Cost_10'] = data20['New_kWh_10%'] * rate
data20['Cost_20'] = data20['New_kWh_20%'] * rate
data20['Cost_30'] = data20['New_kWh_30%'] * rate
data20['Cost_40'] = data20['New_kWh_40%'] * rate

data20['Cost_10'] = data20['Cost_10'] * np.where(data20['Peak'] == 'On-peak', 6, 1)
data20['Cost_20'] = data20['Cost_20'] * np.where(data20['Peak'] == 'On-peak', 6, 1)
data20['Cost_30'] = data20['Cost_30'] * np.where(data20['Peak'] == 'On-peak', 6, 1)
data20['Cost_40'] = data20['Cost_40'] * np.where(data20['Peak'] == 'On-peak', 6, 1)


#calculate the average monthly cost for each ProfileID 
data20['Datefield'] = pd.to_datetime(data20['Datefield'])
data20['Month'] = data10['Datefield'].dt.month

monthly_cost_10_20 = data20.groupby(['ProfileID', 'Month'])['Cost_10'].sum()
average_monthly_cost_10_20 = monthly_cost_10_20.groupby('ProfileID').mean()

monthly_cost_20_20 = data20.groupby(['ProfileID', 'Month'])['Cost_20'].sum()
average_monthly_cost_20_20 = monthly_cost_20_20.groupby('ProfileID').mean()

monthly_cost_30_20 = data20.groupby(['ProfileID', 'Month'])['Cost_30'].sum()
average_monthly_cost_30_20 = monthly_cost_30_20.groupby('ProfileID').mean()

monthly_cost_40_20 = data20.groupby(['ProfileID', 'Month'])['Cost_40'].sum()
average_monthly_cost_40_20 = monthly_cost_40_20.groupby('ProfileID').mean()

#create a boxplot for the average monthly cost 10, 20, 30, 40 on the same plot 

average_monthly_ap_20 = [average_monthly_cost_10_20, average_monthly_cost_20_20, average_monthly_cost_30_20, average_monthly_cost_40_20]
labels = ['10 %', '20 %', '30 %', '40 %']

# Create the box plot
plt.figure(figsize=(10, 6))
plt.boxplot(average_monthly_ap_10, labels=labels)
plt.title('Average Monthly Cost when AP 20%')
plt.ylabel('Average Monthly Cost (R)')
plt.xlabel('Load Shift Factor')
plt.grid(True)

# Show the plot
plt.show()


#column headers
print(data10.columns)

#calculate the average monthly shift for each ProfileID
monthly_shift_10_20 = data20.groupby(['ProfileID', 'Month'])['Shift_10%'].sum()
average_monthly_shift_10_20 = monthly_shift_10_20.groupby('ProfileID').mean()

monthly_shift_20_20 = data20.groupby(['ProfileID', 'Month'])['Shift_20%'].sum()
average_monthly_shift_20_20 = monthly_shift_20_20.groupby('ProfileID').mean()

monthly_shift_30_20 = data20.groupby(['ProfileID', 'Month'])['Shift_30%'].sum()
average_monthly_shift_30_20 = monthly_shift_30_20.groupby('ProfileID').mean()

monthly_shift_40_20 = data20.groupby(['ProfileID', 'Month'])['Shift_40%'].sum()
average_monthly_shift_40_20 = monthly_shift_40_20.groupby('ProfileID').mean()



average_monthly_shift_AP20 = [monthly_shift_10_20, monthly_shift_20_20, monthly_shift_30_20, monthly_shift_40_20]
labels = ['10 %', '20 %', '30 %', '40 %']

# Create the box plot
plt.figure(figsize=(10, 6))
plt.boxplot(average_monthly_shift_AP20, labels=labels)
plt.title('Average Monthly Shift when AP 20%')
plt.ylabel('Average Monthly Shift (kWh)')
plt.xlabel('Load Shift Factor')
plt.grid(True)
plt.show()

################## AP 30 ############################
data30['Cost_10'] = data30['New_kWh_10%'] * rate
data30['Cost_20'] = data30['New_kWh_20%'] * rate
data30['Cost_30'] = data30['New_kWh_30%'] * rate
data30['Cost_40'] = data30['New_kWh_40%'] * rate

data30['Cost_10'] = data30['Cost_10'] * np.where(data30['Peak'] == 'On-peak', 6, 1)
data30['Cost_20'] = data30['Cost_20'] * np.where(data30['Peak'] == 'On-peak', 6, 1)
data30['Cost_30'] = data30['Cost_30'] * np.where(data30['Peak'] == 'On-peak', 6, 1)
data30['Cost_40'] = data30['Cost_40'] * np.where(data30['Peak'] == 'On-peak', 6, 1)

#calculate the average monthly cost for each ProfileID 
data30['Datefield'] = pd.to_datetime(data20['Datefield'])
data30['Month'] = data10['Datefield'].dt.month

monthly_cost_10_30 = data30.groupby(['ProfileID', 'Month'])['Cost_10'].sum()
average_monthly_cost_10_30 = monthly_cost_10_30.groupby('ProfileID').mean()

monthly_cost_20_30 = data30.groupby(['ProfileID', 'Month'])['Cost_20'].sum()
average_monthly_cost_20_30 = monthly_cost_20_30.groupby('ProfileID').mean()

monthly_cost_30_30 = data30.groupby(['ProfileID', 'Month'])['Cost_30'].sum()
average_monthly_cost_30_30 = monthly_cost_30_30.groupby('ProfileID').mean()

monthly_cost_40_30 = data30.groupby(['ProfileID', 'Month'])['Cost_40'].sum()
average_monthly_cost_40_30 = monthly_cost_40_30.groupby('ProfileID').mean()

#create a boxplot for the average monthly cost 10, 20, 30, 40 on the same plot 

average_monthly_ap_20 = [average_monthly_cost_10_30, average_monthly_cost_20_30, average_monthly_cost_30_30, average_monthly_cost_40_30]
labels = ['10 %', '20 %', '30 %', '40 %']

# Create the box plot
plt.figure(figsize=(10, 6))
plt.boxplot(average_monthly_ap_10, labels=labels)
plt.title('Average Monthly Cost when AP 30%')
plt.ylabel('Average Monthly Cost (R)')
plt.xlabel('Load Shift Factor')
plt.grid(True)

# Show the plot
plt.show()

#shift 

monthly_shift_10_30 = data30.groupby(['ProfileID', 'Month'])['Shift_10%'].sum()
average_monthly_shift_10_30 = monthly_shift_10_30.groupby('ProfileID').mean()

monthly_shift_20_30 = data30.groupby(['ProfileID', 'Month'])['Shift_20%'].sum()
average_monthly_shift_20_30 = monthly_shift_20_30.groupby('ProfileID').mean()

monthly_shift_30_30 = data30.groupby(['ProfileID', 'Month'])['Shift_30%'].sum()
average_monthly_shift_30_30 = monthly_shift_30_30.groupby('ProfileID').mean()

monthly_shift_40_30 = data30.groupby(['ProfileID', 'Month'])['Shift_40%'].sum()
average_monthly_shift_40_30 = monthly_shift_40_30.groupby('ProfileID').mean()

average_monthly_shift_AP30 = [monthly_shift_10_30, monthly_shift_20_30, monthly_shift_30_30, monthly_shift_40_30]
labels = ['10 %', '20 %', '30 %', '40 %']


# Create the box plot
plt.figure(figsize=(10, 6))
plt.boxplot(average_monthly_shift_AP10, labels=labels)
plt.title('Average Monthly Shift when AP 20%')
plt.ylabel('Average Monthly Shift (kWh)')
plt.xlabel('Load Shift Factor')
plt.grid(True)
plt.show()

################## AP 40 ############################
data40['Cost_10'] = data40['New_kWh_10%'] * rate
data40['Cost_20'] = data40['New_kWh_20%'] * rate
data40['Cost_30'] = data40['New_kWh_30%'] * rate
data40['Cost_40'] = data40['New_kWh_40%'] * rate

data40['Cost_10'] = data40['Cost_10'] * np.where(data40['Peak'] == 'On-peak', 6, 1)
data40['Cost_20'] = data40['Cost_20'] * np.where(data40['Peak'] == 'On-peak', 6, 1)
data40['Cost_30'] = data40['Cost_30'] * np.where(data40['Peak'] == 'On-peak', 6, 1)
data40['Cost_40'] = data40['Cost_40'] * np.where(data40['Peak'] == 'On-peak', 6, 1)

#calculate the average monthly cost for each ProfileID
data40['Datefield'] = pd.to_datetime(data40['Datefield'])
data40['Month'] = data40['Datefield'].dt.month

monthly_cost_10_40 = data40.groupby(['ProfileID', 'Month'])['Cost_10'].sum()
average_monthly_cost_10_40 = monthly_cost_10_40.groupby('ProfileID').mean()

monthly_cost_20_40 = data40.groupby(['ProfileID', 'Month'])['Cost_20'].sum()
average_monthly_cost_20_40 = monthly_cost_20_40.groupby('ProfileID').mean()

monthly_cost_30_40 = data40.groupby(['ProfileID', 'Month'])['Cost_30'].sum()
average_monthly_cost_30_40 = monthly_cost_30_40.groupby('ProfileID').mean()

monthly_cost_40_40 = data40.groupby(['ProfileID', 'Month'])['Cost_40'].sum()
average_monthly_cost_40_40 = monthly_cost_40_40.groupby('ProfileID').mean()

#create a boxplot for the average monthly cost 10, 20, 30, 40 on the same plot

average_monthly_ap_40 = [average_monthly_cost_10_40, average_monthly_cost_20_40, average_monthly_cost_30_40, average_monthly_cost_40_40]
labels = ['10 %', '20 %', '30 %', '40 %']

# Create the box plot
plt.figure(figsize=(10, 6))
plt.boxplot(average_monthly_ap_40, labels=labels)
plt.title('Average Monthly Cost when AP 40%')
plt.ylabel('Average Monthly Cost (R)')
plt.xlabel('Load Shift Factor')
plt.grid(True)

# Show the plot
plt.show()

#shift
monthly_shift_10_40 = data40.groupby(['ProfileID', 'Month'])['Shift_10%'].sum()
average_monthly_shift_10_40 = monthly_shift_10_40.groupby('ProfileID').mean()

monthly_shift_20_40 = data40.groupby(['ProfileID', 'Month'])['Shift_20%'].sum()
average_monthly_shift_20_40 = monthly_shift_20_40.groupby('ProfileID').mean()

monthly_shift_30_40 = data40.groupby(['ProfileID', 'Month'])['Shift_30%'].sum()
average_monthly_shift_30_40 = monthly_shift_30_40.groupby('ProfileID').mean()

monthly_shift_40_40 = data40.groupby(['ProfileID', 'Month'])['Shift_40%'].sum()
average_monthly_shift_40_40 = monthly_shift_40_40.groupby('ProfileID').mean()

average_monthly_shift_AP40 = [monthly_shift_10_40, monthly_shift_20_40, monthly_shift_30_40, monthly_shift_40_40]
labels = ['10 %', '20 %', '30 %', '40 %']

# Create the box plot
plt.figure(figsize=(10, 6))
plt.boxplot(average_monthly_shift_AP40, labels=labels)
plt.title('Average Monthly Shift when AP 40%')
plt.ylabel('Average Monthly Shift (kWh)')
plt.xlabel('Load Shift Factor')
plt.grid(True)

# Show the plot
plt.show()



#make a dataframe with the average monthly shifts for each AP
average_monthly_shift = [
                            monthly_shift_10_40, monthly_shift_20_40, monthly_shift_30_40, monthly_shift_40_40, 
                            monthly_shift_10_30, monthly_shift_20_30, monthly_shift_30_30, monthly_shift_40_30,
                            monthly_shift_10_20, monthly_shift_20_20, monthly_shift_30_20, monthly_shift_40_20,
                            monthly_shift_10, monthly_shift_20, monthly_shift_30, monthly_shift_40]

combined_df = pd.concat(average_monthly_shift, axis=1)
combined_df.columns = [
    '10%', '20%', '30%', '40%', 
    '10%', '20%', '30%', '40%', 
    '10%', '20%', '30%', '40%', 
    '10%', '20%', '30%', '40%', 
]

colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']
box_colors = [colors[i // 4] for i in range(len(combined_df.columns))]

# Create the box plot
plt.figure(figsize=(15, 8))
box = plt.boxplot(combined_df, patch_artist=True, labels=combined_df.columns)

# Color the boxes
for patch, color in zip(box['boxes'], box_colors):
    patch.set_facecolor(color)

# Create a custom legend
handles = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
labels = ['Ap = 40%', 'Ap = 30%', 'Ap = 20%', 'Ap = 10%']
plt.legend(handles, labels, loc='upper right')

plt.title('Average Monthly Shift Box Plot')
plt.ylabel('Average Monthly Shift (kWh)')
plt.xlabel('Load Shift Factor')
plt.xticks(rotation=45)
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()












#print the first few rows of the dataframe
#create a boxplot for the average monthly shifts for each AP

plt.figure(figsize=(10, 6))
plt.boxplot(average_monthly_shift, labels=labels)
plt.title('Average Monthly Shift when AP 40%')
plt.ylabel('Average Monthly Shift (kWh)')
plt.xlabel('Load Shift Factor')
plt.grid(True)

# Show the plot
plt.show()

