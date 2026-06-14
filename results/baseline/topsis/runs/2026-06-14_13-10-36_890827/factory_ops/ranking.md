# TOPSIS Ranking - Factory-Ops (URLLC)

- source_json: `/app/results/storage/baseline/nsga2_Rural_macro_20offers_18mcs.json`
- throughput_min: 5.0
- latency_max: 2.0
- cost_max: 200.0
- energy_max: 100.0
- criterion_type: ['max', 'min', 'min', 'min']
- weights: [0.2, 0.5, 0.2, 0.1]
- fallback_to_all_offers: False

 rank  offer_id  topsis_score  throughput  latency      cost    energy  feasible
    1         9      0.879561  178.903375 0.041437 44.315142  0.096035      True
    2        16      0.843750  177.464666 0.041783 58.310111 14.017554      True
    3        17      0.833303  222.699163 0.033091 72.402863  0.096035      True
    4        11      0.795074  177.464666 0.041783 87.673690  0.096035      True
    5        20      0.733039  222.818822 0.033072 97.483296 63.437960      True
    6         2      0.717723   70.414883 0.110713 50.187087  0.096035      True
    7        19      0.683742   58.256583 0.136397  0.153226 12.049879      True
    8         1      0.679872   58.256583 0.136397  0.153226 18.337566      True
    9        12      0.670426   58.256583 0.136397 22.113850 18.337566      True
   10         3      0.203636   25.348271 0.376575 59.618667  0.096035      True
