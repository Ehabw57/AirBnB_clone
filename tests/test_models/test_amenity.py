#!/usr/bin/python3
"""Module to test Amenity instances."""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test the Amenity instances."""
    def test_attributes(self):
        """some doc here"""
        self.assertTrue(Amenity.name is '')

    def test_inheritance(self):
        """Test that Amenity inherits from BaseModel"""
        self.assertTrue(
                issubclass(Amenity, BaseModel)
                and Amenity is not BaseModel
                )


if __name__ == "___main__":
    unittest.main()
