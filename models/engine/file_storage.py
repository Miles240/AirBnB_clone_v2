#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
            class_dict = {}
            for k, v in self.__objects.items():
                if isinstance(v, cls):
                    class_dict[k] = v
            return class_dict
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, "w") as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review,
        }
        try:
            if os.path.getsize(FileStorage.__file_path) > 0:
                with open(FileStorage.__file_path, "r") as file:
                    data = json.load(file)
                    for key, value in data.items():
                        cls_name, obj_id = key.split(".")
                        cls_ = eval(cls_name)
                        obj = cls_(**value)
                        FileStorage.__objects[key] = obj
            else:
                return
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes a class and its properties from the object"""
        if obj is not None:
            obj = "{}.{}".format(obj.__class__.__name__, obj.id)
            del self.__objects[obj]

    def close(self):
        """deserializing the JSON file to objects"""
        self.reload()
