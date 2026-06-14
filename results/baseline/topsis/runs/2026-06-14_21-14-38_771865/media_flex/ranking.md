# TOPSIS Ranking - Media-Flex (eMBB)

- source_json: `/app/results/storage/baseline/nsga2_Rural_macro_30_offers_18mcs.json`
- throughput_min: 60.0
- latency_max: 10.0
- cost_max: 200.0
- energy_max: 100.0
- criterion_type: ['max', 'min', 'min', 'min']
- weights: [0.5, 0.2, 0.2, 0.1]
- fallback_to_all_offers: False

 rank  offer_id  topsis_score  throughput  latency      cost    energy  feasible
    1         5      0.845043  367.955966 0.066136 31.808393 27.824090      True
    2         1      0.746554  288.651514 0.084637  6.799983 35.779525      True
    3         3      0.735296  275.113853 0.088882 26.735721  0.001322      True
    4        15      0.703341  288.651514 0.084637 31.808393 41.443961      True
    5         7      0.657534  242.036991 0.101295 26.735721  0.001322      True
    6        13      0.639961  284.783915 0.085808 75.418728  4.215944      True
    7         4      0.582516  242.036991 0.101295 68.941704  0.001322      True
    8        20      0.568689  242.036991 0.101295 75.692667  1.848060      True
    9        10      0.536898  216.142411 0.113731 54.033892 16.837681      True
   10        18      0.473594  188.540378 0.130858 65.417382  6.807232      True
   11        11      0.271135   90.740494 0.280869 54.033892 16.837681      True
   12        23      0.034672   90.740494 0.280869 68.648397 93.691711      True
