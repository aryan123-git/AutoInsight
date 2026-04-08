import os
import time
from apscheduler.schedulers.background import BackgroundScheduler

from database.db import SessionLocal, Base, engine
from database.crud import insert_transactions
from ingestion.ingestor import load_data
from processing.cleaner import clean_data, feature_engineering
from core.logger import get_logger

logger = get_logger(__name__)

def run_pipeline(csv_path: str):
    logger.info("Starting ETL Pipeline run...")
    
    # Ensure tables exist
    Base.metadata.create_all(bind=engine)
    
    if not os.path.exists(csv_path):
        logger.warning(f"File not found: {csv_path}. Pipeline job skipping.")
        return

    # Extract
    df = load_data(csv_path)
    
    # Transform
    df_cleaned = clean_data(df)
    df_final = feature_engineering(df_cleaned)
    
    # Load
    result_records = df_final.to_dict(orient="records")
    
    db = SessionLocal()
    try:
        insert_transactions(db, result_records)
        logger.info(f"Successfully loaded or skipped {len(result_records)} records into the database.")
    except Exception as e:
        logger.error(f"Failed to insert records: {e}")
    finally:
        db.close()
        
    logger.info("ETL Pipeline completed successfully.")

def start_scheduler(csv_path: str="data/sample_data.csv", interval_minutes: int=1):
    scheduler = BackgroundScheduler()
    scheduler.add_job(run_pipeline, 'interval', minutes=interval_minutes, args=[csv_path])
    scheduler.start()
    logger.info(f"Scheduler started. Pipeline runs every {interval_minutes} minute(s).")
    
    # Run once initially
    run_pipeline(csv_path)
    
    try:
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        logger.info("Scheduler stopped.")

if __name__ == "__main__":
    # Ensure working from project root when running directly
    start_scheduler()
