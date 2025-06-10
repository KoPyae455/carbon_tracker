# 🌍 CO₂ Emission Tracker (Backend Only)

This is the **backend module** for a Carbon Emission Tracking System. It uses:

- ✅ Rule-based CO₂ emission calculation
- ✅ KMeans clustering to group users
- ✅ Smart rule-based advice engine
- ✅ JSON input/output for frontend integration


---

## ⚙️ How It Works

### 1. User enters daily data in a form (HTML UI)

- Meal type + weight
- Electricity usage
- Vehicle type + distance
- Plastic usage

### 2. JavaScript sends input to Flask API (`/predict`)
### 3. Python backend:
- Calculates total CO₂
- Predicts cluster via KMeans
- Generates AI-style advice
- Returns a complete JSON result

### 4. Frontend receives result and displays it instantly.

---

## 🚀 Run the Project

### Step 1: Install Python requirements

```bash
pip install -r requirements.txt
```

### Step 2: Train the KMeans model (if not already trained)
```
cd backend
python train_kmeans.py
```
### Step 3: Start Flask backend
```
python app.py
```

### Step 4: Open frontend/index.html in your browser
➡ Fill the form and click Submit
➡ Result will appear instantly with advice and stats
``` json
{
  "meal_type": "beef",
  "meal_kg": 2,
  "electricity_kwh": 20,
  "vehicle_type": "bus",
  "distance_km": 30,
  "plastic_kg": 1
}
```
### Example Output
``` json
{
  "total": 421.0,
  "cluster": 2,
  "advice": "🥩 Try reducing beef.\n🔌 Turn off unused devices.\n🚌 Use public transport.\n🧴 Reuse plastic containers."
}
```
