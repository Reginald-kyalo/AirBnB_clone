#!/usr/bin/python3
"""Defines the FileStorage class."""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Sets up attributes and methods for storage
    for serializing and deserializing hbnb instances

    Returns:
        file_path (str): path to json file
        objects (dict): dictionary of instances to serialize into json
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns dictionary of available instances"""
        return FileStorage.__objects

    def new(self, obj):
        """Saves created instances to objects and sets custom key"""
        my_key = obj.__class__.__name__ + '.' + str(obj.id)
        FileStorage.__objects[my_key] = obj

    def save(self):
        """Serializes objects to json file"""
        obj = FileStorage.__objects
        with open(FileStorage.__file_path, "w") as json_file:
            objdict = {key: value.to_dict() for key, value in obj.items()}
            json.dump(objdict, json_file, indent=4)

    def reload(self):
        """Deserializes json file to objects dictionary"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as json_file:
                objdict = json.load(json_file)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    self.new(eval(cls_name)(**o))
        else:
            pass
