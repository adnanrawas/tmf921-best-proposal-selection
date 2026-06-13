# TOPSIS Ranking - IoT-Sense (mMTC)

- source_json: `/app/results/storage/baseline/nsga2_high_congestion.json`
- throughput_min: 20.0
- latency_max: 10.0
- cost_max: 50.0
- energy_max: 100.0
- criterion_type: ['max', 'min', 'min', 'min']
- weights: [0.2, 0.2, 0.3, 0.3]
- fallback_to_all_offers: False

 rank  offer_id  topsis_score  throughput  latency      cost    energy  feasible
    1         3      0.893770  353.907269 0.135917  8.644961  1.015598      True
    2         4      0.892324  277.067301 0.173715  5.329240  1.015598      True
    3         1      0.878160  443.338657 0.108453  9.950731  1.015598      True
    4         6      0.849912  383.311854 0.125470 10.938558  1.015598      True
    5         2      0.803534  365.218759 0.131699 13.032165  1.015598      True
    6         5      0.763126  365.218759 0.131699 15.185451  1.015598      True
    7         9      0.631553   78.391939 0.618280 11.237112  1.015598      True
    8         7      0.320121  217.750442 0.221200  7.013793 29.233905      True
