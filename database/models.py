from sqlalchemy import Column, Integer, String, Float, Date
from database.db import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    transaction_id = Column(String, unique=True, index=True)
    date = Column(Date)
    customer_id = Column(String)
    category = Column(String)
    product_name = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
    discount = Column(Float)
    total_amount = Column(Float) # Computed
