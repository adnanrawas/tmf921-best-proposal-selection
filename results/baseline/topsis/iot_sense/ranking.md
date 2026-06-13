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
    1         7      0.745960  101.990745 0.472961 10.035403  1.154811      True
    2         8      0.703545  101.990745 0.472961 13.790217  1.154811      True
    3         5      0.399272  101.990745 0.472961  8.697267 67.888881      True
    4         2      0.246772  192.021213 0.250627 20.577538 84.878702      True
