import json
from co2_engine import (
    calculate_emission,
    load_model,
    predict_cluster,
    rule_based_advice,
    save_to_json
)

def cluster_label(cluster_idx):
    mapping = {0: "Eco-friendly", 1: "Moderate CO₂", 2: "Too much CO₂"}
    return mapping.get(cluster_idx, "")

def cluster_range(total):
    if total < 50:
        return 0
    elif total < 100:
        return 1
    else:
        return 2

def main():
    try:
        with open("user_input.json") as f:
            raw = json.load(f)

        for k in raw:
            if k.endswith('_kg') or k.endswith('_kwh') or k.endswith('_km'):
                raw[k] = float(raw[k])

        total, vector = calculate_emission(raw)

        # ML clustering
        model, scaler = load_model()
        cluster_ml = predict_cluster(model, scaler, vector)
        cluster_ml_label = cluster_label(cluster_ml)

        # Rule-based clustering
        cluster_rule = cluster_range(total)
        cluster_rule_label = cluster_label(cluster_rule)

        emissions_dict = {
            'meal': vector[0],
            'electricity': vector[1],
            'vehicle': vector[2],
            'plastic': vector[3]
        }

        advice = rule_based_advice(emissions_dict, raw)

        user_log = {**raw, 'total': total,
                    'cluster_ml': cluster_ml, 'cluster_ml_label': cluster_ml_label,
                    'cluster_rule': cluster_rule, 'cluster_rule_label': cluster_rule_label}
        save_to_json(user_log)

        with open("output.json", "w") as f:
            json.dump({
                'total': total,
                'cluster_ml': cluster_ml,
                'cluster_ml_label': cluster_ml_label,
                'cluster_rule': cluster_rule,
                'cluster_rule_label': cluster_rule_label,
                'advice': advice
            }, f)
    except Exception as e:
        with open("output.json", "w") as f:
            json.dump({"error": str(e)}, f)

if __name__ == "__main__":
    main()
