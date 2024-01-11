#!/usr/bin/python3
"""Module to create City instances."""
from models.base_model import BaseModel


class City(BaseModel):
    """Create new city."""
    name = ""
    state_id = ""
