import streamlit as st

def render():
    st.markdown("## Context and Objectives")
    st.markdown("""
    ### The Challenge
    The French public sector struggles to attract and retain digital talent in a competitive market.
    This analysis examines survey responses from tech professionals interested in public service to identify:
    - Expected salary ranges by role
    - Critical work conditions and benefits
    - Geographic and sectoral preferences
    - Motivations and barriers to public sector employment
    
    ### Research Questions
    1. What salary expectations do digital professionals have for public sector roles?
    2. Which work conditions are most important when considering public employment?
    3. Which government sectors attract the most interest from tech talent?
    4. How do preferences vary by experience level and specialization?

    ### The Goal
    This project aims to understand what matters most to digital workers in the public sector such as 
    career growth, work flexibility, pay, and company culture by talking to recruitment officers and managers. 
    By discovering what workers actually want and comparing it to what organizations currently offer, 
    this project will help public sector employers create better strategies to attract and keep talented digital workers.
    
    ### Data Overview
    The dataset contains responses from a 2019 survey of digital professionals.
    Fields include demographic information, salary expectations, work preferences, and sector interests.
    """)
    st.markdown("---")