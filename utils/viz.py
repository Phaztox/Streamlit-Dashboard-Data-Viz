import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def create_salary_chart(data):
    """Create a chart comparing salaries by job type"""
    salary_summary=data.groupby('radio-metiers').agg({
        'number-salaire-souhait': 'mean',
        'number-salaire-min': 'mean'
    })
    salary_summary=salary_summary.round(0)
    salary_summary=salary_summary.reset_index()
    salary_summary=salary_summary.sort_values('number-salaire-souhait', ascending=True)
    
    figure=go.Figure()
    figure.add_trace(go.Bar(
        y=salary_summary['radio-metiers'],
        x=salary_summary['number-salaire-min'],
        name='Minimum Salary',
        orientation='h',
        marker=dict(color='#85C1E2')
    ))
    figure.add_trace(go.Bar(
        y=salary_summary['radio-metiers'],
        x=salary_summary['number-salaire-souhait'],
        name='Desired Salary',
        orientation='h',
        marker=dict(color='#1F77B4')
    ))
    figure.update_layout(
        title='Salary Expectations by Job Type',
        xaxis_title='Annual Salary (EUR)',
        yaxis_title='Job Type',
        barmode='group',
        height=500
    )
    return figure

def create_conditions_chart(data):
    """Create a chart showing work condition preferences"""
    conditions_split=data['checkbox-acceptation'].str.split(',')
    conditions_expanded=conditions_split.explode()
    conditions_cleaned=conditions_expanded.str.strip()
    conditions_count=conditions_cleaned.value_counts()

    top_conditions=conditions_count.head(10)

    figure=px.bar(
        x=top_conditions.values,
        y=top_conditions.index,
        orientation='h',
        title='Top 10 Desired Work Conditions',
        labels={'x': 'Number of Respondents', 'y': 'Work Condition'}
    )
    figure.update_layout(
        height=500,
        yaxis={'categoryorder': 'total ascending'}
    )
    return figure

def create_map_chart(location_data):
    """Create a chart showing location preferences"""

    top_locations=location_data.head(15)

    figure=px.bar(
        top_locations,
        x='count',
        y='location',
        orientation='h',
        title='Top 15 Preferred Work Locations',
        labels={'count': 'Number of Respondents', 'location': 'Location'}
    )
    figure.update_layout(
        height=500,
        yaxis={'categoryorder': 'total ascending'}
    )
    return figure

def create_experience_distribution(data):
    """Create a histogram of experience distribution"""
    
    figure=px.histogram(
        data,
        x='number-experience',
        nbins=30,
        title='Distribution of Professional Experience',
        labels={'number-experience': 'Years of Experience', 'count': 'Frequency'}
    )
    figure.update_layout(height=400)
    return figure

def create_ministry_chart(tables):
    """Create a chart showing ministry preferences"""

    top_ministries=tables['ministries'].head(10)

    figure=px.bar(
        top_ministries,
        x='count',
        y='ministry',
        orientation='h',
        title='Most Attractive Government Sectors',
        labels={'count': 'Number of Respondents', 'ministry': 'Ministry/Sector'}
    )
    figure.update_layout(
        height=500,
        yaxis={'categoryorder': 'total ascending'}
    )
    return figure