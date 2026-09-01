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


class A3State(TypedDict, total=False):
    intent: dict
    feasible_offers: list[dict[str, object]]
    topsis_rankings: dict[str, object]
    vikor_rankings: dict[str, object]
    # saw_rankings: dict[str, list[dict]] # to be implemented
    messages: Annotated[list[AnyMessage], add_messages]
    observer_outputs: Annotated[list[dict[str, object]], add]
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
# def rank_feasible_offers_node(state: A3State) -> A3State:
#     """Retrieve feasible offers and rank them using MCDA services."""
#     intent = state.get("intent")
#     feasible_offers = fetch_feasible_offers(intent)
#     saw_rankings = fetch_saw_rankings(
#         intent,
#         feasible_offers,
#     )
#     topsis_rankings = fetch_topsis_rankings(
#         intent,
#         feasible_offers,
#     )
#     vikor_rankings = fetch_vikor_rankings(
#         intent,
#         feasible_offers,
#     )
#     return {
#         "intent": intent,
#         "feasible_offers": feasible_offers,
#         "saw_rankings": saw_rankings,
#         "topsis_rankings": topsis_rankings,
#         "vikor_rankings": vikor_rankings,
#     }

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
     }    
    print(state_update, flush=True)
    return state_update
#########################################################################################
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
    system_prompt = """
        You are the TOPSIS observer in a multi-agent offer-selection system.
        Identify the top-ranked offer in the supplied algorithm output
        Rules:
        - Do not recalculate TOPSIS.
        - Do not change any rank or TOPSIS score.
        - Do not invent offers.
        - Recommend only an offer contained in the supplied ranking.
        - Return valid JSON only, without Markdown.
        """
           # Third variable: the input message containing the ranking data.
    user_prompt = json.dumps(
        {
            "source": "TOPSIS algorithm output",
            "ranking_results": topsis_results,
            "task": (
                "Identify the top-ranked offer for every slice "
                "and explain its ranking using the supplied evidence."
            ),
        },
        indent=2,
    )
    request_messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}]

    request_data = {
    "model": MODEL_NAME,
    "messages": request_messages,
    "response_format": {"type": "json_object"},
    "stream": False,
     }
    result = call_llm(request_data)
def vikor_observer_node(state: A3State):
    # Interpret the VIKOR ranking against the user intent.
    pass


def validate_observations_node(state: A3State):
    # Verify that observer claims match the algorithm evidence.
    pass


def consensus_node(state: A3State):
    # Apply the consensus rule and recommend an offer.
    pass


def save_record_node(state: A3State):
    # Save the evidence, messages, validation, and final result.
    pass

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "agent running"}), 200


def calculate_validation_metrics():
    # calculate how well the selected offer matches the user requirements and priorities.
    # return a dict of metrics to be used in the validation node for feedback and improvement.
    pass
#####################################################################################################

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(min=1, max=5),
    reraise=True,
)
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

# def validator_node(state: AgentState):
#     # validate the selected offers based on the calculated metrics and provide feedback for improvement.
#     pass


def build_graph():

    graph = StateGraph(A3State)graph.add_edge(START, "load_rankings")
    graph.add_node("load_rankings", load_rankings_node)
    graph.add_node("topsis_observer", topsis_observer_node)
    graph.add_edge(START, "load_rankings")
    graph.add_edge("load_rankings", "topsis_observer")
    graph.add_edge("topsis_observer", END)
    # graph.add_node("intent_analyzer_node", intent_analyzer_node)
    # graph.add_node("topsis_baseline_node", topsis_baseline_node)
    # graph.add_node("offer_selection_node", offer_selection_node)
    # graph.add_edge(START, "intent_analyzer_node")
    # graph.add_edge("intent_analyzer_node", "topsis_baseline_node")
    # graph.add_edge("intent_analyzer_node", "offer_selection_node")
    # graph.add_edge("offer_selection_node", END)

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
