# VIKOR Ranking - IoT-Sense (mMTC)

- source_json: `/app/results/storage/baseline/nsga2_rural_macro_18_mcs.json`
- throughput_min: 20.0
- latency_max: 10.0
- cost_max: 50.0
- energy_max: 30.0
- criterion_type: ['max', 'min', 'min', 'min']
- weights: [0.2, 0.2, 0.3, 0.3]
- strategy_coefficient: 0.5
- fallback_to_all_offers: False

 rank  offer_id  vikor_q  vikor_s  vikor_r  throughput  latency      cost    energy  feasible
    1        19 0.000000 0.035070 0.035070  212.890280 0.226000  5.198488 16.227881      True
    2        18 0.040730 0.070395 0.045118  200.890455 0.239534  5.593640 16.575210      True
    3         4 0.189458 0.189627 0.084991  139.048488 0.346453  8.794849 15.015514      True
    4         2 0.235015 0.128944 0.128944  212.890280 0.226000 10.654699 15.015514      True
    5         1 0.462356 0.220812 0.219406  211.823766 0.227141 14.482580 15.015514      True
    6        22 0.625302 0.544673 0.200000   35.799006 1.360084 11.320256 15.015514      True
    7        14 0.752815 0.445332 0.300000  114.604517 0.420675 17.892864 15.015514      True
    8        11 1.000000 0.846457 0.300000   35.799006 1.360084 11.395768 25.386399      True
