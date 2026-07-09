import streamlit as st

from api.football_api import get_team_matches
from llm.summarizer import generate_summary

st.set_page_config(
    page_title="AI FIFA Match Summary Generator",
    page_icon="⚽"
)

st.title("⚽ AI FIFA Match Summary Generator")

st.write("Generate AI-powered summaries for FIFA World Cup matches.")

st.divider()

# User enters team name
team = st.text_input("Enter Team Name")

# Store all matches for the selected team
matches = []

if team:
    matches = get_team_matches(team)

# Create dropdown options
match_options = {}

for match in matches:

    match_label = (
        f'{match["fixture"]["date"][:10]} | '
        f'{match["teams"]["home"]["name"]} vs '
        f'{match["teams"]["away"]["name"]}'
    )

    match_options[match_label] = match

selected_match = None

# Show dropdown only if matches are found
if match_options:

    selected_label = st.selectbox(
        "Select Match",
        list(match_options.keys())
    )

    selected_match = match_options[selected_label]

# Generate summary
if st.button("Generate Summary"):

    if selected_match:

        with st.spinner("Generating AI Summary..."):

            summary = generate_summary(selected_match)

        st.success("Summary Generated!")

        st.write(summary)

    else:

        st.error("Please enter a valid team and select a match.")