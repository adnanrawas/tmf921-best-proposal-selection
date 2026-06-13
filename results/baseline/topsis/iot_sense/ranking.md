# TOPSIS Ranking - IoT-Sense (mMTC)

- source_json: `/app/results/storage/baseline/nsga2_Rural_macro_18mcs.json`
- throughput_min: 20.0
- latency_max: 10.0
- cost_max: 50.0
- energy_max: 100.0
- criterion_type: ['max', 'min', 'min', 'min']
- weights: [0.2, 0.2, 0.3, 0.3]
- fallback_to_all_offers: False

 rank  offer_id  topsis_score  throughput  latency      cost    energy  feasible
    1         6      0.956671  212.296059 0.226634  9.483674  4.374375      True
    2         7      0.745019  101.990745 0.472961 10.035403  1.154811      True
    3         8      0.706163  101.990745 0.472961 13.790217  1.154811      True
    4         5      0.388345  101.990745 0.472961  8.697267 67.888881      True
    5         2      0.219691  192.021213 0.250627 20.577538 84.878702      True
