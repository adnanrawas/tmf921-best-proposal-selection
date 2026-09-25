import json
from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd
from pyDecision.algorithm import vikor_method
from algo_mcdm.intent_config import load_use_cases

DEFAULT_USE_CASES  = load_use_cases()

CRITERION_TYPE = ["max", "min", "min", "min"]
VIKOR_RESULT_FILENAME = "vikor_rural_macro_18_mcs.json" # name of the output file for VIKOR results

def _safe_name(value: str) -> str:
    return "".join(ch if ch.isalnum() or ch in ("-", "_") else "_" for ch in value)


def _get_case_folder_name(case_name: str) -> str:
    return case_name.lower().replace("-", "_").replace(" ", "_")


def _extract_solutions(data):
    if isinstance(data, dict):
        try:
            return data["front_0"]["solutions_front_0"]
        except KeyError as exc:
            raise KeyError("Expected keys: data['front_0']['solutions_front_0']") from exc
    return data


def rank_use_cases(data, use_cases=None, weights=None, strategy_coefficient=0.5):
    use_cases = use_cases or DEFAULT_USE_CASES
    default_weights = [1, 1, 1, 1]
    if weights is None:
        weights = default_weights

    solutions = _extract_solutions(data)
    summary_rows = []
    all_results = []

    for case in use_cases:
        slice_name = case["slice"]
        case_name = case["name"]
        case_weights = case.get("weights", weights)

        rows = []
        for solution in solutions:
            thr = float(solution["kpis"]["throughput"][slice_name])
            lat = float(solution["kpis"]["latency_ms"][slice_name])
            cst = float(solution["kpis"]["cost_eur"][slice_name])
            eng = float(solution["kpis"]["energy"][slice_name])

            feasible = (
                thr >= case["throughput_min"]
                and lat <= case["latency_max"]
                and cst <= case["cost_max"]
                and eng <= case["energy_max"]
            )

            rows.append(
                {
                    "offer_id": int(solution["id"]),
                    "throughput": thr,
                    "latency": lat,
                    "cost": cst,
                    "energy": eng,
                    "feasible": feasible,
                }
            )

        df = pd.DataFrame(rows)
        work_df = df[df["feasible"]].copy()
        fallback_to_all = False

        if work_df.empty:
            work_df = df.copy()
            fallback_to_all = True

        dataset = work_df[["throughput", "latency", "cost", "energy"]].to_numpy(dtype=float)

        s, r, q, c_solution = vikor_method(
            dataset,
            case_weights,
            CRITERION_TYPE,
            strategy_coefficient=strategy_coefficient,
            graph=False,
        )
     

        s_arr = np.array(s, dtype=float)
        r_arr = np.array(r, dtype=float)
        q_arr = np.array(q, dtype=float)

        # VIKOR returns [alternative_id, score]
        vikor_order = q_arr[:, 0].astype(int)
        vikor_q_scores = q_arr[:, 1].astype(float)

        s_map = {int(row[0]): float(row[1]) for row in s_arr}
        r_map = {int(row[0]): float(row[1]) for row in r_arr}
        q_map = {int(row[0]): float(row[1]) for row in q_arr}

        # build 1-based positions for the current feasible dataframe
        work_df = work_df.reset_index(drop=True)
        work_df["vikor_alt_id"] = np.arange(1, len(work_df) + 1)

        ranked = work_df.set_index("vikor_alt_id").loc[vikor_order].reset_index()

        ranked["vikor_s"] = ranked["vikor_alt_id"].map(s_map)
        ranked["vikor_r"] = ranked["vikor_alt_id"].map(r_map)
        ranked["vikor_q"] = ranked["vikor_alt_id"].map(q_map)

        ranked["rank"] = np.arange(1, len(ranked) + 1)

        ranked = ranked[
            [
                "rank",
                "offer_id",
                "vikor_q",
                "vikor_s",
                "vikor_r",
                "throughput",
                "latency",
                "cost",
                "energy",
                "feasible",
            ]
        ]

        top1 = ranked.iloc[0]
        summary_rows.append(
            {
                "use_case": case_name,
                "slice": slice_name,
                "feasible_only_mode": not fallback_to_all,
                "top1_offer_id": int(top1["offer_id"]),
                "top1_q": float(top1["vikor_q"]),
                "weights": case_weights,
                "strategy_coefficient": strategy_coefficient,
            }
        )

        all_results.append(
            {
                "use_case": case_name,
                "slice": slice_name,
                "constraints": {
                    "throughput_min": case["throughput_min"],
                    "latency_max": case["latency_max"],
                    "cost_max": case["cost_max"],
                    "energy_max": case["energy_max"],
                },
                "fallback_to_all_offers": fallback_to_all,
                "ranking": ranked.to_dict(orient="records"),
                "weights": case_weights,
                "strategy_coefficient": strategy_coefficient,
                "compromise_solution": np.array(c_solution).tolist(),
            }
        )

    return {
        "summary": summary_rows,
        "results": all_results,
        "weights": weights,
        "criterion_type": CRITERION_TYPE,
        "strategy_coefficient": strategy_coefficient,
    }


