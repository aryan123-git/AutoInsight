from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from database.db import get_db
from database.crud import get_all_transactions, get_summary_metrics
from api.schemas import TransactionResponse, MetricsResponse

router = APIRouter()

@router.get("/transactions", response_model=List[TransactionResponse])
def read_transactions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Retrieve all transactions with pagination."""
    return get_all_transactions(db, skip=skip, limit=limit)

@router.get("/metrics", response_model=MetricsResponse)
def read_metrics(db: Session = Depends(get_db)):
    """Get summarized business metrics."""
    return get_summary_metrics(db)
