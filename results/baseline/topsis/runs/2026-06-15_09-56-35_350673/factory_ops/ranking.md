# TOPSIS Ranking - Factory-Ops (URLLC)

- source_json: `/app/results/storage/baseline/nsga2_rural_macro_18_mcs.json`
- throughput_min: 5.0
- latency_max: 2.0
- cost_max: 200.0
- energy_max: 100.0
- criterion_type: ['max', 'min', 'min', 'min']
- weights: [0.2, 0.5, 0.2, 0.1]
- fallback_to_all_offers: False

 rank  offer_id  topsis_score  throughput  latency       cost    energy  feasible
    1         3      0.983712  402.913900 0.018097   7.551091 20.363828      True
    2        24      0.964834  347.767142 0.021010   7.551091 20.363828      True
    3        26      0.933093  284.012999 0.025814  12.014584 15.003402      True
    4        15      0.820847  151.396517 0.049239  62.874259 16.861949      True
    5         7      0.810942  148.972183 0.050070  59.794998 42.124879      True
    6        28      0.749427  151.396517 0.049239 116.004794 16.861949      True
    7        14      0.150098   14.264414 1.096569  52.225857 20.363828      True
