import json
from pathlib import Path

def load_use_cases():
    json_path = Path(__file__).resolve().parent / "intent_config.json"

    with json_path.open("r", encoding="utf-8") as file:
        config = json.load(file)

    return config["DEFAULT_USE_CASES"]