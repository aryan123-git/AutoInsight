# AutoInsight — Automated Data Pipeline & Analytics Engine

AutoInsight is an end-to-end data pipeline system that ingests raw data, processes it, stores it in a database, and provides insights through RESTful APIs and an interactive Dashboard.

## Tech Stack
- **Python** (Core language)
- **Pandas** (Data cleaning, feature engineering)
- **PostgreSQL & SQLAlchemy** (Data storage and ORM)
- **FastAPI** (REST API Backend)
- **Plotly Dash** (Interactive Dashboard)
- **APScheduler** (Lightweight pipeline scheduling)
- **Docker** (For PostgreSQL quick setup)

## Directory Structure
```text
AutoInsight/
├── api/             # FastAPI REST endpoints
├── core/            # Configuration and Logging
├── dashboard/       # Plotly Dash Frontend
├── database/        # Database setup and CRUD operations
├── ingestion/       # CSV Data loader
├── pipeline/        # APScheduler ETL Job
├── processing/      # Pandas data cleaner
├── data/            # Local data folder
```

## Setup Instructions

### 1. Prerequisites
- Python 3.10+
- Docker (optional, but highly recommended for starting PostgreSQL)

### 2. Environment Setup
Create a virtual environment and install dependencies:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Database Setup (Docker)
Ensure Docker is running, then start the PostgreSQL container:
```bash
docker-compose up -d
```
The database connection string is already configured in `.env`.

### 4. Running the Services
The project consists of 3 services. You should open 3 separate terminals (with the virtual environment activated in each):

**Terminal 1: Start the Data Pipeline**
This will immediately process `data/sample_data.csv` and insert it into the database, then run every 1 minute.
```bash
python run_pipeline.py
```

**Terminal 2: Start the FastAPI Backend**
This will start the REST API.
```bash
python run_api.py
```
> View the automated Swagger documentation at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

**Terminal 3: Start the Dash Frontend**
This will start the interactive dashboard.
```bash
python run_dashboard.py
```
> View the live dashboard at: [http://127.0.0.1:8050](http://127.0.0.1:8050)

## Extending the Project
- **New Data**: Add new CSVs to the `data/` folder and modify `run_pipeline.py` to point to the new files.
- **New Metrics**: Update `database/crud.py` to compute new metrics, expose them via `api/routes.py`, and display them in `dashboard/layout.py`.
