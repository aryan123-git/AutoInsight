from pydantic import BaseModel
from typing import Optional
from datetime import date

class TransactionResponse(BaseModel):
    id: int
    transaction_id: str
    date: date
    customer_id: Optional[str]
    category: Optional[str]
    product_name: Optional[str]
    price: Optional[float]
    quantity: Optional[int]
    discount: Optional[float]
    total_amount: Optional[float]

    class Config:
        from_attributes = True

class MetricsResponse(BaseModel):
    total_sales: float
    total_transactions: int
