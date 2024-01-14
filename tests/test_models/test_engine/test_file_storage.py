#!/usr/bin/python3
"""Module fo testing file_storage module in the airbnb project"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test suite for the FileStorage class, with no instance created"""
    def test_path(self):
        """File path should be string and ends with .json"""
        self.assertTrue(isinstance(FileStorage._FileStorage__file_path, str),
                        "__file_path should be string")
        self.assertTrue(FileStorage._FileStorage__file_path.endswith('.json'),
                        "file extention should be .json")

    def test_objects(self):
        """before creating any instance, __objects should be empty dict"""
        self.assertTrue(
                isinstance(FileStorage._FileStorage__objects, dict),
                "__objects must be a dictionary"
                )


class TestFileStorageInstance(unittest.TestCase):
    """Test suite for an instance of the FileStorage class"""
    def setUp(self):
        """Setting up instances form the test"""
        self.storage = FileStorage()
        self.storage.reload()

    def tearDown(self):
        """what happens after all tests"""
        del self.storage

    def test_path(self):
        """File path should be string and ends with .json"""
        self.assertTrue(isinstance(FileStorage._FileStorage__file_path, str),
                        "__file_path should be string")
        self.assertTrue(FileStorage._FileStorage__file_path.endswith('.json'),
                        "file extention should be .json")

    def test_all_method(self):
        """test for storage.all() method"""
        self.assertTrue(
                isinstance(self.storage.all(), dict),
                "storage.all() must return a dictionary"
                )

    def test_new_method(self):
        """test for storage.new() method"""
        old_length = len(self.storage.all())
        b1 = BaseModel()
        self.storage.new(b1)
        new_length = len(self.storage.all())
        self.assertTrue(
                new_length == old_length + 1,
                "storage.new() is not adding to the __objects"
                )
        b1_from_storage = self.storage.all()[f'BaseModel.{b1.id}']
        self.assertTrue(
                b1_from_storage is b1,
                "storage.new() should add the object as it is in __objects"
                )

    def test_reload_method(self):
        """Tests for the method reload()"""
        b1 = BaseModel()
        self.storage.new(b1)
        self.storage.save()
        self.storage.reload()
        b1_repr = FileStorage._FileStorage__objects[f"BaseModel.{b1.id}"]
        self.assertTrue(isinstance(
            b1_repr, BaseModel),
                        "Reloade objects should be inctance of it's class")
        self.assertTrue(b1_repr.to_dict() == b1.to_dict())
        b1.name = "My b1 model"
        self.assertFalse(b1_repr.to_dict() == b1.to_dict())


if __name__ == "___main__":
    unittest.main()
