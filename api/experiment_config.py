import os

MCS_INDEX = int(os.getenv("MCS_INDEX", "28"))
SCENARIO_NAME = os.getenv("SCENARIO_NAME", "rural_macro")
NSGA2_FILENAME = f"nsga2_{SCENARIO_NAME}_{MCS_INDEX}_mcs.json"
TOPSIS_FILENAME = f"topsis_{SCENARIO_NAME}_{MCS_INDEX}_mcs.json"
VIKOR_FILENAME = f"vikor_{SCENARIO_NAME}_{MCS_INDEX}_mcs.json"