# Digital Talent in Public Sector - Data Analysis Dashboard

## Overview

Interactive Streamlit dashboard analyzing survey data from digital professionals interested in public sector careers in France.

## Requirements

streamlit </br>
pandas </br>
numpy </br>
plotly </br>

## Running the Application

streamlit run app.py

## Project Structure

streamlit-survey-project/ </br>
├── app.py                 # Main application </br>
├── README.md             # Documentation </br>
├── data/ </br>
│   └── sondage-metiers-numeriques.csv </br>
├── sections/ </br>
│   ├── intro.py          # Context and objectives </br>
│   ├── overview.py       # High-level insights </br>
│   ├── deep_dives.py     # Detailed analysis </br>
│   └── conclusions.py    # Findings and recommendations </br>
└── utils/ </br>
    ├── io.py             # Data loading functions </br>
    ├── prep.py           # Data preparation and cleaning </br>
    └── viz.py            # Visualization functions </br>


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



