<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CO₂ Tracker (Backend UI Test)</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">

<div class="container my-5">
    <div class="card shadow-sm">
        <div class="card-body">
            <h2 class="card-title text-center mb-4">🌍 CO₂ Emission Tester</h2>

            <form id="co2-form">
                <div class="row">
                    <div class="col-md-6 mb-3">
                        <label class="form-label">Meal Type</label>
                        <select class="form-select" id="meal_type">
                            <option>beef</option>
                            <option>cheese</option>
                            <option>chicken</option>
                            <option>rice</option>
                            <option>vegetables</option>
                            <option>lentils</option>
                        </select>
                    </div>
                    <div class="col-md-6 mb-3">
                        <label class="form-label">Meal Weight (kg)</label>
                        <input type="number" step="any" class="form-control" id="meal_kg" value="1.2">
                    </div>
                    <div class="col-md-6 mb-3">
                        <label class="form-label">Electricity Used (kWh)</label>
                        <input type="number" step="any" class="form-control" id="electricity_kwh" value="35">
                    </div>
                    <div class="col-md-6 mb-3">
                        <label class="form-label">Vehicle Type</label>
                        <select class="form-select" id="vehicle_type">
                            <option>petrol</option>
                            <option>diesel</option>
                            <option>electric</option>
                            <option>bus</option>
                            <option>train</option>
                        </select>
                    </div>
                    <div class="col-md-6 mb-3">
                        <label class="form-label">Distance Traveled (km)</label>
                        <input type="number" step="any" class="form-control" id="distance_km" value="10">
                    </div>
                    <div class="col-md-6 mb-3">
                        <label class="form-label">Plastic Used (kg)</label>
                        <input type="number" step="any" class="form-control" id="plastic_kg" value="0.3">
                    </div>
                </div>
                <div class="text-center">
                    <button type="submit" class="btn btn-success">Submit</button>
                </div>
            </form>

            <div class="alert alert-info mt-4 d-none" id="result"></div>
        </div>
    </div>
</div>

<script>
    document.getElementById('co2-form').addEventListener('submit', async function(e) {
        e.preventDefault();

        const data = {
            meal_type: document.getElementById('meal_type').value,
            meal_kg: parseFloat(document.getElementById('meal_kg').value),
            electricity_kwh: parseFloat(document.getElementById('electricity_kwh').value),
            vehicle_type: document.getElementById('vehicle_type').value,
            distance_km: parseFloat(document.getElementById('distance_km').value),
            plastic_kg: parseFloat(document.getElementById('plastic_kg').value)
        };

        const res = await fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });

        const result = await res.json();

        const resultDiv = document.getElementById('result');
        let label = result.range || result.cluster_range || ""; // Support both keys for flexibility
        let clusterText = `<strong>Cluster Group:</strong> ${result.cluster}`;
        if (label && label.trim() !== "") {
            clusterText += ` (${label})`;
        }

        resultDiv.innerHTML =
        `<strong>Total CO₂:</strong> ${result.total} kg<br>
        <strong>ML Cluster Group:</strong> ${result.cluster_ml} (${result.cluster_ml_label})<br>
        <strong>Rule-based Cluster Group:</strong> ${result.cluster_rule} (${result.cluster_rule_label})<br>
        <strong>Suggestions:</strong> ${result.advice}`;
        resultDiv.classList.remove('d-none');
    });
</script>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
