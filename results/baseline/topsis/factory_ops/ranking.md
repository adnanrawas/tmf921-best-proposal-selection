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
    1        14      0.991591  143.429316 0.052080   6.544173 16.367199      True
    2        13      0.969523  143.429316 0.052080   6.544173 29.816969      True
    3        15      0.967658  143.429316 0.052080  18.190923 15.014290      True
    4        11      0.914602  131.614895 0.056954  37.278136 15.014290      True
    5         4      0.906007  148.149935 0.050358  26.302178 57.426132      True
    6         2      0.856503  148.149935 0.050358  58.651122 52.437178      True
    7        18      0.849213  143.429316 0.052080  68.674046 15.014290      True
    8        22      0.848506  143.429316 0.052080  60.031217 58.316129      True
    9         1      0.778887  148.149935 0.050358 105.446080 27.804257      True
   10        19      0.055219   27.913329 0.329938  84.921275 52.437178      True
