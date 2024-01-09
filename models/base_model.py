#!/usr/bin/python3 
"""some docstring goes here"""
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """some docment goes here"""
    def __init__(self, *args, **kwargs):
        """this is some doc test"""
        if kwargs:
            for key in kwargs.keys():
                if key != "__class__":
                    self.__dict__[key] = kwargs[key]
            self.updated_at = datetime.fromisoformat(self.updated_at)
            self.created_at = datetime.fromisoformat(self.created_at)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """soem docstring goes here"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """some docs string goes here"""
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """somedoctstring goes here"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
