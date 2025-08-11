import pandas as pd

"""
csv_data = pd.read_csv('old_airline_data_2023.csv')

print(data.dtypes)
"""

json_data = pd.read_json('new_airline_data_2024.json')

#print(json_data.isnull())

#missing_counts = json_data.isnull().sum()
#print(missing_counts)

"""
rows_with_missing = json_data[json_data.isnull().any(axis=1)]

with open("json_missing_data_log.txt","w") as file:
	file.write(rows_with_missing.to_string())


flights_operated_mean = json_data['Flights Operated'].mean()

flights_operated_mean  = "%.2f" %flights_operated_mean

passengers_carried_mean = json_data['Passengers Carried'].mean()

passengers_carried_mean = "%.2f" %passengers_carried_mean

values = {'Flights Operated': flights_operated_mean, 'Passengers Carried': passengers_carried_mean}

json_data_filled = json_data.fillna(value=values)

# print(json_data_filled)


drop_subset_nan = json_data.dropna(subset=['Flights Operated','Passengers Carried'],how='all')

print(drop_subset_nan)


values_not_to_drop = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

df_filtered_month = json_data[~json_data['Month'].isin(values_not_to_drop)]

print(df_filtered_month)
"""

column_names = list(json_data.columns)

for idx in range(len(column_names)):
	column_names[idx] = column_names[idx].lower().replace(' ','_')
	
json_data.columns = column_names 

print(json_data.columns)