# TOPSIS Ranking - IoT-Sense (mMTC)

- source_json: `/app/results/storage/baseline/nsga2_Rural_macro_20offers_18mcs.json`
- throughput_min: 20.0
- latency_max: 10.0
- cost_max: 50.0
- energy_max: 100.0
- criterion_type: ['max', 'min', 'min', 'min']
- weights: [0.2, 0.2, 0.3, 0.3]
- fallback_to_all_offers: False

 rank  offer_id  topsis_score  throughput  latency      cost    energy  feasible
    1         1      0.940528  164.248700 0.293135  6.707984  0.289819      True
    2         2      0.899998  128.622403 0.374647  6.707984  0.289819      True
    3        19      0.812217  164.248700 0.293135  4.776215 19.123985      True
    4        12      0.770375  164.248700 0.293135 13.328027  0.077361      True
    5         3      0.746291  124.575686 0.386867 13.700745  0.077361      True
    6        11      0.703667  124.575686 0.386867 15.914772  0.077361      True
    7        20      0.600286   65.474372 0.738796 18.696537  0.289819      True
    8        16      0.458545  124.575686 0.386867 15.914772 41.998976      True
    9         9      0.333710   72.841398 0.663552  5.326473 78.773779      True
   10        17      0.294052  164.248700 0.293135 13.764058 81.357444      True
