# GitHub Analytics Pipeline

A data analytics pipeline that extracts GitHub repository language statistics from Google BigQuery, loads the data into PostgreSQL, and generates analytics insights using Python.

## Overview

This project demonstrates an end-to-end data pipeline:

Google BigQuery Public Dataset
        |
        v
Data Extraction
        |
        v
Data Loading Pipeline
        |
        v
PostgreSQL Database
        |
        v
Analytics Queries


The pipeline connects to a public GitHub dataset in BigQuery, processes the data, stores it in PostgreSQL, and performs analytical queries.

## Technologies

- Python 3.12
- Google BigQuery
- PostgreSQL
- SQLAlchemy
- Psycopg 3
- python-dotenv


## Pipeline Workflow

### 1. Extract

The application connects to Google BigQuery using a service account and queries GitHub repository language statistics.

### 2. Load

The extracted data is loaded into PostgreSQL.

The pipeline refreshes the snapshot by clearing previous data and inserting the latest results.

### 3. Analyze

SQL queries generate insights such as:

- Total repositories
- Most popular programming language
- Average repositories per language


## Example Output

Starting Analytics Pipeline

Database connection successful

Tables created successfully

Data loaded successfully


Analytics Result
----------------

Total repositories: 5531493

Top language:
JavaScript (1099966)

Average repositories:
553149.3


## Setup

Create a virtual environment:

python -m venv venv


Install dependencies:

pip install -r requirements.txt


Create a `.env` file:

DATABASE_URL=postgresql://username:password@localhost:5432/database_name

GOOGLE_APPLICATION_CREDENTIALS=credentials/service-account.json


Run the pipeline:

python -m app.main


## Security

Sensitive configuration is stored outside the source code.

Ignored files:

.env
credentials/
venv/

Environment variables are loaded using python-dotenv.

## Future Improvements

- Add more GitHub metrics
- Add visualization dashboard
- Add scheduled pipeline execution
- Add automated tests
- Add API endpoints
- Add Docker support