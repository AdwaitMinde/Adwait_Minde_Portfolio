import streamlit as st


def flow_diagram(steps):
    for i, step in enumerate(steps):
        st.markdown(f'<div class="flow-step">{step}</div>', unsafe_allow_html=True)
        if i < len(steps) - 1:
            st.markdown('<div class="flow-arrow">&#8595;</div>', unsafe_allow_html=True)
