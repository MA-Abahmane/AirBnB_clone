#!/usr/bin/python3


import json as js
from os import path
import models
from models.base_model import *


class FileStorage:
    """
        class FileStorage serializes instances to a JSON file
        and deserializes JSON file to instances:
    """
    """ Private class attributes """
    __file_path = 'file.json'
    __objects = {}


    def __init__(self):
        """ Consturtor """

        return

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        Id = str(obj.id)
        # The object key consists of its name and id value <obj class name>.id
        key = obj.__class__.__name__ + '.' + Id
        # set the key (<obj class name>.id) as the key of the newly created onject
        self.__objects[key] =  obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        json_obj = {}

        """ 
            after we created the emply dictionary 'json_obj' we will now
            proceed to filling it with all key/value from __objects, then
            we serializes our dictionary and save it into the file
        """
        for key in self.__objects:
            value = self.__objects[key].to_dict()
            json_obj[key] = value

        with open(self.__file_path, 'w') as fl:
            js.dump(json_obj, fl)

        return

    def reload(self):
        """
            deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists
            and save to __objects
        """
        # check if file exists
        if (not path.isfile(self.__file_path)):
            return

        with open(self.__file_path, 'r', encoding="utf-8") as fl:
            # deserializes file contents
            de_jsoned_dict = js.load(fl)
            
            # save file keys/values in __objects()
            for key, val in de_jsoned_dict.items():
                """ 
                The expression value["__class__"] creates an instance with all the
                values passed as instance methods then returns the name of the class
                of the object. The eval() function then evaluates this string as a 
                reference to the class, and the **value syntax passes the value dictionary
                as keyword arguments to the class constructor. This means that the class 
                will be created with the same attributes as the value dictionary. 
                """
                atrbt_val = eval(val["__class__"])(**val)
                self.__objects[key] = atrbt_val