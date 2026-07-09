from utils.parser import get_user_prompt, extract_query
from api.football_api import find_match
from llm.summarizer import generate_summary

prompt = get_user_prompt()

query = extract_query(prompt)

match = find_match(
    query["team"],
    query["date"]
)

if match:

    print("\nGenerating AI Summary...\n")

    summary = generate_summary(match)

    print(summary)

else:
    print("Match not found.")