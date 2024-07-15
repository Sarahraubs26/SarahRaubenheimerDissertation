#load in the data 
shift_10 = pd.read_csv("Working_shift_AP10_min.csv")
shift_20 = pd.read_csv("Working_shift_AP20_min.csv")
shift_30 = pd.read_csv("Working_shift_AP30_min.csv")
shift_40 = pd.read_csv("Working_shift_AP40_min.csv")

shift_llc = pd.read_csv("Working_shift_LLC.csv")


#first Ap 10% 

#in shift_10 calculate the average New_kWh_10% for when peak is on-peak 
on_peak_10 = shift_10[shift_10['Peak'] == 'On-Peak']
average_on_peak_10 = on_peak_10['New_kWh_10%'].mean()
print(average_on_peak_10)

#do the same calculation for New_new_kWh_20% for when peak is on-peak
on_peak_20 = shift_10[shift_10['Peak'] == 'On-Peak']
average_on_peak_20 = on_peak_20['New_kWh_20%'].mean()   
print(average_on_peak_20)

#do the same calculation for New_new_kWh_30% for when peak is on-peak
on_peak_30 = shift_10[shift_10['Peak'] == 'On-Peak']
average_on_peak_30 = on_peak_30['New_kWh_30%'].mean()
print(average_on_peak_30)

#do the same calculation for New_new_kWh_40% for when peak is on-peak
on_peak_40 = shift_10[shift_10['Peak'] == 'On-Peak']
average_on_peak_40 = on_peak_40['New_kWh_40%'].mean()
print(average_on_peak_40)

#do the same calculation for kWh for when peak is on-peak
on_peak_kWh = shift_10[shift_10['Peak'] == 'On-Peak']
average_on_peak_kWh = on_peak_kWh['kWh'].mean()
print(average_on_peak_kWh)

(0.4602917242078181 - 0.35155238024320506)/0.4602917242078181


#Ap is 20% 
#do the same above for shift_20 
on_peak_10 = shift_20[shift_20['Peak'] == 'On-Peak']
average_on_peak_10 = on_peak_10['New_kWh_10%'].mean()
print(average_on_peak_10)

on_peak_20 = shift_20[shift_20['Peak'] == 'On-Peak']
average_on_peak_20 = on_peak_20['New_kWh_20%'].mean()
print(average_on_peak_20)

on_peak_30 = shift_20[shift_20['Peak'] == 'On-Peak']
average_on_peak_30 = on_peak_30['New_kWh_30%'].mean()
print(average_on_peak_30)

on_peak_40 = shift_20[shift_20['Peak'] == 'On-Peak']
average_on_peak_40 = on_peak_40['New_kWh_40%'].mean()
print(average_on_peak_40)

#do the same for shift_30
on_peak_10 = shift_30[shift_30['Peak'] == 'On-Peak']
average_on_peak_10 = on_peak_10['New_kWh_10%'].mean()
print(average_on_peak_10)

on_peak_20 = shift_30[shift_30['Peak'] == 'On-Peak']
average_on_peak_20 = on_peak_20['New_kWh_20%'].mean()
print(average_on_peak_20)

on_peak_30 = shift_30[shift_30['Peak'] == 'On-Peak']
average_on_peak_30 = on_peak_30['New_kWh_30%'].mean()
print(average_on_peak_30)

on_peak_40 = shift_30[shift_30['Peak'] == 'On-Peak']
average_on_peak_40 = on_peak_40['New_kWh_40%'].mean()
print(average_on_peak_40)


#do the same for shift_40
on_peak_10 = shift_40[shift_40['Peak'] == 'On-Peak']
average_on_peak_10 = on_peak_10['New_kWh_10%'].mean()
print(average_on_peak_10)

on_peak_20 = shift_40[shift_40['Peak'] == 'On-Peak']
average_on_peak_20 = on_peak_20['New_kWh_20%'].mean()
print(average_on_peak_20)

on_peak_30 = shift_40[shift_40['Peak'] == 'On-Peak']
average_on_peak_30 = on_peak_30['New_kWh_30%'].mean()
print(average_on_peak_30)

on_peak_40 = shift_40[shift_40['Peak'] == 'On-Peak']
average_on_peak_40 = on_peak_40['New_kWh_40%'].mean()
print(average_on_peak_40)


#do the same for shift_llc


#in shift_llc calculate the average New_kWh_0.5 for when peak is on-peak 
on_peak_10 = shift_llc[shift_llc['Peak'] == 'On-Peak']
average_on_peak_10 = on_peak_10['New_kWh_0.5'].mean()
print(average_on_peak_10)

#do the same calculation for New_new_kWh_0.6 for when peak is on-peak
on_peak_20 = shift_llc[shift_llc['Peak'] == 'On-Peak']
average_on_peak_20 = on_peak_20['New_kWh_1.0'].mean()
print(average_on_peak_20)

#do the same calculation for New_new_kWh_1.5 for when peak is on-peak
on_peak_30 = shift_llc[shift_llc['Peak'] == 'On-Peak']
average_on_peak_30 = on_peak_30['New_kWh_1.5'].mean()
print(average_on_peak_30)
 

(0.4602917242078181 - 0.3215900665700524)/0.4602917242078181


