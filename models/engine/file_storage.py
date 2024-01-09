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
        FileStorage.__objects[key] = obj.to_dict()
        
    def save(self):
        """doki doki"""
        with open(FileStorage.__file_path, 'w') as data_json:
           json.dump(FileStorage.__objects, data_json)

    def reload(self):
        """doco doco"""
        try:
            with open(FileStorage.__file_path, 'r') as data_json:
                FileStorage.__objects = json.load(data_json)
        except FileNotFoundError:
            pass
        except Exception:
            pass
        
