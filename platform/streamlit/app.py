import streamlit as st

st.set_page_config(
    page_title="DataTopics • Data Engineering",
    page_icon="⚽",
    layout="wide",
)

st.title("DataTopics • Data Engineering")

st.markdown(
    """
Modern, open source and hands-on data engineering course focused on real-world engineering practices.
"""
)

st.divider()

st.header("Environment Status")

st.success("Streamlit container is running successfully.")

st.divider()

st.header("Course Progress")

st.markdown(
    """
- ⬜ Module 00 • Foundations
- ⬜ Module 01 • SQL
- ⬜ Module 02 • Data Modeling
- ⬜ Module 03 • Batch Processing
- ⬜ Module 04 • Spark
- ⬜ Module 05 • dbt
- ⬜ Module 06 • Airflow
- ⬜ Module 07 • Streaming
- ⬜ Module 08 • Lakehouse
- ⬜ Module 09 • Operations
- ⬜ Module 10 • Final Project
"""
)

st.divider()

st.info("The platform will evolve progressively throughout the course.")