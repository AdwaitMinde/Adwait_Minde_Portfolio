# Adwait Minde Portfolio

## Overview

A multipage Streamlit portfolio for Adwait Minde, covering data engineering,
analytics, machine learning, and AI/LLM work. Built to run standalone with no
external API keys.

## Features

- Interactive project cards with category filtering
- Interactive Plotly visualizations (data volume, career timeline)
- Graphviz technology ecosystem diagram
- HTML/CSS architecture flow diagrams per project
- Responsive dark-theme UI
- Ready for Streamlit Community Cloud deployment

## Tech Stack

Python, Streamlit, Plotly, Pandas, Graphviz

## Project Structure

```
portfolio/
├── Home.py
├── pages/
│   ├── 1_About.py
│   ├── 2_Experience.py
│   ├── 3_Projects.py
│   ├── 4_Technical_Skills.py
│   ├── 5_Education_Certifications.py
│   └── 6_Contact.py
├── components/
│   ├── navbar.py
│   ├── cards.py
│   ├── charts.py
│   └── architecture.py
├── data/
│   └── projects.py
├── assets/
│   ├── resume.pdf            (add your own)
│   └── images/
├── .streamlit/
│   ├── config.toml
│   └── secrets.toml.example
├── requirements.txt
├── packages.txt
└── README.md
```

## Local Installation

```bash
git clone <repository-url>
cd portfolio
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run Home.py
```

## Adding Your Resume

Drop a PDF at `assets/resume.pdf`. The Download Resume buttons on the Home
and Contact pages pick it up automatically; if it's missing, they fall back
to linking your LinkedIn instead of erroring out.

## Adding a Profile Photo

Drop an image at `assets/images/` and reference it with `st.image(...)`
wherever you'd like it to appear (e.g. the top of `Home.py` or
`pages/1_About.py`). No page currently displays one, so this is optional.

## Deployment to Streamlit Community Cloud

1. Create a GitHub repository.
2. Push this project to GitHub.
3. Sign in to Streamlit Community Cloud.
4. Select "Create App".
5. Select the GitHub repository.
6. Set the main file path to `Home.py`.
7. Deploy.

`packages.txt` installs the system `graphviz` binary the technology
ecosystem diagram needs — Streamlit Cloud reads it automatically.

### Updating after the first deploy

```bash
git add .
git commit -m "Update portfolio"
git push
```

Streamlit Cloud redeploys automatically on push.
