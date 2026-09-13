import json
import logging
import os
import re
import time
import traceback
import uuid
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from operator import add
from pathlib import Path
from typing import Annotated, TypedDict


import requests
from flask import Flask, jsonify, request
from langgraph.graph import END, START, StateGraph
from tenacity import retry, stop_after_attempt, wait_exponential
from langchain_core.messages import AIMessage,AnyMessage,HumanMessage,SystemMessage
from langgraph.graph.message import add_messages
from helpers.observer_helpers import build_observer_system_prompt,build_observer_user_prompt,build_llm_request,get_latest_report,

class A3State(TypedDict, total=False):
    intent: dict
    current_round: int
    max_rounds: int # maximum number of rounds for the consensus process
    saved_record_path: str #saving the path to the record of the experiment for future reference and analysis
    feasible_offers: list[dict[str, object]]
    topsis_rankings: dict[str, object]
    vikor_rankings: dict[str, object]
    previous_round_reports: dict[str, dict[str, object]]
    # saw_rankings: dict[str, list[dict]] # to be implemented
    messages: Annotated[list[AnyMessage], add_messages]
    topsis_observer_outputs: Annotated[list[dict[str, object]], add]
    vikor_observer_outputs: Annotated[list[dict[str, object]], add]
    observer_outputs: dict[str, list[dict[str, object]]]
    validation_results: dict[str, dict] #to be discovered and implemented i should add the metris that i have 
    consensus_results: dict[str, dict[str, object]]
    preference_metrics: dict[str,dict[str, object]] #to be implimaented afterr the consensus and validation i should add the metrics that i have to match in the user preferences

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
DEBUG_MODE = os.getenv("DEBUG", "false").lower() == "true"
#####################################################
#variables     
MASTER_URL = "http://master:5000/provider/openrouter"
# MODEL_NAME = "deepseek/deepseek-r1"
MODEL_NAME = os.getenv("MODEL_NAME", "nvidia/llama-3.1-nemotron-70b-instruct") 
LLM_TIMEOUT = int(os.getenv("LLM_TIMEOUT",120))  
JOBS_DIR=Path("/app/output/agent_jobs")
JOBS_DIR.mkdir(parents=True, exist_ok=True)
EXECUTOR = ThreadPoolExecutor(max_workers=2)
LLM_TIMEOUT = int(os.getenv("LLM_TIMEOUT", 120))
####################################################
#endpoints
######################################################################################################
MASTER_TOPSIS_URL = os.getenv("MASTER_TOPSIS_URL", "http://master:5000/ranking/topsis")
MASTER_VIKOR_URL = os.getenv("MASTER_VIKOR_URL", "http://master:5000/ranking/vikor")
########################################getting VIKOR rankings from the service##########################################################
def fetch_vikor_rankings() -> dict[str, object]:
    try:
        response = requests.get(
            MASTER_VIKOR_URL,
            params={"save": "true"},
            timeout=LLM_TIMEOUT,
        )
        response.raise_for_status()
        payload = response.json()
    except requests.exceptions.Timeout as exc:
        raise RuntimeError(
            "VIKOR service timed out"
        ) from exc
    except requests.exceptions.ConnectionError as exc:
        raise RuntimeError(
            "Could not connect to VIKOR service"
        ) from exc
    except requests.exceptions.HTTPError as exc:
        raise RuntimeError(
            f"VIKOR returned an HTTP error: {exc}"
        ) from exc
    except ValueError as exc:
        raise RuntimeError(
            "VIKOR returned invalid JSON"
        ) from exc
    if not isinstance(payload, dict):
        raise RuntimeError(
            "VIKOR response must be a JSON object"
        )
    return payload
