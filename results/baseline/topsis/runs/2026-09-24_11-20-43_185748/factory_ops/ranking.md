# TOPSIS Ranking - Factory-Ops (URLLC)

- source_json: `/app/results/storage/baseline/nsga2_rural_macro_28_mcs.json`
- throughput_min: 5.0
- latency_max: 2.0
- cost_max: 200.0
- energy_max: 100.0
- criterion_type: ['max', 'min', 'min', 'min']
- weights: [0.2, 0.5, 0.2, 0.1]
- fallback_to_all_offers: False

 rank  offer_id  topsis_score  throughput  latency       cost    energy  feasible
    1        21      0.911844  225.697537 0.032641  23.484996 15.003693      True
    2         3      0.856009  200.798067 0.036797  31.080389 22.271852      True
    3        27      0.757877  225.697537 0.032641  56.493995 15.003693      True
    4        18      0.734274  126.722786 0.059251   7.026867 47.817900      True
    5         9      0.552570  200.798067 0.036797 115.805492 15.003693      True
    6         5      0.446331   62.334015 0.126542  13.529253 53.240982      True
    7         1      0.441071   56.875722 0.140095   7.026867 22.381151      True
    8        20      0.430259   62.334015 0.126542  24.066398 22.271852      True
    9         8      0.416684   56.875722 0.140095  13.529253 53.240982      True
   10        19      0.416684   56.875722 0.140095  13.529253 53.240982      True
   11        13      0.379157   62.334015 0.126542  38.061309 42.235943      True
   12        15      0.167427   56.875722 0.140095  94.767416 16.566813      True
