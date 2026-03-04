import pandas as pd
import json

# Load the JSON telemetry data
with open('daikibo-telemetry-data.json', 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.json_normalize(data)

# Assume there is a 'status' column and columns 'factory' and 'device_type'
# Create calculated measure 'Unhealthy': 10 mins for every unhealthy status
df['Unhealthy'] = df['status'].apply(lambda x: 10 if x.lower() == 'unhealthy' else 0)

# Export to CSV for Tableau import
df.to_csv('daikibo_telemetry_prepared.csv', index=False)

print("Prepared telemetry data saved to 'daikibo_telemetry_prepared.csv'")
