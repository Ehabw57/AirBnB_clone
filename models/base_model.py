#!/usr/bin/python3
"""Module containing the BaseModel class."""
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """Base class for all models in the Airbnb website."""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of the BaseModel class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
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
        """Return a string representation of the BaseModel.

        Returns:
            str: [<class_name>] (<instance_id>) <instance_attrs>"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """Update the 'updated_at' attribute and save BaseModel instances"""
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel.

        Returns:
            dict: Dictionary representation of the BaseModel.
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
