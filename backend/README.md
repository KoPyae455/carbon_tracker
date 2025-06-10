# 🌍 CO₂ Emission Tracker (Backend Only)

This is the **backend module** for a Carbon Emission Tracking System. It uses:

- ✅ Rule-based CO₂ emission calculation
- ✅ KMeans clustering to group users
- ✅ Smart rule-based advice engine
- ✅ JSON input/output for frontend integration

---

## 📁 Folder Structure

carbon_backend/
├── co2_engine.py # Emission, clustering, advice logic
├── train_kmeans.py # Train clustering model (one-time)
├── model.pkl # Saved KMeans model
├── run_prediction.py # Runs full pipeline on input
├── user_input.json # Input (from frontend)
├── output.json # Output (for frontend)
├── data.json # Optional: logs all users
├── README.md


---

## 🧠 How It Works

### 1. Input (user_input.json)

```json
{
  "meal_type": "beef",
  "meal_kg": 2,
  "electricity_kwh": 20,
  "vehicle_type": "bus",
  "distance_km": 30,
  "plastic_kg": 1
}

2. Backend will:
Calculate CO₂ emissions using multipliers

Predict user's cluster group using KMeans

Give personalized rule-based advice

Save everything to output.json
