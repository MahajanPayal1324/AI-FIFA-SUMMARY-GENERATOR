import streamlit as st

from api.football_api import find_match
from llm.summarizer import generate_summary

st.set_page_config(
    page_title="AI FIFA Match Summary Generator",
    page_icon="⚽"
)

st.title("⚽ AI FIFA Match Summary Generator")

st.write("Generate AI-powered summaries for FIFA World Cup matches.")

st.divider()

team = st.text_input("Enter Team Name")

match_date = st.date_input("Select Match Date")

if st.button("Generate Summary"):

    match = find_match(
        team,
        str(match_date)
    )

    if match:

        with st.spinner("Generating AI Summary..."):

            summary = generate_summary(match)

        st.success("Summary Generated!")

        st.write(summary)

    else:

        st.error("Match not found.")