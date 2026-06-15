# TOPSIS Ranking - Media-Flex (eMBB)

- source_json: `/app/results/storage/baseline/nsga2_rural_macro_18_mcs.json`
- throughput_min: 60.0
- latency_max: 10.0
- cost_max: 200.0
- energy_max: 100.0
- criterion_type: ['max', 'min', 'min', 'min']
- weights: [0.5, 0.2, 0.2, 0.1]
- fallback_to_all_offers: False

 rank  offer_id  topsis_score  throughput  latency      cost    energy  feasible
    1        28      0.864497  287.024075 0.085126 34.051741 15.080218      True
    2        14      0.562727  181.102307 0.136394  5.321218 45.264476      True
    3        15      0.520423  204.980061 0.120087 87.030559 15.080218      True
    4        26      0.400360  142.963219 0.174188 41.021974 15.080218      True
    5        24      0.335921  142.963219 0.174188 75.180684 15.080218      True
    6         7      0.330967  142.963219 0.174188 79.008084 15.080218      True
    7         3      0.284780   88.512660 0.288415 24.415213 22.462682      True
