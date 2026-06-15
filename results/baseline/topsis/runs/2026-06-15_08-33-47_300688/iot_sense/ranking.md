# TOPSIS Ranking - IoT-Sense (mMTC)

- source_json: `/app/results/storage/baseline/nsga2_rural_macro_28_mcs.json`
- throughput_min: 20.0
- latency_max: 10.0
- cost_max: 50.0
- energy_max: 100.0
- criterion_type: ['max', 'min', 'min', 'min']
- weights: [0.2, 0.2, 0.3, 0.3]
- fallback_to_all_offers: False

 rank  offer_id  topsis_score  throughput  latency      cost    energy  feasible
    1        10      1.000000  289.027616 0.166362  1.179767 15.023577      True
    2        11      0.953645  289.027616 0.166362  2.348779 15.023577      True
    3        14      0.738009  108.905101 0.442793  4.526289 15.023577      True
    4         2      0.655366  254.692880 0.188834 10.998997 15.023577      True
    5         1      0.651988  194.105320 0.247929  1.933003 44.140453      True
    6        17      0.504866  289.027616 0.166362 18.582051 15.023577      True
    7        12      0.430817   82.861323 0.582819  9.412970 44.140453      True
    8         9      0.424203   41.246972 1.178178 10.736471 16.850353      True
