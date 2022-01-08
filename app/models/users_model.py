from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import validates
from app.exceptions.exceptions import (
    InvalidKeyError,
    InvalidTypeError,
    NotAcessibleError,
    UniqueUserError,
)
from werkzeug.security import generate_password_hash, check_password_hash


@dataclass
class Users(db.Model):
    id: int
    name: str
    email: str
  

    __tablename__ = "users"

    id = Column(Integer, primary_key= True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(30), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    

    @validates("email")
    def validate(self, key, email):
        unique_key = Users.query.filter(Users.email == email).one_or_none()
        if unique_key is not None:
            raise UniqueUserError 
        return email
    
 

    @staticmethod
    def validate_register_args(data):
        requested_args = ["name", "email", "password"]

        for item in requested_args:
            if item not in data.keys():
                raise InvalidKeyError

        for item in data.values():
            if type(item) is not str:
                raise InvalidTypeError

        for item in data.keys():
            if item not in requested_args:
                raise InvalidKeyError


    @staticmethod
    def validate_login_args(data):
        requested_args = ["email", "password"]

        for item in requested_args:
            if item not in data.keys():
                raise InvalidKeyError

        for item in data.values():
            if type(item) is not str:
                raise InvalidTypeError

        for item in data.keys():
            if item not in requested_args:
                raise InvalidKeyError

    @staticmethod
    def validate_patch_args(data):
        requested_args = ["name"]

        for item in data.values():
            if type(item) is not str:
                raise InvalidTypeError

        for item in data.keys():
            if item not in requested_args:
                raise InvalidKeyError

    @property
    def password(self):
        raise NotAcessibleError("Password is not accessible")

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def validate_password(self, input_password):
        return check_password_hash(self.password_hash, input_password)
