# import pandas (pipenv install pandas locally)
import pandas

# Assign URL to csv_url
csv_url = 'https://sportsdatasolutionsacademy.s3.eu-west-2.amazonaws.com/data/swimming_psb_data.csv'

# Read CSV
csv_df = pandas.read_csv(csv_url)

# Filter British Athletes and drop any duplicate rows
csv_df = csv_df[csv_df['c_NOC'] == 'Australia'].drop_duplicates()

# Display DataFrame
print('#AUS')
print(csv_df.head())

# Assign URL to json_url
json_url = 'https://sportsdatasolutionsacademy.s3.eu-west-2.amazonaws.com/data/swimming_psb_data.json'

# Read JSON
json_df = pandas.read_json(json_url, orient='records')

# Filter British Athletes and drop any duplicate rows
json_df = json_df[json_df['c_NOC'] == 'Great Britain'].drop_duplicates()

# Display DataFrame
print('#GB')
print(json_df.head())

# Write To CSV
print('#Write CSV')
json_df.to_csv(r'gb_swimming_psb_data.csv', index=False)

# Write To JSON
print('#Write JSON')
csv_df.to_json(r'gb_swimming_psb_data.json', orient='records')