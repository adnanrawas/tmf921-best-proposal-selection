# TOPSIS Ranking - Factory-Ops (URLLC)

- source_json: `/app/results/storage/baseline/nsga2_Rural_macro_18mcs.json`
- throughput_min: 5.0
- latency_max: 2.0
- cost_max: 200.0
- energy_max: 100.0
- criterion_type: ['max', 'min', 'min', 'min']
- weights: [0.2, 0.5, 0.2, 0.1]
- fallback_to_all_offers: False

 rank  offer_id  topsis_score  throughput  latency      cost    energy  feasible
    1         8      0.926173  128.917543 0.058198 23.171782 12.692776      True
    2         6      0.803215  138.743503 0.053910 63.089613 18.564685      True
    3         5      0.650106   34.683077 0.249646 29.413125  1.695016      True
    4         2      0.228980   16.517383 0.770320 33.305358  3.616496      True
    5         7      0.000000   16.517383 0.770320 70.313341 35.149025      True
