#!/usr/bin/python3
"""some docstring goes here"""
import uuid
from datetime import datetime

class BaseModel():
    def __init__(self):
        """this is some doc test"""
        self.id = str(uuid.uuid4)
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def __str__(self):
        """soem docstring goes here"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")
    
    def save(self):
         """some docs string goes here"""
         self.updated_at = datetime.now()
    
    def to_dict(self):
        """somedoctstring goes here"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
        
    