import streamlit as st
from components import navbar, cards

navbar.render()

cards.section_heading("About Me")

st.markdown(
    """
    I'm a recent Master of Science graduate in Management Information Systems from the
    University of Arizona, with a Bachelor's in Electronics and Computer Science from the
    University of Mumbai. My background sits at the intersection of information systems
    and computer science, which is what pulled me toward data: it's where technical
    problem-solving meets real business decisions.

    Across data engineering, analytics, machine learning, and AI, I've worked the full
    data lifecycle: ingestion, transformation, storage, analytics, machine learning, and
    visualization. Whether that's building a medallion lakehouse on 270M+ taxi trip
    records, running healthcare disparity analysis at Banner Health, or designing a
    knowledge distillation architecture that makes tabular predictions explainable, the
    common thread is turning messy, large-scale data into something people can actually
    use to make decisions.
    """
)

st.write("")
cards.section_heading("My Data Journey")

cards.timeline_entry("2023", "Bachelor's degree and early professional experience.")
cards.timeline_entry("2024", "Data engineering, databases, ML, and analytics projects.")
cards.timeline_entry("2025", "University of Arizona MS MIS, Banner Health analytics, APS consulting, Graduate Teaching Assistant.")
cards.timeline_entry("2026", "Advanced data engineering, lakehouse, streaming intelligence, and LLM knowledge distillation systems.")
