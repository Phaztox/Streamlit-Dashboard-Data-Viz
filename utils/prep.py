import pandas as pd
import numpy as np

def prepare_data(data):
    """Clean and prepare the dataset"""
    clean_data=data.copy()
    clean_data['number-salaire-min']=pd.to_numeric(clean_data['number-salaire-min'], errors='coerce')
    clean_data['number-salaire-souhait']=pd.to_numeric(clean_data['number-salaire-souhait'], errors='coerce')
    clean_data['number-experience']=pd.to_numeric(clean_data['number-experience'], errors='coerce')
    clean_data['date']=pd.to_datetime(clean_data['date'], errors='coerce')
    clean_data['radio-genre'].fillna('Non spécifié', inplace=True)
    clean_data['radio-metiers'].fillna('Autre', inplace=True)   
    return clean_data

def create_analysis_tables(data):
    """Create summary tables for visualizations"""
    tables={}    
    salary_table=data.groupby('radio-metiers').agg({
        'number-salaire-souhait': 'mean',
        'number-salaire-min': 'mean'
    })
    salary_table=salary_table.round(0)
    salary_table=salary_table.reset_index()
    tables['salary_by_job']=salary_table

    exp_table=data.groupby('number-experience').size()
    exp_table=exp_table.reset_index(name='count')
    tables['experience_dist']=exp_table
    
    gender_table=data.groupby('radio-genre').size()
    gender_table=gender_table.reset_index(name='count')
    tables['gender_dist']=gender_table
    
    contract_table=data.groupby('radio-type-contrat').size()
    contract_table=contract_table.reset_index(name='count')
    tables['contract_type']=contract_table
    
    ministries_split=data['checkbox-themes'].str.split(',')
    ministries_expanded=ministries_split.explode()
    ministries_cleaned=ministries_expanded.str.strip()
    ministries_count=ministries_cleaned.value_counts()
    ministries_table=ministries_count.reset_index()
    ministries_table.columns=['ministry', 'count']
    tables['ministries']=ministries_table
    
    conditions_split=data['checkbox-acceptation'].dropna().str.split(',')
    conditions_expanded=conditions_split.explode()
    conditions_cleaned=conditions_expanded.str.strip()
    conditions_count=conditions_cleaned.value_counts()
    conditions_table=conditions_count.reset_index()
    conditions_table.columns=['condition', 'count']
    tables['conditions']=conditions_table
    
    return tables

def extract_location_data(data):
    """Extract and count location preferences"""
    locations_split=data['text-lieu'].dropna().str.split(',')
    locations_expanded=locations_split.explode()
    locations_cleaned=locations_expanded.str.strip()
    location_counts=locations_cleaned.value_counts()
    location_table=location_counts.reset_index()
    location_table.columns=['location', 'count']   
    return location_table