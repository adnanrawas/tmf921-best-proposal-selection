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
    1         1      0.920662  164.511778 0.292664  3.189253  0.018373      True
    2        13      0.904102  164.511778 0.292664  5.301435  0.538451      True
    3        10      0.814950  144.590995 0.333127  9.729422  0.018373      True
    4        20      0.743014  155.122420 0.310437 12.307758  6.215546      True
    5         7      0.706352  215.697391 0.223052 18.045521  0.018373      True
    6        11      0.564122  144.590995 0.333127 12.469533 22.153103      True
    7        23      0.554660   37.722957 1.289759 18.167038  0.018373      True
    8        18      0.543393  130.271010 0.369888 13.805937 22.153103      True
    9         4      0.460695  155.122420 0.310437 16.084369 32.315128      True
   10         5      0.438332  155.122420 0.310437 20.281648 32.315128      True
   11        15      0.279939   20.650471 2.383545 10.627254 22.153103      True
