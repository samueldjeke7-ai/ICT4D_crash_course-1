import pandas as pd

# 1. Load the Excel file
# We use pandas to read the file. It's like opening the file in Excel but with code.
print("Reading floodarchive.xlsx...")
df = pd.read_excel('floodarchive.xlsx')

# 2. Filter for Ivory Coast
# We look at the 'Country' column. 
# .str.strip() removes any accidental hidden spaces at the start or end.
print("Filtering rows for Ivory Coast...")
filtered_data = df[df['Country'].str.strip() == 'Ivory Coast']

# 3. Save the result
# We save the filtered rows to a new CSV file. 
# index=False means we don't add an extra column for row numbers.
output_file = 'ivory_coast_floods.csv'
filtered_data.to_csv(output_file, index=False)

print(f"Success! Saved {len(filtered_data)} rows to {output_file}")
