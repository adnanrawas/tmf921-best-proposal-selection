# TOPSIS Ranking - Factory-Ops (URLLC)

- source_json: `/app/results/storage/baseline/nsga2_rural_macro_18_mcs.json`
- throughput_min: 5.0
- latency_max: 2.0
- cost_max: 200.0
- energy_max: 100.0
- criterion_type: ['max', 'min', 'min', 'min']
- weights: [0.2, 0.5, 0.2, 0.1]
- fallback_to_all_offers: False

 rank  offer_id  topsis_score  throughput  latency       cost    energy  feasible
    1        18      0.935696  335.679816 0.021778  29.082262  0.087107      True
    2        10      0.841987  180.300469 0.041106  20.362798  0.087107      True
    3         4      0.779814  236.918392 0.031060  85.250783 30.374109      True
    4        13      0.778335  149.575300 0.049861  39.417638 53.493269      True
    5        11      0.680318  180.300469 0.041106 142.116923  0.087107      True
    6         7      0.664173  107.144576 0.070658 101.402633 93.111716      True
    7         5      0.537053   20.703393 0.510226   6.326576 30.374109      True
    8         1      0.530863   20.703393 0.510226   4.060911 53.493269      True
    9        15      0.508172   20.703393 0.510226  51.279509 11.142008      True
   10        23      0.316379   14.290816 1.090909   4.060911  0.087107      True
   11        20      0.291485   14.290816 1.090909  11.768936 30.374109      True
