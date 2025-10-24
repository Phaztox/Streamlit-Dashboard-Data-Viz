import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    """Load the survey data from CSV file"""
    data=pd.read_csv('data/sondage-metiers-numeriques.csv')
    return data

def get_data_license():
    """Return license information as text"""
    license_text="""
    License: Open License
    Source: data.gouv.fr
    Dataset: Sondage métiers numériques
    Year: 2019
    """
    return license_text