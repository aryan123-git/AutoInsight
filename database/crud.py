from sqlalchemy.orm import Session
from database.models import Transaction
from typing import List, Dict

def insert_transactions(db: Session, records: List[Dict]):
    from sqlalchemy.dialects.postgresql import insert
    stmt = insert(Transaction).values(records)
    # On conflict, ignore the new row
    stmt = stmt.on_conflict_do_nothing(index_elements=['transaction_id'])
    
    db.execute(stmt)
    db.commit()

def get_all_transactions(db: Session, skip: int = 0, limit: int = 500):
    return db.query(Transaction).offset(skip).limit(limit).all()

def get_summary_metrics(db: Session):
    from sqlalchemy import func
    total_sales = db.query(func.sum(Transaction.total_amount)).scalar() or 0
    total_transactions = db.query(func.count(Transaction.id)).scalar() or 0
    
    return {
        "total_sales": total_sales,
        "total_transactions": total_transactions
    }
