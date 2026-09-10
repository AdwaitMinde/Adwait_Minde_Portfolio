import streamlit as st
from components import navbar, cards, charts
from data.projects import PROJECTS, CATEGORIES

navbar.render()

cards.section_heading("Projects", "Filter by category to explore the stack, architecture, and results behind each build.")

selected = st.radio("Filter", CATEGORIES, horizontal=True, label_visibility="collapsed")

filtered = PROJECTS if selected == "All Projects" else [p for p in PROJECTS if p["category"] == selected]

for project in filtered:
    cards.project_card(project)

if not filtered:
    st.info("No projects in this category yet.")

st.write("")
cards.section_heading("Project Scale & Technology Ecosystem")

col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(charts.project_scale_chart(), use_container_width=True, config={"displayModeBar": False})
with col2:
    st.markdown("**Technology Ecosystem**")
    st.graphviz_chart(charts.tech_ecosystem_graphviz(), use_container_width=True)
