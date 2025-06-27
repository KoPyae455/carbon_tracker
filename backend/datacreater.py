import json

# 1. Load your data
with open("data.json") as f:
    data = json.load(f)

# 2. Filter out records with extreme (unrealistic) values
filtered = [
    d for d in data
    if (
        d.get('meal_kg', 0) < 20 and
        d.get('electricity_kwh', 0) < 1000 and
        d.get('distance_km', 0) < 10000 and
        d.get('plastic_kg', 0) < 100
    )
]

# 3. Save cleaned data as data_clean.json
with open("data_clean.json", "w") as f:
    json.dump(filtered, f, indent=2)

print(f"Original: {len(data)} records; Cleaned: {len(filtered)} records.")
