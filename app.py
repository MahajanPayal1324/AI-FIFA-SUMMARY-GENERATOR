import streamlit as st

st.set_page_config(
    page_title="AI FIFA Match Summary Generator",
    page_icon="⚽"
)

st.title("⚽ AI FIFA Match Summary Generator")

st.write(
    "Generate AI-powered summaries for FIFA World Cup matches."
)

st.divider()

team = st.text_input("Enter Team Name")

match_date = st.date_input("Select Match Date")

st.button("Generate Summary")