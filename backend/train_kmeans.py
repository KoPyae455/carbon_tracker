import json
import math
import random
from co2_engine import calculate_emission
import joblib
from ml_utils import SimpleScaler, SimpleKMeans



# ----------------------------
# 1. Load training data from data.json
# ----------------------------
with open("data.json") as f:
    records = json.load(f)

X = []
for entry in records:
    # calculate_emission returns (total, [meal, electricity, vehicle, plastic])
    _, vector = calculate_emission(entry)
    X.append(vector)

# ----------------------------
# 2. Scale features and train KMeans model
# ----------------------------
scaler = SimpleScaler()
X_scaled = scaler.fit_transform(X)

model = SimpleKMeans(n_clusters=3, random_state=0)
model.fit(X_scaled)

# Persist model and scaler
joblib.dump(model, "model.pkl")
joblib.dump(scaler, "scaler.pkl")

# ----------------------------
# 3. Print basic metric
# ----------------------------
labels = model.predict(X_scaled)
inertia = sum(model._dist_sq(x, model.cluster_centers_[label]) for x, label in zip(X_scaled, labels))
print("✅ KMeans trained. Inertia:", round(inertia, 2))
