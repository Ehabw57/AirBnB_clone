#!/usr/bin/python3
"""Module containing unit tests for the BaseModel class."""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def setUp(self):
        """Set up the test fixtures."""
        self.b1 = BaseModel()
        self.b2 = BaseModel()

    def tearDown(self):
        """Tear down the test fixtures."""
        del self.b1
        del self.b2

    def test_uid(self):
        """Test the uniqueness of the instance IDs."""
        self.assertTrue(isinstance(self.b1.id, str), "ID should be a string")
        self.assertNotEqual(self.b1.id, self.b2.id, "IDs should be different")

    def test_time(self):
        """Test the creation and update times."""
        self.assertNotEqual(
            self.b1.created_at, self.b2.created_at,
            "Instances should have different creation times"
        )
        self.assertNotEqual(
            self.b1.updated_at, self.b2.updated_at,
            "Instances should have different update times"
        )

    def test_str_method(self):
        """Test the __str__ method."""
        name = f"[{self.b1.__class__.__name__}]"
        expected = f"{name} ({self.b1.id}) {self.b1.__dict__}"
        self.assertEqual(str(self.b1), expected,
                         "Output should match the expected string")

    def test_save_method(self):
        """Test the save method."""
        self.assertFalse(
            self.b1.updated_at > self.b2.updated_at,
            "First instance should not be newer than the second instance"
        )
        self.b1.save()
        self.assertTrue(
            self.b1.updated_at > self.b2.updated_at,
            "Save should update the update time"
        )

    def test_dict_method(self):
        """Test the to_dict method."""
        obj_dict = self.b1.to_dict()
        self.assertEqual(
            obj_dict['__class__'], self.b1.__class__.__name__,
            "Class names should match"
        )
        self.assertEqual(
            obj_dict['created_at'], self.b1.created_at.isoformat(),
            "Creation times should match"
        )
        self.assertEqual(
            obj_dict['updated_at'], self.b1.updated_at.isoformat(),
            "Update times should match"
        )

    def test_init(self):
        """Test the __init__ method."""
        obj_dict = self.b1.to_dict()
        self.b0 = BaseModel(**obj_dict)

        for key in obj_dict.keys():
            if key not in ['updated_at', 'created_at', '__class__']:
                self.assertEqual(
                    obj_dict[key], self.b0.__dict__[key],
                    f"Values for key '{key}' should match"
                )

        self.assertEqual(
            type(self.b0.updated_at), type(self.b1.updated_at),
            "Updated time should be an instance of the datetime class"
        )
        self.assertEqual(
            type(self.b0.created_at), type(self.b1.created_at),
            "Creation time should be an instance of the datetime class"
        )
        self.assertFalse('__class__' in self.b0.__dict__)


if __name__ == "__main__":
    unittest.main()
