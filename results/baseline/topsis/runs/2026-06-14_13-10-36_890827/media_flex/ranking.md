# TOPSIS Ranking - Media-Flex (eMBB)

- source_json: `/app/results/storage/baseline/nsga2_Rural_macro_20offers_18mcs.json`
- throughput_min: 60.0
- latency_max: 10.0
- cost_max: 200.0
- energy_max: 100.0
- criterion_type: ['max', 'min', 'min', 'min']
- weights: [0.5, 0.2, 0.2, 0.1]
- fallback_to_all_offers: False

 rank  offer_id  topsis_score  throughput  latency       cost    energy  feasible
    1         1      0.891823  415.977001 0.058406   7.993017 22.018023      True
    2        12      0.772206  419.657560 0.057887  41.466916 33.390506      True
    3        16      0.602009  352.370897 0.069105  86.495240  0.191540      True
    4        19      0.586572  243.219439 0.100792   7.993017 22.018023      True
    5         9      0.552928  240.739927 0.101853  39.764964  0.738756      True
    6         2      0.503896  265.603752 0.092128  76.192058  0.191540      True
    7        11      0.490986  307.141595 0.079455  43.593725 85.412259      True
    8        17      0.481989  210.014748 0.117134  53.524528  0.738756      True
    9        20      0.478541  240.739927 0.101853  53.276765 25.980082      True
   10         3      0.378476  264.120133 0.092656 135.844604  0.191540      True
