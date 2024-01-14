#!/usr/bin/python3
"""Module to test Place instances."""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test the Place instances."""
    def test_attributes(self):
        """some doc here"""
        self.assertTrue(Place.name is '')
        self.assertTrue(Place.city_id is '')
        self.assertTrue(Place.user_id is "")
        self.assertTrue(Place.description is "")
        self.assertTrue(Place.number_rooms is 0)
        self.assertTrue(Place.number_bathrooms is 0)
        self.assertTrue(Place.max_guest is 0)
        self.assertTrue(Place.price_by_night is 0)
        self.assertTrue(Place.latitude is 0.0)
        self.assertTrue(Place.longitude is 0.0)
        self.assertTrue(Place.amenity_ids is [])

    def test_inheritance(self):
        """Test that Place inherits from BaseModel"""
        self.assertTrue(
                issubclass(Place, BaseModel)
                and Place is not BaseModel
                )


if __name__ == "___main__":
    unittest.main()
