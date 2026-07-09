from config import BASE_URL, WORLD_CUP_LEAGUE_ID, WORLD_CUP_SEASON
import os
import requests
from pathlib import Path
from dotenv import load_dotenv

# Load .env
dotenv_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=dotenv_path)

API_KEY = os.getenv("FOOTBALL_API_KEY")



HEADERS = {
    "x-apisports-key": API_KEY
}


def get_world_cup_matches():
    """
    Fetch FIFA World Cup 2022 matches.
    """

    url = f"{BASE_URL}/fixtures"

    params = {
    "league": WORLD_CUP_LEAGUE_ID,
    "season": WORLD_CUP_SEASON
}

    response = requests.get(url, headers=HEADERS, params=params)

    return response.json()["response"]

def find_match_by_team(team_name):
    """
    Find the first World Cup match for the given team.
    """

    matches = get_world_cup_matches()

    for match in matches:
        home_team = match["teams"]["home"]["name"]
        away_team = match["teams"]["away"]["name"]

        if (
            team_name.lower() == home_team.lower()
            or team_name.lower() == away_team.lower()
        ):
            return match

    return None

def find_match(team_name, match_date):
    """
    Find a World Cup match by team and date.
    """

    matches = get_world_cup_matches()

    for match in matches:

        home_team = match["teams"]["home"]["name"]
        away_team = match["teams"]["away"]["name"]

        fixture_date = match["fixture"]["date"][:10]

        if (
            fixture_date == match_date
            and (
                home_team.lower() == team_name.lower()
                or away_team.lower() == team_name.lower()
            )
        ):
            return match

    return None

def get_team_matches(team_name):
    """
    Return all World Cup matches played by the given team.
    """

    matches = get_world_cup_matches()

    team_matches = []

    for match in matches:

        home_team = match["teams"]["home"]["name"]
        away_team = match["teams"]["away"]["name"]

        if (
            team_name.lower() == home_team.lower()
            or team_name.lower() == away_team.lower()
        ):
            team_matches.append(match)

    return team_matches