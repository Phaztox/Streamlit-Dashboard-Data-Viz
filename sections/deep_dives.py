import streamlit as st
from utils.viz import create_conditions_chart, create_map_chart, create_ministry_chart
from utils.prep import extract_location_data, create_analysis_tables

def render(data):
    st.markdown("## Detailed Analysis")
    st.markdown("### Work Conditions and Benefits")
    conditions_chart=create_conditions_chart(data)
    st.plotly_chart(conditions_chart, use_container_width=True)
    st.caption("Most frequently mentioned work conditions and requirements")
    st.warning("""
    Remote work flexibility and autonomy in technology choices are mentioned by over 60% of respondents.
    These factors appear critical for attracting digital talent to the public sector.
    """)
    
    st.markdown("### Government Sector Preferences")
    tables=create_analysis_tables(data)
    ministry_chart=create_ministry_chart(tables)
    st.plotly_chart(ministry_chart, use_container_width=True)
    st.caption("Ministries and sectors with highest interest from digital professionals")

    st.markdown("### Geographic Preferences")
    location_data=extract_location_data(data)
    location_chart=create_map_chart(location_data)
    st.plotly_chart(location_chart, use_container_width=True)
    st.caption("Preferred work locations mentioned in survey responses")

    col1, col2=st.columns(2)
    with col1:
        st.markdown("### Contract Type Preferences")
        contract_counts=data['radio-type-contrat'].value_counts()
        st.bar_chart(contract_counts)
        st.caption("Preferred employment contract types")
    with col2:
        st.markdown("### Primary Motivations")
        motivations_split=data['checkbox-pourquoi'].str.split(',')
        motivations_expanded=motivations_split.explode()
        motivations_cleaned=motivations_expanded.str.strip()
        motivations_counts=motivations_cleaned.value_counts()
        top_motivations=motivations_counts.head(8)
        st.bar_chart(top_motivations)
        st.caption("Main reasons for considering public sector employment")