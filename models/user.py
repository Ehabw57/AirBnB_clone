#!/usr/bin/python3
"""Module to create User instances."""
from models.base_model import BaseModel


class User(BaseModel):
    """Create new user """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
