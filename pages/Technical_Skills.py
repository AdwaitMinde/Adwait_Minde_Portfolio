import streamlit as st
from components import navbar, cards
from data.projects import SKILLS

navbar.render()

cards.section_heading("Technical Skills", "Grouped by domain — no made-up proficiency bars.")

for category, skills in SKILLS.items():
    with st.container(border=True):
        st.markdown(f"**{category}**")
        cards.badges(skills)
