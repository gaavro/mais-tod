from sqlalchemy import Column, Integer, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from app.configs.database import db
from dataclasses import dataclass
from datetime import datetime
from app.exceptions.exceptions import (
    InvalidKeyError,
    InvalidTypeError,
     NotFoundError, UniqueUserError
)
import re
from sqlalchemy.orm import validates
from app.models.products_model import Products
from app.models.users_model import Users

@dataclass
class ProductsUser(db.Model): 
    allowed_keys = [ "cpf", "qty"]
    id: int
    sold_at: str
    total: float
    users_id: Users
    qty: int
    

    __tablename__ = 'products_user'

    
    id = Column(Integer, primary_key=True)
    sold_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    total = Column(Float)
    users_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    cashback= Column(Float)
    qty = Column(Integer, default= 1)
    products = relationship('Products', backref='products', uselist=True)
    users = relationship('Users', backref='users', uselist=False)
    

    @validates("cpf")
    def validate(self, key, cpf):
        regex = r'^[0-9]{11}$'
        result = re.fullmatch(regex, cpf)
        unique_key = Users.query.filter(Users.cpf == cpf).one_or_none()
        if not result:
            raise InvalidTypeError        
        if unique_key is not None:
            raise UniqueUserError 
        return cpf 

    def validate_id(current):
        if current is None:
            raise NotFoundError
        if type(current) != ProductsUser and len(current) == 0:
            raise NotFoundError


    @staticmethod
    def validate_keys(data):
        for item in ProductsUser.allowed_keys:
            if item not in data.keys():
                raise InvalidKeyError

        for item in data.keys():
            if item not in ProductsUser.allowed_keys:
                raise InvalidKeyError
        if (
            type(data["qty"]) is not int
            or type(data["cpf"]) is not str
        ):
            raise InvalidTypeError
