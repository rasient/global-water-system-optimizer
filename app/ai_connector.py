import os
from typing import Dict, List

from dotenv import load_dotenv

load_dotenv()


def build_strategy_prompt(metrics: Dict[str, float], bottlenecks: List[str], recommendations: List[Dict[str, str]]) -> str:
    recommendation_text = "\n".join(
        f"- {r['Priority']}: {r['Intervention']} — {r['Why it matters']}" for r in recommendations
    )
    metric_text = "\n".join(f"- {k}: {v:.1f}" for k, v in metrics.items())
    bottleneck_text = "\n".join(f"- {b}" for b in bottlenecks)

    return f"""
You are a water systems strategy analyst. Write a concise, LinkedIn-ready strategy memo based on this simplified water-system scenario.

Frame the problem as a system-design challenge, not only a water-supply challenge.

Metrics:
{metric_text}

Bottlenecks:
{bottleneck_text}

Recommended interventions:
{recommendation_text}

Output format:
1. 3-line executive summary
2. Key bottleneck
3. Best first move
4. Why this matters for climate resilience
5. One strong final sentence
""".strip()


def generate_strategy_memo(prompt: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

    if not api_key:
        return "OpenAI API key not found. Add OPENAI_API_KEY to your .env file to enable the AI strategy memo."

    try:
        from openai import OpenAI

        client = OpenAI(api_key=api_key)
        response = client.responses.create(
            model=model,
            input=prompt,
        )
        return response.output_text
    except Exception as exc:
        return f"AI generation failed: {exc}"
