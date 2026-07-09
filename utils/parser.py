import re


def get_user_prompt():
    """
    Get the user's request.
    """
    return input("Enter your request: ")


def extract_query(prompt):
    """
    Extract team name and match date.

    Example:
    Summarize Argentina match on 2022-11-22
    """

    team_match = re.search(r"summarize\s+(.+?)\s+match", prompt, re.IGNORECASE)

    date_match = re.search(r"\d{4}-\d{2}-\d{2}", prompt)

    team = team_match.group(1).strip() if team_match else None
    date = date_match.group(0) if date_match else None

    return {
        "team": team,
        "date": date
    }