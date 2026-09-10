"""
All portfolio project data lives here so the pages stay pure UI code.
Every metric below is pulled straight from Adwait's resume/work history -
nothing here is invented or estimated.
"""

PROJECTS = [
    {
        "title": "NYC Taxi Lakehouse: End-to-End Medallion Pipeline",
        "category": "Data Engineering",
        "technologies": ["PySpark", "Delta Lake", "Databricks Jobs", "Streamlit"],
        "problem": (
            "NYC TLC publishes trip data across four separate transportation "
            "datasets with no unified, quality-checked view for analysis."
        ),
        "architecture": [
            "NYC TLC Data",
            "Bronze Layer",
            "Silver Layer + Data Quality",
            "Gold Analytics Layer",
            "Databricks Jobs Orchestration",
            "Streamlit Dashboard",
        ],
        "highlights": [
            "Processed 270M+ NYC TLC trip records across 4 integrated transportation datasets",
            "Built a Bronze / Silver / Gold medallion architecture on Delta Lake",
            "Validated Delta schemas against production files and built deterministic data quality checks",
            "Used PySpark window functions for deduplication with quarantine routing for bad records",
            "Root-caused a Spark casting defect affecting trip duration calculations",
            "Orchestrated a 12-task dependency-aware Databricks Jobs DAG",
            "Built a public Streamlit dashboard covering revenue, demand, and trip duration",
        ],
        "metrics": {"Records processed": "270M+", "Datasets integrated": "4", "DAG tasks": "12"},
        "skills": ["PySpark", "Delta Lake", "Data Quality", "Orchestration", "Lakehouse Design"],
        "links": {"Live Dashboard": "https://nyc-taxi-lakehouse-dashboard.streamlit.app"},
    },
    {
        "title": "Real-Time Customer Churn Intelligence Platform",
        "category": "AI & LLM",
        "technologies": ["Kafka", "AWS S3", "BigQuery", "dbt", "XGBoost", "MLflow", "Claude AI", "SHAP", "Streamlit"],
        "problem": (
            "E-commerce behavioral events needed a streaming path to a trustworthy churn "
            "model, with results explainable to non-technical stakeholders."
        ),
        "architecture": [
            "Behavioral Events",
            "Kafka",
            "AWS S3",
            "BigQuery",
            "dbt Transformations + Tests",
            "Feature Mart",
            "XGBoost + MLflow",
            "SHAP + Claude AI",
            "Streamlit Dashboard",
        ],
        "highlights": [
            "Built a streaming pipeline ingesting 500K e-commerce behavioral events",
            "Built a dbt-powered BigQuery warehouse with 7 schema tests",
            "Created a customer feature mart covering 7,362 users",
            "Trained an XGBoost churn classifier reaching 0.9956 AUC / 0.9911 F1",
            "Tracked 3 MLflow experiments for reproducibility",
            "Used SHAP to identify recency and purchase frequency as top churn signals",
            "Used Claude AI (Haiku) to generate plain-English churn explanations for 6,826 at-risk users",
            "Built a two-tab Streamlit dashboard for model output and explanations",
        ],
        "metrics": {"Events ingested": "500K", "AUC": "0.9956", "F1 Score": "0.9911", "Users explained": "6,826"},
        "skills": ["Streaming Data", "Feature Engineering", "XGBoost", "Model Explainability", "LLM Integration"],
        "links": {"Live Dashboard": "https://churn-intelligence-platform-project.streamlit.app"},
    },
    {
        "title": "Airflow Data Pipelines",
        "category": "Data Engineering",
        "technologies": ["Apache Airflow", "Amazon S3", "Amazon Redshift", "Python", "Tableau", "QuickSight"],
        "problem": (
            "Daily S3-to-Redshift loads needed to be automated, idempotent, and quality-checked "
            "without manual reprocessing."
        ),
        "architecture": ["S3", "Airflow DAG", "Custom Operators + Data Quality Checks", "Redshift", "Tableau / QuickSight"],
        "highlights": [
            "Built automated ETL pipelines with custom Airflow operators",
            "Automated daily S3-to-Redshift data loading",
            "Built idempotent, parameterized workflows with partitioned loads",
            "Reduced reprocessing time by 40%",
            "Built a DataQualityOperator using SQL validation",
            "Designed a star-schema warehouse connected to Tableau and QuickSight",
        ],
        "metrics": {"Reprocessing time reduced": "40%"},
        "skills": ["Airflow", "Custom Operators", "Star Schema Design", "Data Quality"],
        "links": {},
    },
    {
        "title": "Cloud-Based ETL Pipeline Development",
        "category": "Data Engineering",
        "technologies": ["AWS", "Glue", "S3", "Athena"],
        "problem": "Retail order and customer data needed scalable, queryable ETL pipelines on AWS.",
        "architecture": ["Raw Data", "AWS Glue Transformations", "S3", "Athena Queries", "Fact / Dimension Tables"],
        "highlights": [
            "Built two complete ETL pipelines processing retail order and customer data",
            "Used AWS Glue transformations and stored datasets in S3",
            "Queried outputs using Athena",
            "Generated fact and dimension tables with clear data lineage",
            "Designed scalable and modular workflows",
        ],
        "metrics": {"Pipelines built": "2"},
        "skills": ["AWS Glue", "S3", "Athena", "Dimensional Modeling"],
        "links": {},
    },
    {
        "title": "Microsoft Security Incident False-Positive Prediction",
        "category": "Machine Learning",
        "technologies": ["Python", "Random Forest", "SVM", "XGBoost", "Scikit-learn"],
        "problem": "Security teams were spending time triaging incidents that were ultimately false positives.",
        "architecture": ["Raw Incident Data", "Feature Engineering", "Model Training + Cross-Validation", "Evaluation"],
        "highlights": [
            "Built predictive ML models on a 1M-record dataset",
            "Achieved 87% accuracy predicting false-positive security incidents",
            "Applied A/B testing and feature importance analysis",
            "Extracted time-series features and used cross-validation",
            "Identified MITRE ATT&CK techniques as important predictive features",
        ],
        "metrics": {"Records": "1M", "Accuracy": "87%"},
        "skills": ["Random Forest", "XGBoost", "Feature Importance", "A/B Testing"],
        "links": {},
    },
    {
        "title": "Big Data Analytics for Earnings Prediction",
        "category": "Machine Learning",
        "technologies": ["Apache Spark", "Python", "Scikit-learn"],
        "problem": "Predicting earnings surprises by combining market data with analyst estimates.",
        "architecture": ["Yahoo Finance OHLC Data", "Estimize / Zacks Earnings Data", "Feature Engineering", "Spark MLlib Models"],
        "highlights": [
            "Merged Yahoo Finance OHLC data with Estimize/Zacks earnings data",
            "Engineered moving averages and price/volume momentum features",
            "Compared Logistic Regression, Decision Tree, and Random Forest models in Spark MLlib",
            "Applied cross-validation and evaluated precision, recall, and F1",
        ],
        "metrics": {},
        "skills": ["Apache Spark", "MLlib", "Feature Engineering", "Model Comparison"],
        "links": {},
    },
    {
        "title": "McDonald's Supply Chain Data Management",
        "category": "Database Systems",
        "technologies": ["SQL", "Oracle APEX", "ER Modeling", "Normalization", "Triggers", "Stored Procedures"],
        "problem": "A supply chain domain needed a normalized relational schema with real-time reporting.",
        "architecture": ["ER Model", "Normalized Schema (4NF)", "Triggers / Stored Procedures", "Oracle APEX Reporting"],
        "highlights": [
            "Designed ER models and built a normalized relational schema to 4NF",
            "Developed SQL triggers and stored procedures",
            "Deployed the database in Oracle APEX with real-time reporting",
        ],
        "metrics": {},
        "skills": ["ER Modeling", "Normalization", "PL/SQL", "Oracle APEX"],
        "links": {},
    },
    {
        "title": "Estonia Traffic Violations Analysis",
        "category": "Analytics",
        "technologies": ["Power BI", "SQL", "Python"],
        "problem": "790K traffic violation records needed to be turned into actionable planning insights.",
        "architecture": ["Raw Violation Records", "SQL Analysis", "Power BI Dashboards"],
        "highlights": [
            "Analyzed 790,000 traffic violation records",
            "Evaluated violation patterns and risk using SQL",
            "Built interactive Power BI dashboards",
            "Supported planning and budgeting recommendations",
        ],
        "metrics": {"Records analyzed": "790K"},
        "skills": ["SQL", "Power BI", "Risk Analysis"],
        "links": {},
    },
    {
        "title": "Mobile App Revamp for eSMS",
        "category": "Analytics",
        "technologies": ["SDLC", "UML", "DFD", "ER Modeling", "Prototyping"],
        "problem": "An existing mobile app needed a structured revamp plan grounded in formal SDLC artifacts.",
        "architecture": ["Requirements", "UML / DFD Modeling", "ER Modeling", "Prototyping"],
        "highlights": [
            "Applied SDLC methodology to a mobile app revamp",
            "Built UML and DFD models",
            "Built ER models and prototypes",
        ],
        "metrics": {},
        "skills": ["SDLC", "UML", "DFD", "Prototyping"],
        "links": {},
    },
    {
        "title": "Boeing Board Consulting",
        "category": "Analytics",
        "technologies": ["Financial Modeling", "Strategy"],
        "problem": "Boeing's board needed a cultural transformation strategy backed by financial projections.",
        "architecture": ["Current State Analysis", "Financial Modeling", "Strategic Proposal"],
        "highlights": [
            "Developed a $1.3B cultural transformation proposal",
            "Built financial models projecting $25M net income improvement",
            "Presented strategic recommendations to a board-level audience",
        ],
        "metrics": {"Proposal size": "$1.3B", "Projected net income improvement": "$25M"},
        "skills": ["Financial Modeling", "Strategic Consulting"],
        "links": {},
    },
    {
        "title": "AI-Driven Intrusion Detection for T-Mobile Hybrid Cloud",
        "category": "AI & LLM",
        "technologies": ["AI", "CNN-LSTM", "AWS GuardDuty", "Palo Alto Cortex"],
        "problem": "Hybrid cloud environments need AI-driven threat detection beyond static rule sets.",
        "architecture": ["Network Traffic", "CNN-LSTM Model", "AWS GuardDuty", "Palo Alto Cortex"],
        "highlights": [
            "Focused on AI-driven threat detection for a hybrid cloud environment",
            "Applied a CNN-LSTM architecture for intrusion detection",
            "Integrated with AWS GuardDuty and Palo Alto Cortex",
        ],
        "metrics": {},
        "skills": ["CNN-LSTM", "Cloud Security", "AI/ML"],
        "links": {},
    },
]

