# TOPSIS Ranking - IoT-Sense (mMTC)

- source_json: `/app/results/storage/baseline/nsga2_rural_macro_18_mcs.json`
- throughput_min: 20.0
- latency_max: 10.0
- cost_max: 50.0
- energy_max: 100.0
- criterion_type: ['max', 'min', 'min', 'min']
- weights: [0.2, 0.2, 0.3, 0.3]
- fallback_to_all_offers: False

 rank  offer_id  topsis_score  throughput  latency      cost    energy  feasible
    1        19      0.978748  212.890280 0.226000  5.198488 16.227881      True
    2        18      0.959711  200.890455 0.239534  5.593640 16.575210      True
    3         2      0.809122  212.890280 0.226000 10.654699 15.015514      True
    4         4      0.803166  139.048488 0.346453  8.794849 15.015514      True
    5         1      0.705127  211.823766 0.227141 14.482580 15.015514      True
    6        14      0.583812  114.604517 0.420675 17.892864 15.015514      True
    7        22      0.532083   35.799006 1.360084 11.320256 15.015514      True
    8        11      0.453230   35.799006 1.360084 11.395768 25.386399      True
    9        15      0.403798  100.433542 0.480331  9.643439 51.982199      True
   10        13      0.205158   35.799006 1.360084 14.996611 41.664775      True
