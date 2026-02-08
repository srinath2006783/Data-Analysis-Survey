import requests

# ==============================
# Local Ollama configuration
# ==============================

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3:8b"


def build_article_prompt(summary):
    """
    Builds an editorial-style prompt using computed insights ONLY.
    """

    return f"""
You are a data journalist writing a newspaper-style explainer article,
similar in tone to The Hindu or The Times of India.

Your role is to explain observed patterns clearly and calmly, without
offering advice, prescriptions, or emotional framing.

Use only the verified findings below. Do not speculate beyond them.

Overall risk distribution:
{summary["overall_risk"]}

Risk distribution by age group:
{summary["age_risk"]}

Risk distribution by role:
{summary["role_risk"]}

Top stress causes among high-risk respondents:
{summary["high_risk_causes"]}

STRICT WRITING GUIDELINES:
- Write in a neutral, analytical newspaper tone
- Avoid motivational, therapeutic, or advisory language
- Avoid words like “alarming”, “concerning”, or “worrying”
- Do not address the reader directly
- Do not mention surveys, charts, or methodology
- Do not repeat raw numbers mechanically
- Prefer phrasing such as “the data suggests”, “the distribution indicates”, “a closer look shows”

STYLE EXPECTATIONS:
- Short, clear paragraphs
- Emphasis on contrast and concentration
- No bullet points or headings
- No rhetorical questions
- No conclusions about what should be done

STRUCTURE:
1. One paragraph explaining the overall distribution
2. One paragraph interpreting age-based patterns
3. One paragraph interpreting role-based patterns
4. One paragraph explaining stress causes among high-risk respondents
5. One restrained concluding paragraph synthesising the findings

Write as if for a general newspaper audience interested in data-driven insight.
"""


def generate_llm_article(summary):
    """
    Generates an editorial article using a local Ollama model.
    """

    prompt = build_article_prompt(summary)

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload, timeout=120)
    response.raise_for_status()

    result = response.json()
    return result["response"].strip()