CATEGORIES = ["All Projects", "Data Engineering", "Streaming", "Machine Learning", "AI & LLM", "Analytics", "Database Systems"]

EXPERIENCE = [
    {
        "role": "Project Lead",
        "org": "Knowledge Distillation for Airbnb Occupancy Prediction",
        "period": "January 2026 - Present",
        "technologies": ["PyTorch", "FAISS", "RAG", "Python"],
        "highlights": [
            "Designed a three-component knowledge distillation architecture using a 120B LLM teacher augmented with RAG over Reddit QA",
            "Generated structured soft labels for a tabular student neural network predicting 30-day Airbnb occupancy",
            "Built a concept bottleneck student model with a Beta distribution head",
            "Routed predictions through 12 human-interpretable occupancy factors",
            "Implemented an EMA-based Teaching Assistant model tracking concept gaps",
            "Used personalized curriculum learning across 8 KMeans listing profiles",
            "Developed a self-refinement pipeline that updates teacher prompts based on concept gaps",
        ],
    },
    {
        "role": "Graduate Teaching Assistant - Database Management Systems",
        "org": "University of Arizona",
        "period": "August 2025 - December 2025",
        "technologies": [],
        "highlights": [
            "Led labs and office hours for 60+ undergraduate students",
            "Supported ER modeling, normalization, and SQL",
            "Managed D2L content and grading",
            "Mentored students on SQL optimization and data modeling",
            "Implemented systematic quality checks",
        ],
    },
    {
        "role": "Data Analyst",
        "org": "Banner Health",
        "period": "June 2025 - August 2025",
        "technologies": ["Python", "Pandas", "Plotly", "LLM-Powered Insights"],
        "highlights": [
            "Analyzed chronic disease prevalence using CMS and Census datasets",
            "Identified disparities by age, race, and county",
            "Built Python workflows and choropleth visualizations",
            "Analyzed COPD and Hypertension trends",
            "Validated outputs against CDC benchmarks",
            "Built interactive dashboards supporting healthcare outreach and planning",
        ],
    },
    {
        "role": "Team Lead",
        "org": "Arizona Public Service",
        "period": "January 2025 - May 2025",
        "technologies": ["Excel", "Power BI", "Financial Modeling"],
        "highlights": [
            "Led a 6-member consulting team",
            "Evaluated 4 capital projects totaling $250M",
            "Built financial models using ROI and NPV",
            "Identified $1.2M+ in potential annual savings",
            "Created Power BI dashboards for cost, risk, and utilization",
            "Managed timelines and deliverables with MS Project and JIRA",
        ],
    },
    {
        "role": "Business Development Analyst",
        "org": "Zycus Pvt. Ltd. - Mumbai, India",
        "period": "June 2023 - September 2023",
        "technologies": [],
        "highlights": [
            "Used Excel and Salesforce for strategic outreach to 180 clients weekly",
            "Used LinkedIn Sales Navigator for lead generation",
            "Designed Power BI KPI dashboards",
            "Improved workflows using Jira and Trello",
            "Collaborated with data governance teams on client master data consistency",
            "Partnered with product and analytics teams on data lineage documentation",
        ],
    },
]

