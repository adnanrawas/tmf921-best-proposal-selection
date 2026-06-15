# TOPSIS Ranking - Factory-Ops (URLLC)

- source_json: `/app/results/storage/baseline/nsga2_rural_macro_28_mcs.json`
- throughput_min: 5.0
- latency_max: 2.0
- cost_max: 200.0
- energy_max: 100.0
- criterion_type: ['max', 'min', 'min', 'min']
- weights: [0.2, 0.5, 0.2, 0.1]
- fallback_to_all_offers: False

 rank  offer_id  topsis_score  throughput  latency      cost    energy  feasible
    1         1      0.968261 1074.795211 0.006730 11.592057 27.403452      True
    2         2      0.867087  907.091787 0.007982 44.258703 33.967332      True
    3        14      0.818044 1074.795211 0.006730 67.655805 15.001093      True
    4         9      0.817219  519.701658 0.013990 27.251258 15.001093      True
    5        17      0.726777  339.082644 0.021556 10.287078 15.001093      True
    6        12      0.628085  260.125012 0.028232 30.601906 15.001093      True
    7        11      0.470837  216.296913 0.034094 98.184900 49.292153      True
    8        10      0.227122  110.045843 0.068697 22.833577 64.447439      True
