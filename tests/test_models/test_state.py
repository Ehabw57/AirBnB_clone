#!/usr/bin/python3
"""Module to test State instances."""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test the State instances."""
    def test_attributes(self):
        """some doki doki here"""
        self.assertTrue(State.name is '')

    def test_inheritance(self):
        """Test that State inherits from BaseModel"""
        self.assertTrue(
                issubclass(State, BaseModel)
                and State is not BaseModel
                )


if __name__ == "___main__":
    unittest.main()
