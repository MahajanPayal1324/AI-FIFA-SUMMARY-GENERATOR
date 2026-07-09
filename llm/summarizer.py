from config import OLLAMA_MODEL
import ollama


def build_prompt(match):
    """
    Convert match data into a prompt for the LLM.
    """

    home = match["teams"]["home"]["name"]
    away = match["teams"]["away"]["name"]

    home_score = match["goals"]["home"]
    away_score = match["goals"]["away"]

    date = match["fixture"]["date"][:10]

    prompt = f"""
You are a professional football analyst.

Match Details

Date: {date}
Home Team: {home}
Away Team: {away}

Final Score:
{home} {home_score} - {away_score} {away}

Generate a professional summary of this FIFA World Cup match.

Rules:
- Maximum 120 words
- Mention the winning team
- Mention the final score
- Keep it factual
- Do not invent facts
"""

    return prompt


def generate_summary(match):
    """
    Generate a summary using Ollama.
    """

    prompt = build_prompt(match)

    response = ollama.chat(
        model=OLLAMA_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]