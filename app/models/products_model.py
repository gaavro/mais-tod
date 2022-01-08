from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship, validates

from app.exceptions.exceptions import (
    InvalidKeyError,
    InvalidTypeError,
    NotFoundError,
    ProductAlreadyExistsError,
)


@dataclass
class Products(db.Model):
    allowed_keys = ["name", "category", "price"]
    id: int
    name: str
    category: str
    price: float

    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    category = Column(String(30), nullable=False)
    price = Column(Float, nullable=False)
   

    @validates("name", "category", "price")
    def validates(self, key, value):
        if key == "name":
            unique_key = Products.query.filter(Products.name == value).one_or_none()
            if unique_key is not None:
                raise ProductAlreadyExistsError
        return value

    def validate_id(current):
        if current is None:
            raise NotFoundError
        if type(current) != Products and len(current) == 0:
            raise NotFoundError

    def validate_keys(data):
        for item in Products.allowed_keys:
            if item not in data.keys():
                raise InvalidKeyError

        for item in data.keys():
            if item not in Products.allowed_keys:
                raise InvalidKeyError
        if (
            type(data["name"]) is not str
            or type(data["category"]) is not str
            or type(data["price"]) is not float
        ):
            raise InvalidTypeError
