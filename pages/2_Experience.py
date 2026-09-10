import streamlit as st
from components import navbar, cards, charts
from data.projects import EXPERIENCE

navbar.render()

cards.section_heading("Experience", "Professional and academic experience, most recent first.")

st.plotly_chart(charts.career_timeline_chart(EXPERIENCE), use_container_width=True, config={"displayModeBar": False})

st.write("")
for exp in EXPERIENCE:
    cards.experience_card(exp)
