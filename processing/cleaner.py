import pandas as pd
from core.config import settings
from core.logger import get_logger

logger = get_logger(__name__)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean the dataframe according to configuration settings."""
    initial_len = len(df)
    
    if settings.drop_duplicates:
        df = df.drop_duplicates(subset=['transaction_id'], keep='first')
        logger.info(f"Dropped {initial_len - len(df)} duplicate records based on transaction_id.")
    
    if settings.handle_missing:
        # Fill missing numeric values with 0
        numeric_cols = df.select_dtypes(include=['number']).columns
        df[numeric_cols] = df[numeric_cols].fillna(0)
        
        # Fill missing categorical values with 'Unknown'
        categorical_cols = df.select_dtypes(include=['object']).columns
        df[categorical_cols] = df[categorical_cols].fillna('Unknown')
        logger.info("Handled missing values.")
    
    return df

def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate derived columns."""
    if 'price' in df.columns and 'quantity' in df.columns:
        discount = df['discount'] if 'discount' in df.columns else 0
        df['total_amount'] = df['price'] * df['quantity'] * (1 - discount)
        logger.info("Calculated total_amount feature.")
    
    return df
