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
        for key in json_dict.keys():
            json_dict[key] = json_dict[key].to_dict()

        with open(FileStorage.__file_path, 'w') as data_json:
           json.dump(json_dict, data_json)

    def reload(self):
        """doco doco"""
        from models.base_model import BaseModel
        try:
            with open(FileStorage.__file_path, 'r') as data_json:
                FileStorage.__objects = json.load(data_json)
        except FileNotFoundError:
            pass
        except Exception:
            pass
        for key in FileStorage.__objects.keys():
            FileStorage.__objects[key] = BaseModel(**FileStorage.__objects[key])

        
