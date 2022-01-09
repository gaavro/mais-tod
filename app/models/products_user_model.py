from sqlalchemy import Column, Integer, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from app.configs.database import db
from dataclasses import dataclass
from datetime import datetime

from .customer_model import Customer


@dataclass
class ProductsUser(db.Model): 
    id: int
    sold_at: str
    total: float
    customer_id: Customer
    qty: int

    __tablename__ = 'products_user'

    id = Column(Integer, primary_key=True)
    sold_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    total = Column(Float)
    customer_id = Column(Integer, ForeignKey('customer.id'), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    qty = Column(Integer, default= 1)
    customer = relationship('Customer', backref='customer', uselist=False)