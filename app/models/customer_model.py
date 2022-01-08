from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import validates
from app.exceptions.exceptions import (
    InvalidKeyError,
    InvalidTypeError,
    UniqueUserError, NotFoundError, 
)
import re

@dataclass
class Customer(db.Model):
    id: int
    name: str
    cpf: str
  

    __tablename__ = "customer"

    id = Column(Integer, primary_key= True, autoincrement=True)
    name = Column(String(100), nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
    
    

    @validates("cpf")
    def validate(self, key, cpf):
        regex = r'^[0-9]{11}$'
        result = re.fullmatch(regex, cpf)
        unique_key = Customer.query.filter(Customer.cpf == cpf).one_or_none()
        if not result:
            raise InvalidTypeError        
        if unique_key is not None:
            raise UniqueUserError 
        return cpf 
    
 

    @staticmethod
    def validate_register_args(data):
        requested_args = ["name", "cpf"]

        for item in requested_args:
            if item not in data.keys():
                raise InvalidKeyError

        for item in data.values():
            if type(item) is not str:
                raise InvalidTypeError

        for item in data.keys():
            if item not in requested_args:
                raise InvalidKeyError

    def validate_id(current):
        if current is None:
            raise NotFoundError
        if type(current) != Customer and len(current) == 0:
            raise NotFoundError

    

    

        