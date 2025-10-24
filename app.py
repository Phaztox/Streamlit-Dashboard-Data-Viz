import streamlit as st
import pandas as pd
from utils.io import load_data
from utils.prep import prepare_data, create_analysis_tables
from utils.viz import create_salary_chart, create_conditions_chart, create_map_chart, create_experience_distribution
from sections import intro, overview, deep_dives, conclusions

st.set_page_config(
    page_title="Digital Talent in Public Sector Dashboard",
    layout="wide"
)

@st.cache_data(show_spinner=False)
def get_data():
    data_raw=load_data()
    data_clean=prepare_data(data_raw)
    tables=create_analysis_tables(data_clean)
    return data_raw, data_clean, tables

st.title("Digital Talent and Public Service: Understand the Gap")
st.caption("Source: Sondage métiers numériques - data.gouv.fr")

intro.render()

with st.sidebar:
    st.header("Filters")
    raw_data, clean_data, analysis_tables=get_data()
    
    all_genders=clean_data['radio-genre'].dropna().unique().tolist()
    all_genders_sorted=sorted(all_genders)
    gender_options=["All"]+all_genders_sorted
    selected_gender=st.selectbox("Gender", gender_options)
    
    min_exp=int(clean_data['number-experience'].min())
    max_exp=int(clean_data['number-experience'].max())
    exp_range=st.slider(
        "Years of Experience",
        min_value=min_exp,
        max_value=max_exp,
        value=(min_exp, max_exp)
    )

    all_jobs=clean_data['radio-metiers'].dropna().unique().tolist()
    all_jobs_sorted=sorted(all_jobs)
    job_options=["All"]+all_jobs_sorted
    selected_job=st.selectbox("Job Type", job_options)

filtered_data=clean_data.copy()

if selected_gender != "All":
    filtered_data=filtered_data[filtered_data['radio-genre'] == selected_gender]

filtered_data=filtered_data[filtered_data['number-experience'] >= exp_range[0]]
filtered_data=filtered_data[filtered_data['number-experience'] <= exp_range[1]]

if selected_job != "All":
    filtered_data=filtered_data[filtered_data['radio-metiers'] == selected_job]

st.subheader("Key Metrics")
col1, col2, col3=st.columns(3)

average_salary=filtered_data['number-salaire-souhait'].mean()
col1.metric("Average Desired Salary", f"€{average_salary:,.0f}")

total_people=len(filtered_data)
col2.metric("Total Respondents", f"{total_people}")

average_exp=filtered_data['number-experience'].mean()
col3.metric("Average Experience (years)", f"{average_exp:.1f}")


overview.render(filtered_data, analysis_tables)
deep_dives.render(filtered_data)
conclusions.render(filtered_data)

st.markdown("---")
st.markdown("### Data Quality and Limitations")
st.info("""
- Survey conducted in 2019, responses are self-reported
- Geographic data is text-based and may contain inconsistencies  
- Missing values exist in some fields and are handled through filtering
- Salary data represents expectations, not actual compensation
- The size of the database is quite restricted 
""")