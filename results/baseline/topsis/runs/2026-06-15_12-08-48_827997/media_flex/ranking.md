# TOPSIS Ranking - Media-Flex (eMBB)

- source_json: `/app/results/storage/baseline/nsga2_rural_macro_28_mcs.json`
- throughput_min: 60.0
- latency_max: 10.0
- cost_max: 200.0
- energy_max: 100.0
- criterion_type: ['max', 'min', 'min', 'min']
- weights: [0.5, 0.2, 0.2, 0.1]
- fallback_to_all_offers: False

 rank  offer_id  topsis_score  throughput  latency       cost    energy  feasible
    1         5      0.773906  909.895898 0.026523  86.953375 15.100339      True
    2        21      0.626287  747.250213 0.032336 126.122231 15.845970      True
    3        18      0.594194  530.779699 0.045651   4.658422 15.100339      True
    4         3      0.533068  521.733017 0.046450  40.582494 47.452262      True
    5         8      0.513387  521.733017 0.046450  71.795139 15.100339      True
    6         1      0.424187  336.458658 0.072424   4.658422 15.100339      True
    7        15      0.423629  336.458658 0.072424   5.094047 15.100339      True
    8         9      0.349841  326.925904 0.074569  40.830926 36.456470      True
    9        20      0.336760  297.810756 0.081988  28.955730 53.917013      True
   10        19      0.296990  336.458658 0.072424  98.571606 15.100339      True
   11        13      0.279158  186.538704 0.132304  20.177688 39.778886      True
   12        27      0.279143  336.458658 0.072424 119.864382 15.845970      True
