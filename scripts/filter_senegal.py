import pandas as pd

# 1. Load the Excel file
df = pd.read_excel('data/floodarchive.xlsx')

# 2. Filter for Senegal
# We look for rows where the Country column says "Senegal"
senegal_data = df[df['Country'].str.strip() == 'Senegal']

# 3. Save to CSV
senegal_data.to_csv('data/senegal_floods.csv', index=False)

print(f"Success! Saved {len(senegal_data)} Senegal flood events to senegal_floods.csv")