#########################################################################################################
############################################ fetch_ranking##############################################
def fetch_topsis_rankings() -> dict[str, object]:
    try:
        response = requests.get(
            MASTER_TOPSIS_URL,
            params={"save": "true"},
            timeout=LLM_TIMEOUT,
        )
        response.raise_for_status()
        payload = response.json()
    except requests.exceptions.Timeout as exc:
        raise RuntimeError(
            "TOPSIS service timed out"
        ) from exc
    except requests.exceptions.ConnectionError as exc:
        raise RuntimeError(
            "Could not connect to TOPSIS service"
        ) from exc
    except requests.exceptions.HTTPError as exc:
        raise RuntimeError(
            f"TOPSIS returned an HTTP error: {exc}"
        ) from exc
    except ValueError as exc:
        raise RuntimeError(
            "TOPSIS returned invalid JSON"
        ) from exc
    if not isinstance(payload, dict):
        raise RuntimeError(
            "TOPSIS response must be a JSON object"
        )

    return payload
#########################################################################################
def load_rankings_node(state: A3State) -> A3State:
    """Load TOPSIS and VIKOR rankings from the master service."""

    topsis_rankings = fetch_topsis_rankings()
    vikor_rankings = fetch_vikor_rankings()

    if topsis_rankings.get("status") != "success":
        raise RuntimeError(
            f"TOPSIS service failed: "
            f"{topsis_rankings.get('error', 'unknown error')}"
        )

    if vikor_rankings.get("status") != "success":
        raise RuntimeError(
            f"VIKOR service failed: "
            f"{vikor_rankings.get('error', 'unknown error')}"
        )
    state_update = {
    "topsis_rankings": topsis_rankings,
    "vikor_rankings": vikor_rankings,
    "current_round": 0,
    "max_rounds": state.get("max_rounds", 3),
}
    # print(state_update, flush=True)
    return state_update

# #########################################################################################
# def topsis_observer_node(state: A3State) -> A3State:
    # """Run TOPSIS as a tool and interpret its result."""

    # GET the user intent and feasible offers from state.
    # GET the saved TOPSIS ranking for each slice from state.

    # CREATE a SystemMessage defining:
    #     - The TOPSIS observer role.
    #     - Interpretation rules.
    #     - Restriction against changing algorithm results.
    
    # CREATE a HumanMessage containing:
    #     - Read The user intent and KPI preferences.
    #     - Read The rank offers for every slice.
    #     - Ask the observer to interpret the TOPSIS ranking and provide a structured report.

    #     SEND the SystemMessage and HumanMessage to the cloud LLM

    #     RECEIVE and save  an AIMessage containing the TOPSIS tool call.
    #     CHECK that the AIMessage contains a valid tool call.
    #     EXECUTE the TOPSIS tool using the supplied offers and weights.
    #     CREATE a ToolMessage containing:
    #         - Ranked offers.
    #         - TOPSIS scores.
    #         - Tool name.
    #         - Tool-call ID matching the AIMessage.

    #     IF the tool call fails:
    #         - Save the error.
    #         - Do not ask the observer to interpret missing results.

    #     SEND the complete message sequence back to the cloud LLM:
    #         - SystemMessage.
    #         - HumanMessage.
    #         - AIMessage containing the tool call.
    #         - ToolMessage containing the tool result.

    #     RECEIVE the interpretation as a final AIMessage.

    #     SAVE all messages in state["messages"].

    #     SAVE the raw ranking under:
    #         state["topsis_rankings"][slice_name].

    #     SAVE the structured report in state["observer_outputs"],
    #     including the observer name, algorithm, slice, and analysis.

    # RETURN messages, TOPSIS rankings, and observer outputs.

    # pass
