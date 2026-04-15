import pandas as pd
import json
import math

def haversine(lat1, lon1, lat2, lon2):
    # Radius of the Earth in km
    R = 6371.0
    
    # Convert latitude and longitude to radians
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    
    # Haversine formula
    a = math.sin(dphi / 2)**2 + \
        math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2)**2
    
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

# 1. Load flood data
print("Reading flood data...")
df_floods = pd.read_excel('data/floodarchive.xlsx')
# Keep only Ivory Coast floods with valid coordinates
ivory_coast_floods = df_floods[
    (df_floods['Country'].str.strip() == 'Ivory Coast') & 
    (df_floods['lat'].notnull()) & 
    (df_floods['long'].notnull())
]

# 2. Load health sites
print("Reading health sites...")
with open('data/ivory_coast_health_sites.json', 'r') as f:
    health_data = json.load(f)

at_risk_sites = []
all_sites = health_data.get('elements', [])

print(f"Checking {len(all_sites)} health sites against {len(ivory_coast_floods)} flood events...")

# 3. Analyze each health site
for site in all_sites:
    site_lat = site.get('lat')
    site_lon = site.get('lon')
    
    if site_lat is None or site_lon is None:
        continue
        
    is_at_risk = False
    closest_distance = float('inf')
    
    for _, flood in ivory_coast_floods.iterrows():
        dist = haversine(site_lat, site_lon, flood['lat'], flood['long'])
        
        if dist <= 5.0: # Increased from 1km to 5km
            is_at_risk = True
            if dist < closest_distance:
                closest_distance = dist
    
    if is_at_risk:
        # Add risk info to the site object
        site['risk_info'] = {
            'is_at_risk': True,
            'closest_flood_dist_km': round(closest_distance, 3)
        }
        at_risk_sites.append(site)

# 4. Save results
output_file = 'data/at_risk_health_sites.json'
with open(output_file, 'w') as f:
    json.dump({'elements': at_risk_sites}, f, indent=2)

print(f"Success! Identified {len(at_risk_sites)} health sites at risk (within 5km of a flood).")
print(f"Results saved to {output_file}")
