#!/usr/bin/python3
"""A model storage with a class FileStorage"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.city import City
from models.state import State


class FileStorage:
    """A class that stores instances"""
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """adds a new created instance to object dictionary"""
        # key = f"{obj.__class__name__}.{obj.id}"
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def all(self):
        """Returns all the ojects in the objects dictionary"""
        return FileStorage.__objects

    def save(self):
        """Saves objects stored in object dict to json"""
        all_objects = FileStorage.__objects
        serialized = {}
        for key in all_objects.keys():
            serialized[key] = all_objects[key].to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(serialized, file)

    def reload(self):
        """converts a json file to a python object"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    obj_dict = json.load(file)
                    for key, values in obj_dict.items():
                        cls_name, obj_id = key.split(".")
                        cls = eval(cls_name)
                        instance = cls(**values)
                        FileStorage.__objects[key] = instance
                except Exception:
                    pass
