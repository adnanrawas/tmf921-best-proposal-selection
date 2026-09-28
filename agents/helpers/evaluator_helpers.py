"""Evaluate Verifier-ranked proposals
   using a deterministic QoS satisfaction algorithm."""
#first we need to get the intent for the use case and slice from the master orchestrator
import requests
from copy import deepcopy
from helpers.qos_satisfaction import (
    normalize_utility,
    normalize_cost,
    satisfaction_score,
    combination_function,
)
def fetch_intents(
    intent_url: str,
    timeout: int,
) -> list[dict[str, object]]:
    """Fetch the Intent Owner's use-case intents from the master service."""

    response = requests.get(
        intent_url,
        timeout=timeout,
    )
    # raise an exception if the request in case of a non-200 response like 404 or 500
    response.raise_for_status()

    payload = response.json()# transform the response to a list of dicts
    intents = payload.get("use_cases") 

    if not isinstance(intents, list):
        raise RuntimeError(
            "Intent endpoint must return a list"
        )

    return intents

def get_intent(
    intents: list[dict[str, object]],
    use_case_report: dict[str, object],
) -> dict[str, object]:
    """Return the intent matching a use-case ranking report."""

    use_case_name = str(use_case_report.get("use_case", "")).strip()
    slice_name = str(use_case_report.get("slice", "")).strip()

    if not use_case_name or not slice_name:
        raise ValueError("The ranking report is missing use_case or slice")

    for intent in intents:
        intent_name = str(intent.get("name", "")).strip()
        intent_slice = str(intent.get("slice", "")).strip()

        if (
            intent_name == use_case_name
            and intent_slice == slice_name
        ):
            return intent

    raise ValueError(
        f"Intent not found for '{use_case_name}/{slice_name}'"
    )
####################################################################################
def build_qos_bounds(
    intent: dict[str, object],
) -> dict[str, tuple[float, float]]:
    """Build the lower and upper bounds for each QoS criterion."""

    bounds = {
        "throughput": (
            float(intent["throughput_min"]),
            float(intent["throughput_max"]),
        ),
        "latency": (
            float(intent["latency_min"]),
            float(intent["latency_max"]),
        ),
        "cost": (
            float(intent["cost_min"]),
            float(intent["cost_max"]),
        ),
        "energy": (
            float(intent["energy_min"]),
            float(intent["energy_max"]),
        ),
    }

    for metric, (lower, upper) in bounds.items():
        if upper <= lower:
            raise ValueError(
                f"Invalid {metric} bounds: "
                f"lower={lower}, upper={upper}"
            )

    return bounds
def evaluate_offer_satisfaction(
    offer: dict[str, object],
    bounds: dict[str, tuple[float, float]],
    weights: list[float],
) -> dict[str, object]:
    """Calculate satisfaction for one ranked offer."""

    if len(weights) != 4:
        raise ValueError("Four QoS weights are required")

    throughput_normalized = normalize_utility(
        float(offer["throughput"]),
        bounds["throughput"][0], # lower bound
        bounds["throughput"][1], # uper bound
        "utility",
    )

    latency_normalized = normalize_cost(
        float(offer["latency"]),
        bounds["latency"][0], # lower bound
        bounds["latency"][1], # upper bound
        "cost",
    )

    cost_normalized = normalize_cost(
        float(offer["cost"]),
        bounds["cost"][0], # lower bound
        bounds["cost"][1], # upper bound
        "cost",
    )

    energy_normalized = normalize_cost(
        float(offer["energy"]),
        bounds["energy"][0], # lower bound
        bounds["energy"][1], # upper bound
        "cost",
    )

    normalized_qos = {
        "throughput": throughput_normalized,
        "latency": latency_normalized,
        "cost": cost_normalized,
        "energy": energy_normalized,
    }

    satisfaction = {
        "throughput": satisfaction_score(
            throughput_normalized,
            weights[0],
        ),
        "latency": satisfaction_score(
            latency_normalized,
            weights[1],
        ),
        "cost": satisfaction_score(
            cost_normalized,
            weights[2],
        ),
        "energy": satisfaction_score(
            energy_normalized,
            weights[3],
        ),
    }

    overall_satisfaction = combination_function(
        satisfaction["throughput"],
        weights[0],
        satisfaction["latency"],
        weights[1],
        satisfaction["cost"],
        weights[2],
        satisfaction["energy"],
        weights[3],
    )

    return {
        "normalized_qos": normalized_qos,
        "satisfaction": satisfaction,
        "overall_satisfaction": overall_satisfaction,
    }    
#evaluate the use case rankings against the intent and return a score for each use case
def evaluate_topsis_report(
    topsis_report: dict[str, object],
    intents: list[dict[str, object]],
) -> dict[str, object]:
    """Evaluate every use case in a TOPSIS ranking report."""

    evaluated_report = deepcopy(topsis_report)
    # the loop will iterate through 3 use cases in the report, for each use case it will find the matching intent and evaluate the ranking against the intent
    for use_case_report in evaluated_report["results"]: # looping through each use case in the report
        intent_case = get_intent(
            intents=intents,
            use_case_report=use_case_report,
        )
        bounds = build_qos_bounds(intent_case)

        weights = [
            float(weight)
            for weight in intent_case["weights"]
        ]

        # Inner loop for the offers of the current use case
        for offer in use_case_report["ranking"]:
            evaluation = evaluate_offer_satisfaction(
                offer=offer,
                bounds=bounds,
                weights=weights,
            )

            offer.update(evaluation)

        
    return evaluated_report

def evaluate_vikor_report(
    vikor_report: dict[str, object],
    intents: list[dict[str, object]],
) -> dict[str, object]:
    """Evaluate every use case in a VIKOR ranking report."""

    evaluated_report = deepcopy(vikor_report)

    for use_case_report in evaluated_report["results"]:
        intent_case = get_intent(
            intents=intents,
            use_case_report=use_case_report,
        )

        bounds = build_qos_bounds(intent_case)

        weights = [float(weight) for weight in intent_case["weights"]]

        for offer in use_case_report["ranking"]:
            evaluation = evaluate_offer_satisfaction(
                offer=offer,
                bounds=bounds,
                weights=weights,
            )

            offer.update(evaluation)   
    return evaluated_report    