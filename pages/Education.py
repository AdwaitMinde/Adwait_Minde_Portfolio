import streamlit as st
from components import navbar, cards
from data.projects import EDUCATION, CERTIFICATIONS

navbar.render()

cards.section_heading("Education")

for edu in EDUCATION:
    with st.container(border=True):
        st.markdown(f"**{edu['degree']}**")
        st.caption(f"{edu['school']} \u00b7 GPA {edu['gpa']} \u00b7 {edu['date']}")

st.write("")
cards.section_heading("Certifications")

for cert in CERTIFICATIONS:
    st.markdown(f"- {cert}")
