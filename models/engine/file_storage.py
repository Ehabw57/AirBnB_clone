#!/usr/bin/python3
"""soem fukn docstriong goes here"""
import json

class FileStorage():
    """some freaking doc goes here"""
    __file_path = 'data.json'
    __objects = {}

    def all(self):
        """doooooc"""
        return FileStorage.__objects

    def new(self, obj):
        """doc doc doc"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj
        
    def save(self):
        """doki doki"""
        json_dict = FileStorage.__objects.copy()
        for key, value in json_dict.items():
            json_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as data_json:
           json.dump(json_dict, data_json)

    def reload(self):
        """doco doco"""
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

    def delete(self,obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects.pop(key)
