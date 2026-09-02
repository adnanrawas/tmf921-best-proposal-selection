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
        },
        indent=2,
    )
 #########llm request and response handling########################################
 ##########llm request and response handling########################################
def build_llm_request(
    system_prompt: str,
    user_prompt: str,
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
        ],
        "response_format": {
            "type": "json_object",
        },
        "stream": False,
    }
#########################################################################################