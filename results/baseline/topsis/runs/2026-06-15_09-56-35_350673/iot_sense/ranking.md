# TOPSIS Ranking - IoT-Sense (mMTC)

- source_json: `/app/results/storage/baseline/nsga2_rural_macro_18_mcs.json`
- throughput_min: 20.0
- latency_max: 10.0
- cost_max: 50.0
- energy_max: 100.0
- criterion_type: ['max', 'min', 'min', 'min']
- weights: [0.2, 0.2, 0.3, 0.3]
- fallback_to_all_offers: False

 rank  offer_id  topsis_score  throughput  latency      cost    energy  feasible
    1        26      0.898254  170.709538 0.282008  0.602475 15.006958      True
    2        14      0.883635  163.425914 0.294615  0.379717 15.006958      True
    3        28      0.778282  216.764809 0.221951  4.759428 15.006958      True
    4         7      0.570697  216.764809 0.221951  2.926613 35.699470      True
    5        15      0.450914  202.199685 0.237979 13.580561 15.006958      True
    6         3      0.449371  124.989454 0.385581 12.228123 15.006958      True
    7        24      0.357529  127.336265 0.378446 15.597094 17.087559      True
