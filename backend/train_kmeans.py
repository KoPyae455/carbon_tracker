import json
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

from co2_engine import calculate_emission

# Load your logged data
with open("data.json") as f:
    records = json.load(f)

X = [calculate_emission(entry)[1] for entry in records]

# Standard scaling (important for KMeans)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Optimal KMeans model training
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(X_scaled)

# Save sklearn model and scaler
joblib.dump(kmeans, "model.pkl")
joblib.dump(scaler, "scaler.pkl")

print("✅ ML model trained successfully!")
