# TOPSIS Ranking - Media-Flex (eMBB)

- source_json: `/app/results/storage/baseline/nsga2_rural_macro_18_mcs.json`
- throughput_min: 60.0
- latency_max: 10.0
- cost_max: 200.0
- energy_max: 100.0
- criterion_type: ['max', 'min', 'min', 'min']
- weights: [0.5, 0.2, 0.2, 0.1]
- fallback_to_all_offers: False

 rank  offer_id  topsis_score  throughput  latency      cost    energy  feasible
    1        13      0.874566  281.706479 0.086763  3.079729 15.116882      True
    2        11      0.624609  298.619591 0.081762 33.521313 47.930409      True
    3        15      0.619543  293.905796 0.083097 47.632687 18.709568      True
    4         4      0.615539  293.905796 0.083097 49.238724 15.116882      True
    5        22      0.599142  197.491131 0.124765  1.648619 15.116882      True
    6         1      0.562208  293.905796 0.083097 58.200156 15.116882      True
    7        18      0.520978  309.926877 0.078729 71.632976 15.116882      True
    8        19      0.518778  293.905796 0.083097 66.561574 15.116882      True
    9        14      0.407657  281.706479 0.086763 66.783468 51.573962      True
   10         2      0.265353  195.584817 0.126015 87.001922 15.116882      True
