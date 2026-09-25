# TOPSIS Ranking - IoT-Sense (mMTC)

- source_json: `/app/results/storage/baseline/nsga2_rural_macro_18_mcs.json`
- throughput_min: 20.0
- latency_max: 10.0
- cost_max: 50.0
- energy_max: 30.0
- criterion_type: ['max', 'min', 'min', 'min']
- weights: [0.2, 0.2, 0.3, 0.3]
- fallback_to_all_offers: False

 rank  offer_id  topsis_score  throughput  latency      cost    energy  feasible
    1        19      0.961348  212.890280 0.226000  5.198488 16.227881      True
    2        18      0.939609  200.890455 0.239534  5.593640 16.575210      True
    3         2      0.763454  212.890280 0.226000 10.654699 15.015514      True
    4         4      0.760609  139.048488 0.346453  8.794849 15.015514      True
    5         1      0.638216  211.823766 0.227141 14.482580 15.015514      True
    6        14      0.479763  114.604517 0.420675 17.892864 15.015514      True
    7        22      0.378390   35.799006 1.360084 11.320256 15.015514      True
    8        11      0.274077   35.799006 1.360084 11.395768 25.386399      True