##############################################################
##############################################################
def topsis_observer_node(state: A3State) -> A3State:
    """Interpret the existing TOPSIS rankings."""
    round_number = state.get("current_round", 0) #getting the current round number from the state, defaulting to 0 if not present
    topsis_response = state.get("topsis_rankings")
    if not isinstance(topsis_response, dict):
        raise RuntimeError(
            "TOPSIS rankings are missing from state"
        )
    topsis_results = topsis_response.get("results")
    if not isinstance(topsis_results, list):
        raise RuntimeError(
            "TOPSIS response does not contain a results list"
        )

    latest_vikor_report = get_latest_report( #get the latest report from the vikor observer outputs in the state
    state.get("vikor_observer_outputs", [])
)
    system_prompt = build_observer_system_prompt(
    algorithm="TOPSIS",
    ranking_rule=(
    "In TOPSIS, a higher score represents a better result."),
    score_values="TOPSIS score")

    user_prompt = build_observer_user_prompt( #user prompt helper
    algorithm="TOPSIS",
    ranking_results=topsis_results)
    request_data = build_llm_request(
    system_prompt= system_prompt,
    user_prompt= user_prompt,
    message_history= state.get("topsis_observer_outputs", [])
    model_name= MODEL_NAME)

    result = call_llm(request_data)
    return {
            "topsis_observer_outputs": [
                {
                    "observer": "topsis_observer",
                    "algorithm": "TOPSIS",
                    "round": round_number, # i should update the round number for each observer output to reflect the current round of evaluation
                    "response": result,
                    "latest_vikor_report": get_latest_report(state.get("vikor_observer_outputs", []))
                }
            ]
           }
#######################################################################
#vikor observer node
def vikor_observer_node(state: A3State) -> A3State:
    """Interpret the existing VIKOR rankings."""
    round_number = state.get("current_round", 0) 
    vikor_response = state.get("vikor_rankings")

    if not isinstance(vikor_response, dict):
        raise RuntimeError(
            "VIKOR rankings are missing from state"
        )
    vikor_results = vikor_response.get("results")
    if not isinstance(vikor_results, list):
        raise RuntimeError(
            "VIKOR response does not contain a results list")
    system_prompt = build_observer_system_prompt(
    algorithm="VIKOR",
    ranking_rule=(
    "In VIKOR, a lower Q value represents "
    "a better compromise result."),
    score_values="Q, S, or R value")

    user_prompt = build_observer_user_prompt(
    algorithm="VIKOR",
    ranking_results=vikor_results)

    request_data = build_llm_request(
    system_prompt=system_prompt,
    user_prompt=user_prompt,
    message_history=state.get("vikor_observer_outputs", []),
    model_name=MODEL_NAME)

    result = call_llm(request_data)

    return {
        "vikor_observer_outputs": [
            {
                "observer": "vikor_observer",
                "algorithm": "VIKOR",
                "round": round_number,
                "response": result,
                "latest_topsis_report": get_latest_report(state.get("topsis_observer_outputs", [])),
            }
                 # adding the latest

        ]
       }
       
    
              
    
#################################################################################
#saving the results of the observers and the consensus in a record for future reference and analysis
A3_RESULTS_DIR = Path(
    "/app/results/storage/experiments/a3"
)

A3_RESULT_FILENAME = (
    "a3_rural_macro_28_mcs.json"
)

A3_RESULT_FILE = (
    A3_RESULTS_DIR /
    A3_RESULT_FILENAME
)
#################################################################################
def round_controller_node(
    state: A3State,
) -> Command[
    Literal[
        "topsis_observer",
        "vikor_observer",
        "save_record",
    ]
]:
    """RepeatRepeattoon or save after the final round."""
    current_round = state["current_round"]
    max_rounds = state["max_rounds"]

    if current_round < max_rounds - 1:
         observer_history = {
        "topsis": state.get(
            "topsis_observer_outputs",
            [],
        ),
        "vikor": state.get(
            "vikor_observer_outputs",
            [],
        ),
    }

        state_update = {
            "current_round": current_round + 1,
        }
        goto = [
            "topsis_observer",
            "vikor_observer",
        ]
    else:
        state_update = {}
        goto = "save_record"

    return Command(
        update=state_update,
        goto=goto,
    )
# def consensus_node(state: A3State) -> A3State:
#     print("Hi, I am consensus", flush=True)
#     return {}

def validate_observations_node(state: A3State):
    # Verify that observer claims match the algorithm evidence.
    pass
