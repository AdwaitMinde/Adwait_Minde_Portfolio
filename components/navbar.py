import streamlit as st

GLOBAL_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, sans-serif;
    }

    :root {
        --bg-primary: #0a0e17;
        --bg-secondary: #10151f;
        --bg-card: rgba(255, 255, 255, 0.03);
        --border-subtle: rgba(255, 255, 255, 0.08);
        --accent-blue: #4d8dff;
        --accent-cyan: #35e0d5;
        --text-primary: #e9edf5;
        --text-muted: #8891a5;
    }

    .stApp {
        background:
            radial-gradient(circle at 15% 0%, rgba(77, 141, 255, 0.10) 0%, transparent 45%),
            radial-gradient(circle at 85% 15%, rgba(53, 224, 213, 0.07) 0%, transparent 45%),
            var(--bg-primary);
    }

    #MainMenu, footer, header {visibility: hidden;}

    .block-container {
        padding-top: 2rem;
        max-width: 1150px;
    }

    /* Top navbar - the first bordered st.container on the page */
    div[data-testid="stVerticalBlockBorderWrapper"]:has(.navbar-brand) {
        background: rgba(255, 255, 255, 0.02);
        backdrop-filter: blur(10px);
        border-radius: 14px !important;
        border-color: var(--border-subtle) !important;
        margin-bottom: 1.6rem;
    }
    div[data-testid="stVerticalBlockBorderWrapper"]:has(.navbar-brand) [data-testid="stVerticalBlock"] {
        gap: 0;
    }
    .navbar-brand {
        font-weight: 700;
        font-size: 1.05rem;
        color: var(--text-primary);
        letter-spacing: -0.01em;
    }
    .navbar-brand span { color: var(--accent-cyan); }

    div[data-testid="stPageLink"] a {
        color: var(--text-muted) !important;
        font-size: 0.92rem;
        font-weight: 500;
        border-radius: 8px;
        transition: all 0.15s ease;
    }
    div[data-testid="stPageLink"] a:hover {
        color: var(--text-primary) !important;
        background: rgba(255, 255, 255, 0.06);
    }
    div[data-testid="stPageLink"] p { font-size: 0.92rem !important; }

    /* Section heading */
    .section-heading {
        font-size: 1.7rem;
        font-weight: 700;
        color: var(--text-primary);
        margin: 2.2rem 0 0.4rem 0;
        letter-spacing: -0.02em;
    }
    .section-sub {
        color: var(--text-muted);
        font-size: 0.98rem;
        margin-bottom: 1.4rem;
    }

    /* Cards */
    .glass-card {
        background: var(--bg-card);
        border: 1px solid var(--border-subtle);
        border-radius: 16px;
        padding: 1.5rem 1.6rem;
        margin-bottom: 1.1rem;
        transition: border-color 0.2s ease, transform 0.2s ease;
    }
    .glass-card:hover {
        border-color: rgba(77, 141, 255, 0.35);
        transform: translateY(-2px);
    }

    .metric-card {
        background: var(--bg-card);
        border: 1px solid var(--border-subtle);
        border-radius: 14px;
        padding: 1.3rem 1rem;
        text-align: center;
    }
    .metric-value {
        font-size: 1.9rem;
        font-weight: 800;
        background: linear-gradient(120deg, var(--accent-blue), var(--accent-cyan));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        line-height: 1.1;
    }
    .metric-label {
        color: var(--text-muted);
        font-size: 0.82rem;
        margin-top: 0.35rem;
    }

    .badge {
        display: inline-block;
        background: rgba(77, 141, 255, 0.10);
        border: 1px solid rgba(77, 141, 255, 0.25);
        color: #a9c6ff;
        border-radius: 999px;
        padding: 0.22rem 0.75rem;
        font-size: 0.78rem;
        font-family: 'JetBrains Mono', monospace;
        margin: 0.15rem 0.3rem 0.15rem 0;
    }

    .category-tag {
        display: inline-block;
        background: rgba(53, 224, 213, 0.10);
        border: 1px solid rgba(53, 224, 213, 0.3);
        color: var(--accent-cyan);
        border-radius: 6px;
        padding: 0.15rem 0.6rem;
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.04em;
        margin-bottom: 0.6rem;
    }

    .flow-step {
        background: var(--bg-card);
        border: 1px solid var(--border-subtle);
        border-radius: 10px;
        padding: 0.6rem 1rem;
        text-align: center;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.85rem;
        color: var(--text-primary);
    }
    .flow-arrow {
        text-align: center;
        color: var(--accent-cyan);
        font-size: 1.1rem;
        line-height: 0.6;
    }

    .timeline-item {
        border-left: 2px solid rgba(77, 141, 255, 0.35);
        padding-left: 1.2rem;
        margin-bottom: 1.4rem;
        position: relative;
    }
    .timeline-item::before {
        content: '';
        position: absolute;
        left: -6px;
        top: 4px;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background: var(--accent-cyan);
        box-shadow: 0 0 8px rgba(53, 224, 213, 0.6);
    }
    .timeline-year {
        color: var(--accent-cyan);
        font-family: 'JetBrains Mono', monospace;
        font-weight: 700;
        font-size: 0.95rem;
    }

    .stButton > button, .stDownloadButton > button {
        background: linear-gradient(120deg, var(--accent-blue), var(--accent-cyan));
        color: #06121f;
        font-weight: 600;
        border: none;
        border-radius: 10px;
        padding: 0.55rem 1.3rem;
    }
    .stButton > button:hover, .stDownloadButton > button:hover {
        filter: brightness(1.08);
    }
</style>
"""

NAV_PAGES = [
    ("Home.py", "Home"),
    ("pages/1_About.py", "About"),
    ("pages/2_Experience.py", "Experience"),
    ("pages/3_Projects.py", "Projects"),
    ("pages/4_Technical_Skills.py", "Skills"),
    ("pages/5_Education_Certifications.py", "Education"),
    ("pages/6_Contact.py", "Contact"),
]


def render():
    st.set_page_config(
        page_title="Adwait Minde | Data Portfolio",
        page_icon="\U0001F4CA",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

    with st.container(border=True):
        left, *nav_cols = st.columns([2.6] + [1] * len(NAV_PAGES))
        with left:
            st.markdown('<div class="navbar-brand">Adwait <span>Minde</span></div>', unsafe_allow_html=True)
        for col, (path, label) in zip(nav_cols, NAV_PAGES):
            with col:
                st.page_link(path, label=label)
