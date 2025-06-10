import json
from co2_engine import (
    calculate_emission,
    load_model,
    predict_cluster,
    rule_based_advice,
    save_to_json
)

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
        model = load_model()
        cluster = predict_cluster(model, vector)

        emissions_dict = {
            'meal': vector[0],
            'electricity': vector[1],
            'vehicle': vector[2],
            'plastic': vector[3]
        }
        advice = rule_based_advice(emissions_dict)

        user_log = {**raw, 'total': total, 'cluster': cluster}
        save_to_json(user_log)

        # Save output
        with open("output.json", "w") as f:
            json.dump({
                'total': total,
                'cluster': cluster,
                'advice': advice
            }, f)
    except Exception as e:
        with open("output.json", "w") as f:
            json.dump({"error": str(e)}, f)

if __name__ == "__main__":
    main()
