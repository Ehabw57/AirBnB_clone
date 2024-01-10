"""Module to create user instances."""
from models.base_model import BaseModel

class User(BaseModel):
    """Class of User instances"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
