import streamlit as st

from api.football_api import get_team_matches
from llm.summarizer import generate_summary

st.set_page_config(
    page_title="AI FIFA Match Summary Generator",
    page_icon="⚽",
    layout="centered"
)

st.title("⚽ AI FIFA Match Summary Generator")

st.write("Generate AI-powered summaries for FIFA World Cup matches.")

st.divider()

# -----------------------------
# Team Input
# -----------------------------
team = st.text_input("Enter Team Name")

matches = []

if team:
    matches = get_team_matches(team)

# -----------------------------
# Match Dropdown
# -----------------------------
match_options = {}

for match in matches:

    match_label = (
        f'{match["fixture"]["date"][:10]} | '
        f'{match["teams"]["home"]["name"]} vs '
        f'{match["teams"]["away"]["name"]}'
    )

    match_options[match_label] = match

selected_match = None

if match_options:

    selected_label = st.selectbox(
        "Select Match",
        list(match_options.keys())
    )

    selected_match = match_options[selected_label]

# -----------------------------
# Match Details
# -----------------------------
if selected_match:

    st.divider()

    st.subheader("📊 Match Details")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**🏠 Home Team**")
        st.write(selected_match["teams"]["home"]["name"])

        st.write("**📅 Date**")
        st.write(selected_match["fixture"]["date"][:10])

    with col2:
        st.write("**✈️ Away Team**")
        st.write(selected_match["teams"]["away"]["name"])

        st.write("**⚽ Score**")

        home_goals = selected_match["goals"]["home"]
        away_goals = selected_match["goals"]["away"]

        st.write(f"{home_goals} - {away_goals}")

# -----------------------------
# Generate Summary
# -----------------------------
# -----------------------------
# Generate Summary
# -----------------------------
if st.button("Generate Summary"):

    if selected_match:

        with st.spinner("Generating AI Summary..."):

            summary = generate_summary(selected_match)

        st.divider()

        st.subheader("🤖 AI Match Summary")

        with st.container(border=True):

            st.markdown(summary)

    else:

        st.error("Please enter a valid team and select a match.")