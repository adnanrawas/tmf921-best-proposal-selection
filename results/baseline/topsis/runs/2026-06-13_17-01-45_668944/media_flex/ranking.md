# TOPSIS Ranking - Media-Flex (eMBB)

- source_json: `/app/results/storage/baseline/nsga2_high_congestion.json`
- throughput_min: 60.0
- latency_max: 10.0
- cost_max: 200.0
- energy_max: 100.0
- criterion_type: ['max', 'min', 'min', 'min']
- weights: [0.5, 0.2, 0.2, 0.1]
- fallback_to_all_offers: False

 rank  offer_id  topsis_score  throughput  latency      cost    energy  feasible
    1         7      0.879249  911.363193 0.026555 40.696193  0.421566      True
    2         6      0.790588  786.548844 0.030810 30.510227 24.951745      True
    3         5      0.633008  670.488583 0.036204 48.249901 34.611631      True
    4         1      0.397780  406.918467 0.060109 57.071151  0.421566      True
    5         2      0.392528  406.918467 0.060109 40.608695 29.679316      True
    6         3      0.362865  437.829292 0.055788 76.765647 34.611631      True
    7         9      0.319429  223.469341 0.111261 17.789579  0.679199      True
    8         4      0.295594  191.975650 0.130314 19.313645  1.481230      True
