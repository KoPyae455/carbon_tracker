import json
from co2_engine import (
    calculate_emission,
    load_model,
    predict_cluster,
    rule_based_advice,
    save_to_json
)

# ----------------------------
# 1. Load Input JSON
# ----------------------------
with open("user_input.json") as f:
    raw = json.load(f)

# Convert number strings to float
for k in raw:
    if k.endswith('_kg') or k.endswith('_kwh') or k.endswith('_km'):
        raw[k] = float(raw[k])

# ----------------------------
# 2. Calculate Emission
# ----------------------------
total, vector = calculate_emission(raw)

# ----------------------------
# 3. Predict Cluster
# ----------------------------
model = load_model()
cluster = predict_cluster(model, vector)

# ----------------------------
# 4. Generate Advice
# ----------------------------
emissions_dict = {
    'meal': vector[0],
    'electricity': vector[1],
    'vehicle': vector[2],
    'plastic': vector[3]
}
advice = rule_based_advice(emissions_dict)

# ----------------------------
# 5. Save User Log (optional)
# ----------------------------
user_log = {**raw, 'total': total, 'cluster': cluster}
save_to_json(user_log)

# ----------------------------
# 6. Save Output for Frontend
# ----------------------------
with open("output.json", "w") as f:
    json.dump({'total': total, 'cluster': cluster, 'advice': advice}, f)
