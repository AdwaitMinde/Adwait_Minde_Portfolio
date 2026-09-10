import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

DARK = "#0a0e17"
BLUE = "#4d8dff"
CYAN = "#35e0d5"
TEXT = "#c7cede"

BASE_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color=TEXT, family="Inter, sans-serif"),
    margin=dict(l=10, r=10, t=40, b=10),
)


def project_scale_chart():
    data = pd.DataFrame([
        {"project": "NYC Taxi Lakehouse", "records": 270_000_000},
        {"project": "Security Incident ML", "records": 1_000_000},
        {"project": "Estonia Traffic", "records": 790_000},
        {"project": "Customer Churn Events", "records": 500_000},
    ])
    fig = go.Figure(go.Bar(
        x=data["records"],
        y=data["project"],
        orientation="h",
        marker=dict(color=[CYAN, BLUE, CYAN, BLUE], line=dict(width=0)),
        text=[f"{v:,}" for v in data["records"]],
        textposition="outside",
    ))
    fig.update_layout(
        **BASE_LAYOUT,
        title="Data Volume by Project (log scale)",
        xaxis=dict(type="log", showgrid=False, title="Records / Events"),
        yaxis=dict(showgrid=False, autorange="reversed"),
        height=320,
    )
    return fig


def tech_ecosystem_graphviz():
    return """
    digraph G {
        bgcolor="transparent";
        rankdir=LR;
        node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11,
              color="#4d8dff", fillcolor="#10151f", fontcolor="#e9edf5", penwidth=1.2];
        edge [color="#35e0d5", arrowsize=0.6];

        DE [label="Data Engineering"];
        AN [label="Analytics"];
        ML [label="Machine Learning"];
        AI [label="AI / LLM"];
        CL [label="Cloud"];

        DE -> "PySpark / Delta Lake";
        DE -> "Airflow / dbt";
        DE -> "Kafka";
        CL -> "AWS (S3, Glue, Athena)";
        CL -> "Databricks / BigQuery";
        AN -> "Power BI / Tableau";
        AN -> "Plotly";
        ML -> "XGBoost / Scikit-learn";
        ML -> "PyTorch";
        AI -> "RAG / FAISS";
        AI -> "Knowledge Distillation";
        AI -> "Claude AI";

        DE -> CL;
        ML -> AI;
        DE -> AN;
        ML -> DE;
    }
    """


def career_timeline_chart(experience):
    rows = []
    for exp in experience:
        start, end = exp["period"].split(" - ")
        rows.append({
            "Role": f"{exp['role']} · {exp['org']}",
            "Start": pd.to_datetime(start.strip(), format="%B %Y", errors="coerce"),
            "End": pd.Timestamp.today() if "Present" in end else pd.to_datetime(end.strip(), format="%B %Y", errors="coerce"),
        })
    df = pd.DataFrame(rows)
    fig = px.timeline(df, x_start="Start", x_end="End", y="Role", color_discrete_sequence=[CYAN])
    fig.update_yaxes(autorange="reversed", showgrid=False, title="")
    fig.update_xaxes(showgrid=False, title="")
    fig.update_layout(**BASE_LAYOUT, height=320, title="Career Timeline", showlegend=False)
    return fig
