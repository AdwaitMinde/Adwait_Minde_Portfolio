import streamlit as st
from components import navbar, cards
from data.projects import CONTACT

navbar.render()

st.markdown(
    """
    <div style="text-align:center; padding: 1.5rem 0;">
        <div style="font-size:2.1rem; font-weight:800; color:#e9edf5;">Let's Build Something With Data.</div>
        <div style="color:#8891a5; max-width:560px; margin:0.8rem auto 0 auto;">
            I'm always interested in opportunities involving data engineering, analytics,
            machine learning, AI, and data-driven problem solving.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

c1, c2, c3 = st.columns(3)
with c1:
    st.link_button("Connect on LinkedIn", CONTACT["linkedin"], use_container_width=True, icon="\U0001F517")
with c2:
    st.link_button("Email Me", f"mailto:{CONTACT['email']}", use_container_width=True, icon="\U0001F4E7")
with c3:
    try:
        with open("assets/resume.pdf", "rb") as f:
            st.download_button(
                "Download Resume", f, file_name="Adwait_Minde_Resume.pdf",
                mime="application/pdf", use_container_width=True,
            )
    except FileNotFoundError:
        st.link_button("Download Resume", CONTACT["linkedin"], use_container_width=True)

st.write("")
st.caption(f"Email: {CONTACT['email']}")
