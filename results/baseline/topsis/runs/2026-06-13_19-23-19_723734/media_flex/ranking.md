# TOPSIS Ranking - Media-Flex (eMBB)

- source_json: `/app/results/storage/baseline/nsga2_Rural_macro_18mcs.json`
- throughput_min: 60.0
- latency_max: 10.0
- cost_max: 200.0
- energy_max: 100.0
- criterion_type: ['max', 'min', 'min', 'min']
- weights: [0.5, 0.2, 0.2, 0.1]
- fallback_to_all_offers: False

 rank  offer_id  topsis_score  throughput  latency      cost   energy  feasible
    1         8      0.629832  301.537478 0.080957 64.339417 3.491759      True
    2         7      0.553248  199.167094 0.123687  3.167133 3.491759      True
    3         2      0.315317  199.167094 0.123687 58.931545 3.491759      True
    4         5      0.000000  175.762081 0.140667 98.870367 3.491759      True
