import streamlit as st


def metric_card(value, label):
    st.markdown(
        f"""<div class="metric-card">
            <div class="metric-value">{value}</div>
            <div class="metric-label">{label}</div>
        </div>""",
        unsafe_allow_html=True,
    )


def metric_row(metrics, per_row=3):
    for i in range(0, len(metrics), per_row):
        cols = st.columns(per_row)
        chunk = metrics[i:i + per_row]
        for col, m in zip(cols, chunk):
            with col:
                metric_card(m["value"], m["label"])


def badges(items):
    html = "".join(f'<span class="badge">{item}</span>' for item in items)
    st.markdown(html, unsafe_allow_html=True)


def section_heading(title, subtitle=None):
    st.markdown(f'<div class="section-heading">{title}</div>', unsafe_allow_html=True)
    if subtitle:
        st.markdown(f'<div class="section-sub">{subtitle}</div>', unsafe_allow_html=True)


def experience_card(exp):
    with st.container(border=True):
        st.markdown(f"**{exp['role']}**")
        st.caption(f"{exp['org']} \u00b7 {exp['period']}")
        if exp["technologies"]:
            badges(exp["technologies"])
        for h in exp["highlights"]:
            st.markdown(f"- {h}")


def project_card(project):
    with st.container(border=True):
        st.markdown(f'<div class="category-tag">{project["category"]}</div>', unsafe_allow_html=True)
        st.markdown(f"### {project['title']}")
        badges(project["technologies"])

        st.markdown(f"**Problem:** {project['problem']}")

        with st.expander("Architecture & key achievements"):
            from components.architecture import flow_diagram
            flow_diagram(project["architecture"])
            st.markdown("**Highlights**")
            for h in project["highlights"]:
                st.markdown(f"- {h}")
            if project["skills"]:
                st.markdown("**Skills demonstrated**")
                badges(project["skills"])

        if project["metrics"]:
            cols = st.columns(len(project["metrics"]))
            for col, (label, value) in zip(cols, project["metrics"].items()):
                with col:
                    metric_card(value, label)

        for label, url in project["links"].items():
            st.link_button(label, url)


def resume_download_button(contact):
    try:
        with open("assets/Adwait Minde Resume.pdf", "rb") as f:
            st.download_button(
                "Download Resume", f, file_name="Adwait_Minde_Resume.pdf",
                mime="application/pdf", use_container_width=True,
            )
    except FileNotFoundError:
        st.link_button("Download Resume", contact["linkedin"], use_container_width=True)


def timeline_entry(year, description):
    st.markdown(
        f"""<div class="timeline-item">
            <div class="timeline-year">{year}</div>
            <div>{description}</div>
        </div>""",
        unsafe_allow_html=True,
    )
