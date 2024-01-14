#!/usr/bin/python3
"""Module to test Review instances."""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test the Review instances."""
    def test_attributes(self):
        """some doc here"""
        self.assertTrue(Review.text is '')
        self.assertTrue(Review.place_id is '')
        self.assertTrue(Review.user_id is "")

    def test_inheritance(self):
        """Test that Review inherits from BaseModel"""
        self.assertTrue(
                issubclass(Review, BaseModel)
                and Review is not BaseModel
                )


if __name__ == "___main__":
    unittest.main()
