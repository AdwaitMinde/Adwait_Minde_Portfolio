import streamlit as st
from components import navbar, cards
from data.projects import SNAPSHOT_METRICS, CONTACT

navbar.render()

st.markdown(
    """
    <div style="text-align:center; padding: 2.5rem 0 1rem 0;">
        <div style="color:#35e0d5; font-family:'JetBrains Mono', monospace; font-size:0.95rem; margin-bottom:0.6rem;">
            Hi, I'm Adwait Minde
        </div>
        <div style="font-size:2.6rem; font-weight:800; color:#e9edf5; letter-spacing:-0.02em; line-height:1.15;">
            Data Engineer &nbsp;|&nbsp; Data Analyst &nbsp;|&nbsp; AI &amp; Machine Learning
        </div>
        <div style="color:#8891a5; font-size:1.05rem; max-width:680px; margin:1.1rem auto 0 auto;">
            I build scalable data pipelines, analytics platforms, machine learning models,
            and AI-powered systems that transform complex data into actionable insights.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

c1, c2, c3 = st.columns(3)
with c1:
    st.page_link("pages/3_Projects.py", label="View Projects", icon="\U0001F4C1", use_container_width=True)
with c2:
    try:
        with open("assets/resume.pdf", "rb") as f:
            st.download_button(
                "Download Resume", f, file_name="Adwait_Minde_Resume.pdf",
                mime="application/pdf", use_container_width=True,
            )
    except FileNotFoundError:
        st.link_button("Download Resume", CONTACT["linkedin"], use_container_width=True)
with c3:
    st.link_button("Connect on LinkedIn", CONTACT["linkedin"], use_container_width=True, icon="\U0001F517")

st.write("")
cards.section_heading("Quick Snapshot", "Verified numbers pulled straight from shipped project work.")
cards.metric_row(SNAPSHOT_METRICS, per_row=3)

st.write("")
cards.section_heading("What I Build")

build_cols = st.columns(4)
categories = [
    ("Data Engineering", "ETL pipelines, lakehouse architectures, cloud data platforms, orchestration, and data quality systems."),
    ("Data Analytics", "Interactive dashboards, business intelligence, exploratory analysis, and stakeholder insights."),
    ("Machine Learning", "Predictive models, feature engineering, model evaluation, and explainable ML."),
    ("AI & LLM Systems", "RAG architectures, knowledge distillation, LLM prompting, evaluation, and AI-powered explanations."),
]
for col, (title, desc) in zip(build_cols, categories):
    with col:
        with st.container(border=True):
            st.markdown(f"**{title}**")
            st.caption(desc)
