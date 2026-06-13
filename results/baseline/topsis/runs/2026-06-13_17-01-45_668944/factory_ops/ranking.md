# TOPSIS Ranking - Factory-Ops (URLLC)

- source_json: `/app/results/storage/baseline/nsga2_high_congestion.json`
- throughput_min: 5.0
- latency_max: 2.0
- cost_max: 200.0
- energy_max: 100.0
- criterion_type: ['max', 'min', 'min', 'min']
- weights: [0.2, 0.5, 0.2, 0.1]
- fallback_to_all_offers: False

 rank  offer_id  topsis_score  throughput  latency      cost    energy  feasible
    1         1      0.970176  447.324322 0.016375 47.317504 12.996423      True
    2         4      0.970176  447.324322 0.016375 47.317504 12.996423      True
    3         2      0.930485  447.324322 0.016375 76.910592  2.386480      True
    4         9      0.895404  198.025045 0.037849 44.568683  2.386480      True
    5         5      0.890003  198.025045 0.037849 61.246138  2.386480      True
    6         3      0.886921  198.025045 0.037849 65.784149  2.386480      True
    7         6      0.795941  134.486129 0.056898 75.433462 66.238110      True
    8         7      0.163478   17.378813 1.720498 48.313981  2.386480      True
