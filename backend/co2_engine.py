import json
import joblib

# ----------------------------
# 1. Rule-based CO₂ Calculation
# ----------------------------
def calculate_emission(data):
    meal_factors = {
        'beef': 25, 'cheese': 13.5, 'chicken': 6.9,
        'rice': 2.7, 'vegetables': 2.0, 'lentils': 0.9
    }
    vehicle_factors = {
        'petrol': 0.25, 'diesel': 0.3, 'electric': 0.2,
        'bus': 0.1, 'train': 0.04
    }

    meal = data['meal_kg'] * meal_factors.get(data['meal_type'], 2.5)
    electricity = data['electricity_kwh'] * 0.5
    vehicle = data['distance_km'] * vehicle_factors.get(data['vehicle_type'], 0.2)
    plastic = data['plastic_kg'] * 6

    return round(meal + electricity + vehicle + plastic, 2), [meal, electricity, vehicle, plastic]

# ----------------------------
# 2. Rule-based Chat Response (improved)
# ----------------------------
def rule_based_advice(emissions, user_input=None):
    tips = []
    meal_type = user_input['meal_type'] if user_input and 'meal_type' in user_input else None

    # Meal advice (based on both type and amount)
    if emissions['meal'] > 500:
        if meal_type == 'beef':
            tips.append("🥩 Your beef intake is very high. Try reducing beef or switch to lentils for much lower emissions.")
        elif meal_type == 'cheese':
            tips.append("🧀 Too much cheese! Consider reducing cheese intake and opting for vegetables.")
        else:
            tips.append("🍽️ Your meal CO₂ is very high. Try reducing portion size and favoring low-emission foods (lentils, vegetables).")
    elif emissions['meal'] > 300:
        if meal_type in ['beef', 'cheese']:
            tips.append("🥗 Reduce beef/cheese and try more chicken, lentils, or vegetables.")
        else:
            tips.append("🍚 Big portions increase CO₂. Try a bit less next time!")
    else:
        if meal_type in ['lentils', 'vegetables', 'rice']:
            tips.append("✅ Excellent choice of low-CO₂ foods!")
        else:
            tips.append("👍 Good job on meal choices!")

    # Electricity advice
    if emissions['electricity'] > 50:
        tips.append("💡 Turn off unused devices and use LED lighting.")
    else:
        tips.append("🔌 Efficient electricity usage!")

    # Vehicle advice
    if emissions['vehicle'] > 80:
        tips.append("🚗 Try using public transport or carpooling.")
    elif emissions['vehicle'] > 20:
        tips.append("🚌 Combine errands to reduce trips.")
    else:
        tips.append("🚶‍♂️ Excellent transport choice!")

    # Plastic advice
    if emissions['plastic'] > 2:
        tips.append("🧴 Use reusable containers to reduce plastic.")
    else:
        tips.append("♻️ Great job on minimizing plastic use!")

    return "\n".join(tips)

# ----------------------------
# 3. Clustering Prediction (if you ever switch to ML)
# ----------------------------
def load_model():
    model = joblib.load("model.pkl")
    scaler = joblib.load("scaler.pkl")
    return model, scaler

def predict_cluster(model, scaler, vector):
    scaled = scaler.transform([vector])
    return int(model.predict(scaled)[0])

# ----------------------------
# 4. Save User Log (Optional)
# ----------------------------
def save_to_json(user_data, path='data.json'):
    try:
        with open(path, 'r') as f:
            existing = json.load(f)
    except:
        existing = []

    existing.append(user_data)
    with open(path, 'w') as f:
        json.dump(existing, f, indent=2)
