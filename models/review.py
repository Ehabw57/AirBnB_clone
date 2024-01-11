#!/usr/bin/python3
"""Module to create Review instances."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Create new review."""
    place_id = ""
    user_id = ""
    text = ""
