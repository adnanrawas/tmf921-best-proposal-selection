import json

def build_observer_system_prompt( #system prompt  
    algorithm: str, 
    ranking_rule: str,
    score_values: str,
) -> str:
    return f"""
You are the {algorithm} observer in a multi-agent offer-selection system.
Identify the top-ranked offer in the supplied algorithm output.

{ranking_rule}
Treat the supplied rank as authoritative.

Rules:
- Do not recalculate {algorithm}.
- Do not change any rank or {score_values}.
- Do not invent offers.
- Recommend only an offer contained in the supplied ranking.
- Return valid JSON only, without Markdown.
"""
#############################################################################
# 
# def build_observer_user_prompt(
#     algorithm: str,
#     ranking_results: list[dict[str, object]],
# ) -> str:
#     return json.dumps(
#         {
#             "source": f"{algorithm} algorithm output",
#             "ranking_results": ranking_results,
#             "task": (
#                 "Identify the top-ranked offer for every slice "
#                 "and explain its ranking using the supplied evidence."
#             ),
#             "required_output": {
#                 "algorithm": algorithm,
#                 "reports": [
#                     {
#                         "slice": "eMBB",
#                         "use_case": "Media-Flex",
#                         "top_offer_id": "integer",
#                         "rank": 1,
#                         "reason": "explanation",
#                     },
#                     {
#                         "slice": "URLLC",
#                         "use_case": "Factory-Ops",
#                         "top_offer_id": "integer",
#                         "rank": 1,
#                         "reason": "explanation",
#                     },
#                     {
#                         "slice": "mMTC",
#                         "use_case": "IoT-Sense",
#                         "top_offer_id": "integer",
#                         "rank": 1,
#                         "reason": "explanation",
#                     },
#                 ],
#             },    
#         },
#         indent=2,
#     )

def build_observer_user_prompt(
    algorithm: str,
    ranking_results: list[dict[str, object]],
) -> str:
        return json.dumps(
            {
                "source": f"{algorithm} algorithm output",
                "ranking_results": ranking_results,
                "task": (
                    "Analyze every supplied ranked offer for every slice "
                    "and explain its ranking using the supplied evidence."
                ),
                "required_output": {
                    "algorithm": algorithm,
                    "reports": [
                        {
                            "slice": "string",
                            "use_case": "string",
                            "offer_id": "integer",
                            "rank": "integer",
                            "reason": "explanation",
                        }
                    ],
                }, 
            },
            indent=2,
        )
 #########llm request and response handling########################################
 ##########llm request and response handling########################################
def build_llm_request(
    system_prompt: str,
    user_prompt: str,
    message_history: list[dict[str, object]],
    model_name: str,
) -> dict[str, object]:
    return {
        "model": model_name,
        "messages": [
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
            {
                "role": "assistant",
                "content": message_history,
            },
        ],
        "response_format": {
            "type": "json_object",
        },
        "stream": False,
    }
#########################################################################################
def get_latest_report( # get the latest report from the report history
    report_history: list[dict[str, object]],
) -> dict[str, object] | None:
    """Return the latest observer report."""
    if not report_history:
        return None

    return report_history[-1]
##########################################################################################

def limit_rankings( #limit the number of rankings returned by the observer
    rankings: dict[str, object],
    limit: int | None = None,
) -> dict[str, object]:

    if limit is None:
        return rankings

    ranking_list = rankings.get("rankings")

    if not isinstance(ranking_list, list):
        raise RuntimeError("Rankings must contain a 'rankings' list")

    if limit < len(ranking_list):
        rankings["rankings"] = ranking_list[:limit]

    return rankings

##########################################################################################    
def limit_rankings( #later transform it to data models for each ranking algorithm 
    rankings: dict[str, object],
    limit: int | None = None,
) -> dict[str, object]:

    if limit is None:
        return rankings

    results = rankings.get("results")

    if not isinstance(results, list):
        raise RuntimeError("Rankings must contain a 'results' list")

    for result in results:
        ranking_list = result.get("ranking")

        if not isinstance(ranking_list, list):
            raise RuntimeError("Each result must contain a 'ranking' list")

        if limit < len(ranking_list):
            result["ranking"] = ranking_list[:limit]

    return rankings