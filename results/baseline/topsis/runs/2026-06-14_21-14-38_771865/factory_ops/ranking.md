# TOPSIS Ranking - Factory-Ops (URLLC)

- source_json: `/app/results/storage/baseline/nsga2_Rural_macro_30_offers_18mcs.json`
- throughput_min: 5.0
- latency_max: 2.0
- cost_max: 200.0
- energy_max: 100.0
- criterion_type: ['max', 'min', 'min', 'min']
- weights: [0.2, 0.5, 0.2, 0.1]
- fallback_to_all_offers: False

 rank  offer_id  topsis_score  throughput  latency       cost    energy  feasible
    1        18      0.944295  335.679816 0.021778  29.082262  0.087107      True
    2        10      0.845506  180.300469 0.041106  20.362798  0.087107      True
    3         4      0.800589  236.918392 0.031060  85.250783 30.374109      True
    4        13      0.783775  149.575300 0.049861  39.417638 53.493269      True
    5        11      0.710988  180.300469 0.041106 142.116923  0.087107      True
    6         3      0.708193  149.575300 0.049861 133.594770  0.087107      True
    7         7      0.680605  107.144576 0.070658 101.402633 93.111716      True
    8         5      0.527018   20.703393 0.510226   6.326576 30.374109      True
    9         1      0.519882   20.703393 0.510226   4.060911 53.493269      True
   10        15      0.506867   20.703393 0.510226  51.279509 11.142008      True
   11        23      0.290472   14.290816 1.090909   4.060911  0.087107      True
   12        20      0.263284   14.290816 1.090909  11.768936 30.374109      True
