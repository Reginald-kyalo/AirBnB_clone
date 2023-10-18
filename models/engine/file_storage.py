#!/usr/bin/python3
"""Defines the FileStorage class."""

import json
import os


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        my_key = obj.__class__.name + '.' + str(obj.id)
        FileStorage.__objects[my_key] = obj

    def save(self):
            obj = FileStorage.__objects
            with open(FileStorage.__file_path, "w") as json_file:
                objdict = {key: value.__dict__ for key, value in obj.items()}
                json.dump(objdict, json_file)

    def reload(self):
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as json_file:
                objdict = json.load(json_file)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    self.new(eval(cls_name)(**o))
        else:
            pass
