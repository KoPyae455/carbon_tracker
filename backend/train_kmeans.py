import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import joblib

# ----------------------------
# 1. Sample Training Data
# ----------------------------
# Each entry = [meal_CO₂, electricity_CO₂, vehicle_CO₂, plastic_CO₂]
X = np.array([
    [100, 10, 5, 0.5], [120, 12, 6, 0.6], [130, 11, 4, 0.4],     # Cluster 0 (Eco-friendly)
    [500, 50, 30, 2], [520, 55, 28, 2.2], [510, 52, 32, 1.9],     # Cluster 1 (Moderate)
    [900, 90, 100, 4], [950, 95, 110, 4.5], [920, 85, 105, 3.8]   # Cluster 2 (High CO₂)
])

# ----------------------------
# 2. Train KMeans Model
# ----------------------------
model = KMeans(n_clusters=3, random_state=0)
model.fit(X)

# Save model
joblib.dump(model, "model.pkl")

# ----------------------------
# 3. Print Accuracy Metric
# ----------------------------
labels = model.predict(X)
score = silhouette_score(X, labels)
print("✅ KMeans trained. Silhouette score:", round(score, 2))
