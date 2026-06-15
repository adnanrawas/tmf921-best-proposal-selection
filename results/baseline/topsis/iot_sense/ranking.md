# TOPSIS Ranking - IoT-Sense (mMTC)

- source_json: `/app/results/storage/baseline/nsga2_rural_macro_28_mcs.json`
- throughput_min: 20.0
- latency_max: 10.0
- cost_max: 50.0
- energy_max: 100.0
- criterion_type: ['max', 'min', 'min', 'min']
- weights: [0.2, 0.2, 0.3, 0.3]
- fallback_to_all_offers: False

 rank  offer_id  topsis_score  throughput  latency      cost    energy  feasible
    1        20      0.954078  375.656844 0.127947  1.118284 15.013883      True
    2         9      0.824269  350.332784 0.137209  4.394300 15.013883      True
    3        19      0.747581  418.565620 0.114815  6.691320 15.013883      True
    4        21      0.652071  172.198757 0.279562  6.408452 15.013883      True
    5         8      0.651572  204.882472 0.234855  7.089751 15.013883      True
    6        13      0.559003   98.656582 0.489027  7.767875 15.013883      True
    7         3      0.548260  375.656844 0.127947 13.154430 15.013883      True
    8        18      0.543184   48.768514 0.994543  5.215685 15.013883      True
    9        27      0.495961  172.198757 0.279562 11.656637 18.598880      True
   10        15      0.463272  179.868051 0.267608 11.580428 26.953527      True
   11         5      0.413198   21.473107 2.289945  4.597629 15.013883      True
   12         1      0.398211   21.473107 2.289945  5.215685 15.013883      True
