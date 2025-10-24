import streamlit as st
from utils.viz import create_salary_chart, create_experience_distribution

def render(data, tables):
    st.markdown("## High-Level Trends")
    col1, col2=st.columns(2)

    with col1:
        st.markdown("### Job Type Distribution")
        job_counts=data['radio-metiers'].value_counts()
        top_jobs=job_counts.head(10)
        st.bar_chart(top_jobs)
        st.caption("Top 10 job types among respondents")
    
    with col2:
        st.markdown("### Gender Distribution")
        gender_counts=data['radio-genre'].value_counts()
        st.bar_chart(gender_counts)
        st.caption("Gender breakdown of survey participants")
    
    st.markdown("### Salary Expectations by Role")
    salary_chart=create_salary_chart(data)
    st.plotly_chart(salary_chart, use_container_width=True)
    st.caption("Comparison of minimum acceptable and desired salaries across job types")
    
    st.markdown("### Experience Distribution")
    experience_chart=create_experience_distribution(data)
    st.plotly_chart(experience_chart, use_container_width=True)
    st.caption("Years of professional experience among respondents")
    
    st.info("""
    Most respondents have 5-15 years of experience. Fullstack developers and data scientists 
    represent the largest job categories. Average salary expectations range from €35,000 to €50,000 
    depending on specialization.
    """)