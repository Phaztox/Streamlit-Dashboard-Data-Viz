# Digital Talent in Public Sector - Data Analysis Dashboard

## Overview

Interactive Streamlit dashboard analyzing survey data from digital professionals interested in public sector careers in France.

## Requirements

streamlit
pandas
numpy
plotly

## Running the Application

streamlit run app.py

## Project Structure

streamlit-survey-project/
├── app.py                 # Main application
├── README.md             # Documentation
├── data/
│   └── sondage-metiers-numeriques.csv
├── sections/
│   ├── intro.py          # Context and objectives
│   ├── overview.py       # High-level insights
│   ├── deep_dives.py     # Detailed analysis
│   └── conclusions.py    # Findings and recommendations
└── utils/
    ├── io.py             # Data loading functions
    ├── prep.py           # Data preparation and cleaning
    └── viz.py            # Visualization functions


## Features

- Interactive filtering by gender, experience, and job type
- Salary analysis across different roles
- Work condition preferences visualization
- Geographic and sectoral preferences
- Ministry/sector attractiveness comparison

## Data Source

- Dataset: Sondage métiers numériques
- Source: data.gouv.fr
- License: Open License
- Collection Year: 2019

## Technical Stack

- Python 3.8+
- Streamlit 1.33.0
- Pandas for data manipulation
- Plotly for interactive visualizations
- NumPy for numerical operations