#saving the records     
def save_record_node(state: A3State) -> A3State:
    """Save the current A3 experiment results."""

    record = {
        "experiment": "A3",
        "saved_at": datetime.now().isoformat(),
        "model_name": MODEL_NAME,
        "current_round": state["current_round"]+1, # for user-friendly display, increment the round number by 1
        "max_rounds": state["max_rounds"],
        "topsis_rankings": state[
            "topsis_rankings"
        ],
        "vikor_rankings": state[
            "vikor_rankings"
        ],
        "topsis_observer_outputs": state[
            "topsis_observer_outputs"
        ],
        "vikor_observer_outputs": state[
            "vikor_observer_outputs"
        ],
    }

    A3_RESULTS_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    A3_RESULT_FILE.write_text(
        json.dumps(
            record,
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    return {
        "saved_record_path": str(
            A3_RESULT_FILE
        ),
    }

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "agent running"}), 200
def calculate_validation_metrics():
    # calculate how well the selected offer matches the user requirements and priorities.
    # return a dict of metrics to be used in the validation node for feedback and improvement.
    pass
# def validator_node(state: AgentState):
# validate the selected offers based on the calculated metrics and provide feedback for improvement.
# pass
#####################################################################################################
@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(min=1, max=5),
    reraise=True,
)
def call_llm(data: dict[str, object]) -> dict[str, object]:
    """Call the LLM and return its parsed JSON answer."""
    response = requests.post(
        MASTER_URL,
        json=data,
        timeout=LLM_TIMEOUT,
    )
    response.raise_for_status()
    raw_result = response.json()

    content = (
        raw_result.get("choices", [{}])[0]
        .get("message", {})
        .get("content", "{}")
    )
    return json.loads(content)
##################################################################################################
def build_graph():
    graph = StateGraph(A3State)
    graph.add_node("load_rankings", load_rankings_node)
    graph.add_node("topsis_observer", topsis_observer_node)
    graph.add_node("vikor_observer", vikor_observer_node)
    graph.add_node("round_controller", round_controller_node)
    graph.add_node("save_record", save_record_node)
    graph.add_edge(START, "load_rankings")
    graph.add_edge("load_rankings", "topsis_observer")
    graph.add_edge("load_rankings", "vikor_observer")
    graph.add_edge(["topsis_observer", "vikor_observer"],"round_controller")
    graph.add_edge("save_record", END)
    return graph.compile()    
graph_app = build_graph()
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
#                
#Intent Analyzer
#↓
#Offer Selection
#↓
#Validation Metrics Calculation
#↓
#Validator
#↓
#Feedback Loop if needed        

# next TM Forum compliance inve and knowledge base 



# =============================================================================
# SEND VERSION OF THE A3 GRAPH — FUTURE EXAMPLE
# =============================================================================
#
# Required import:
#
# from langgraph.types import Send
#
#
# def dispatch_observers(state: A3State):
#     """Dynamically dispatch the two observer nodes."""
#
#     round_number = state.get("current_round", 0)
#
#     return [
#         Send(
#             "topsis_observer",
#             {
#                 "topsis_rankings": state["topsis_rankings"],
#                 "current_round": round_number,
#             },
#         ),
#         Send(
#             "vikor_observer",
#             {
#                 "vikor_rankings": state["vikor_rankings"],
#                 "current_round": round_number,
#             },
#         ),
#     ]
#
#
# def build_graph_with_send():
#     graph = StateGraph(A3State)
#
#     graph.add_node(
#         "load_rankings",
#         load_rankings_node,
#     )
#
#     graph.add_node(
#         "topsis_observer",
#         topsis_observer_node,
#     )
#
#     graph.add_node(
#         "vikor_observer",
#         vikor_observer_node,
#     )
#
#     graph.add_node(
#         "consensus",
#         consensus_node,
#     )
#
#     graph.add_edge(
#         START,
#         "load_rankings",
#     )
#
#     graph.add_conditional_edges(
#         "load_rankings",
#         dispatch_observers,
#         [
#             "topsis_observer",
#             "vikor_observer",
#         ],
#     )
#
#     graph.add_edge(
#         [
#             "topsis_observer",
#             "vikor_observer",
#         ],
#         "consensus",
#     )
#
#     graph.add_edge(
#         "consensus",
#         END,
#     )
#
#     return graph.compile()
#
# =============================================================================