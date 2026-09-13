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
def build_observer_user_prompt(
    algorithm: str,
    ranking_results: list[dict[str, object]],
) -> str:
    return json.dumps(
        {
            "source": f"{algorithm} algorithm output",
            "ranking_results": ranking_results,
            "task": (
                "Identify the top-ranked offer for every slice "
                "and explain its ranking using the supplied evidence."
            ),
            "required_output": {
                "algorithm": algorithm,
                "reports": [
                    {
                        "slice": "eMBB",
                        "use_case": "Media-Flex",
                        "top_offer_id": "integer",
                        "rank": 1,
                        "reason": "explanation",
                    },
                    {
                        "slice": "URLLC",
                        "use_case": "Factory-Ops",
                        "top_offer_id": "integer",
                        "rank": 1,
                        "reason": "explanation",
                    },
                    {
                        "slice": "mMTC",
                        "use_case": "IoT-Sense",
                        "top_offer_id": "integer",
                        "rank": 1,
                        "reason": "explanation",
                    },
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
    message_history: list[dict[str, object]]
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