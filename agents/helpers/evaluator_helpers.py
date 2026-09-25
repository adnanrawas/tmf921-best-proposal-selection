"""Evaluate Verifier-ranked proposals
   using a deterministic QoS satisfaction algorithm."""
#first we need to get the intent for the use case and slice from the master orchestrator
import requests
from copy import deepcopy

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

    intents = response.json() # transform the response to a list of dicts

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

        # Next:
        # bounds = build_qos_bounds(intent_case)
        # weights = build_weight_mapping(intent_case)
        # evaluate offers

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

        # Next:
        # bounds = build_qos_bounds(intent_case)
        # weights = build_weight_mapping(intent_case)
        # evaluate offers

    return evaluated_report    