def _write_rankings_to_dir(rankings, target_dir, source_json):
    target_dir.mkdir(parents=True, exist_ok=True)

    summary_df = pd.DataFrame(rankings["summary"])
    summary_df.to_csv(target_dir / "summary.csv", index=False)
    summary_df.to_json(target_dir / "summary.json", orient="records", indent=2)

    summary_md = [
        "# VIKOR Use-Case Summary",
        "",
        f"- source_json: `{source_json}`" if source_json else "- source_json: `unknown`",
        f"- criterion_type: {rankings['criterion_type']}",
        f"- strategy_coefficient: {rankings['strategy_coefficient']}",
        "",
        summary_df.to_string(index=False),
        "",
    ]
    (target_dir / "summary.md").write_text("\n".join(summary_md), encoding="utf-8")

    for result in rankings["results"]:
        case_dir = target_dir / _get_case_folder_name(result["use_case"])
        case_dir.mkdir(parents=True, exist_ok=True)

        ranked_df = pd.DataFrame(result["ranking"])
        ranked_df.to_csv(case_dir / "ranking.csv", index=False)
        ranked_df.to_json(case_dir / "ranking.json", orient="records", indent=2)

        constraints = result["constraints"]
        md_lines = [
            f"# VIKOR Ranking - {result['use_case']} ({result['slice']})",
            "",
            f"- source_json: `{source_json}`" if source_json else "- source_json: `unknown`",
            f"- throughput_min: {constraints['throughput_min']}",
            f"- latency_max: {constraints['latency_max']}",
            f"- cost_max: {constraints['cost_max']}",
            f"- energy_max: {constraints['energy_max']}",
            f"- criterion_type: {rankings['criterion_type']}",
            f"- weights: {result['weights']}",
            f"- strategy_coefficient: {result['strategy_coefficient']}",
            f"- fallback_to_all_offers: {result['fallback_to_all_offers']}",
            "",
            ranked_df.to_string(index=False),
            "",
        ]
        (case_dir / "ranking.md").write_text("\n".join(md_lines), encoding="utf-8")


def save_rankings(rankings, output_dir, source_json=None):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    _write_rankings_to_dir(rankings, output_dir, source_json)

    run_id = datetime.now().strftime("%Y-%m-%d_%H-%M-%S_%f")
    run_dir = output_dir / "runs" / _safe_name(run_id)
    _write_rankings_to_dir(rankings, run_dir, source_json)

    payload = {
        "source_json": str(source_json) if source_json else None,
        "output_dir": str(output_dir),
        "run_id": run_id,
        "run_output_dir": str(run_dir),
        "summary": rankings["summary"],
        "results": rankings["results"],
        "weights": rankings["weights"],
        "criterion_type": rankings["criterion_type"],
        "strategy_coefficient": rankings["strategy_coefficient"],
    }

    (output_dir / VIKOR_RESULT_FILENAME).write_text(
        json.dumps(payload, indent=2),
        encoding="utf-8",
    )
    return payload