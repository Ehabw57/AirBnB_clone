#!/usr/bin/python3
"""Module to test City instances."""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test the City instances."""
    def test_attributes(self):
        """some doc here"""
        self.assertTrue(City.name is '')
        self.assertTrue(City.state_id is '')

    def test_inheritance(self):
        """Test that City inherits from BaseModel"""
        self.assertTrue(
                issubclass(City, BaseModel)
                and City is not BaseModel
                )


if __name__ == "___main__":
    unittest.main()