SKILLS = {
    "Programming & Development": ["Python", "SQL", "React", "FastAPI", "HTML", "CSS", "JavaScript", "C", "C++"],
    "Data & Machine Learning": ["Pandas", "NumPy", "Scikit-learn", "PyTorch", "Hugging Face", "NLP", "Data Mining"],
    "Databases & Data Engineering": ["Oracle SQL", "Amazon Redshift", "Supabase", "Apache Airflow", "Apache Spark", "PySpark", "Delta Lake", "dbt", "BigQuery", "Kafka"],
    "Cloud & Infrastructure": ["AWS S3", "AWS Glue", "AWS Athena", "Docker", "DevOps"],
    "Analytics & Visualization": ["Power BI", "Tableau", "Excel", "Plotly"],
    "AI & LLM Systems": ["RAG", "FAISS", "Knowledge Distillation", "LLM Prompting", "LLM Evaluation", "Model Performance Analysis", "Feature Engineering", "API Integration"],
}

CERTIFICATIONS = [
    "AWS Certified Cloud Practitioner (CLF-C02)",
    "Foundations of Project Management | Google",
    "Teamwork Skills: Communicating Effectively in Groups | University of Colorado Boulder",
    "Python Data Structures | University of Michigan",
]

EDUCATION = [
    {
        "school": "University of Arizona",
        "degree": "Master of Science in Management Information Systems",
        "gpa": "3.89",
        "date": "December 2025",
    },
    {
        "school": "University of Mumbai",
        "degree": "Bachelor of Engineering in Electronics and Computer Science",
        "gpa": "3.47",
        "date": "May 2023",
    },
]

SNAPSHOT_METRICS = [
    {"label": "NYC transportation records processed", "value": "270M+"},
    {"label": "Streaming e-commerce events", "value": "500K"},
    {"label": "Estonia traffic violation records analyzed", "value": "790K"},
    {"label": "Capital projects evaluated", "value": "$250M"},
    {"label": "Potential annual savings identified", "value": "$1.2M+"},
    {"label": "ML model accuracy", "value": "87%"},
]

CONTACT = {
    "name": "Adwait Minde",
    "email": "adwaitm131@gmail.com",
    "linkedin": "https://www.linkedin.com/in/adwait-minde/",
    "github": "https://github.com/AdwaitMinde",
}
