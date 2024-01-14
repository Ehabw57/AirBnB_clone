#!/usr/bin/python3
"""Module containing the FileStorage class for persisting data to JSON."""
import json


class FileStorage():
    """Class for serializing and deserializing instances to and from JSON.

    Attributes:
        __file_path (str): The path to the JSON file.
        __objects (dict): A dictionary containing all serializable objects.
    """

    __file_path = 'Data.json'
    __objects = {}

    def all(self):
        """Return the dictionary of all serialized objects.

        Returns:
            dict: Dictionary containing all serialized objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """Add a new serialized object to the dictionary.

        Args:
            obj: The object to be serialized and added to the dictionary.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize objects and save them to the JSON file."""
        json_dict = FileStorage.__objects.copy()
        for key, value in json_dict.items():
            json_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as data_json:
            json.dump(json_dict, data_json)

    def reload(self):
        """Deserialize objects from the JSON file and creat the dictionary"""
        from models.base_model import BaseModel
        from models.user import User
        from models.city import City
        from models.place import Place
        from models.state import State
        from models.review import Review
        from models.amenity import Amenity

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "City": City,
            "Place": Place,
            "State": State,
            "Review": Review,
            "Amenity": Amenity
        }
        try:
            with open(FileStorage.__file_path, 'r') as data_json:
                FileStorage.__objects = json.load(data_json)
                for k, v in FileStorage.__objects.items():
                    FileStorage.__objects[k] = classes[v['__class__']](**v)
        except FileNotFoundError:
            FileStorage.__objects = {}

    def delete(self, obj):
        """Remove the serialized object from the dictionary.

        Args:
            obj: The object to be removed from the dictionary.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects.pop(key)
