# TOPSIS Ranking - Media-Flex (eMBB)

- source_json: `/app/results/storage/baseline/nsga2_rural_macro_28_mcs.json`
- throughput_min: 60.0
- latency_max: 10.0
- cost_max: 200.0
- energy_max: 100.0
- criterion_type: ['max', 'min', 'min', 'min']
- weights: [0.5, 0.2, 0.2, 0.1]
- fallback_to_all_offers: False

 rank  offer_id  topsis_score  throughput  latency      cost    energy  feasible
    1        12      0.824718  825.136058 0.029265 55.620191 15.011417      True
    2        11      0.319518  252.749420 0.096911 23.524204 20.331891      True
    3        17      0.288517  252.749420 0.096911 50.331834 20.331891      True
    4         1      0.210266   63.043994 0.416570  2.004186 28.148524      True
    5         2      0.164610   63.043994 0.416570 19.748632 28.148524      True
    6        10      0.128801   63.043994 0.416570 35.951804 19.380975      True
    7        14      0.114555   63.043994 0.416570 37.563846 28.148524      True
    8         9      0.000000   63.043994 0.416570 67.490676 45.703872      True
