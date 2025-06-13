import json
from co2_engine import (
    calculate_emission,
    load_model,
    predict_cluster,
    rule_based_advice,
    save_to_json
)


def cluster_range(total):
    """Return a simple textual range based on total CO₂."""
    if total < 50:
        return "<50kg"
    if total < 200:
        return "50-200kg"
    return ">=200kg"

def main():
    try:
        # Load input
        with open("user_input.json") as f:
            raw = json.load(f)

        for k in raw:
            if k.endswith('_kg') or k.endswith('_kwh') or k.endswith('_km'):
                raw[k] = float(raw[k])

        # Process
        total, vector = calculate_emission(raw)
        model, scaler = load_model()
        cluster = predict_cluster(model, scaler, vector)
        range_text = cluster_range(total)

        emissions_dict = {
            'meal': vector[0],
            'electricity': vector[1],
            'vehicle': vector[2],
            'plastic': vector[3]
        }
        advice = rule_based_advice(emissions_dict)

        user_log = {**raw, 'total': total, 'cluster': cluster, 'range': range_text}
        save_to_json(user_log)

        # Save output
        with open("output.json", "w") as f:
            json.dump({
                'total': total,
                'cluster': cluster,
                'range': range_text,
                'advice': advice
            }, f)
    except Exception as e:
        with open("output.json", "w") as f:
            json.dump({"error": str(e)}, f)

if __name__ == "__main__":
    main()
