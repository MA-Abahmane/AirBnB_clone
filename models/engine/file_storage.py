#!/usr/bin/python3

""" 
    This module contains a class that is used to manipulate Data and save/load 
    it using a JSON file
"""

import json as js
from os import path
import models
from models.base_model import *


class FileStorage:
    """
        class FileStorage serializes instances to a JSON file
        and deserializes JSON file to instances:
    """
    """ 
        Private class attributes:
        __file_path: used to store the name of the JSON file
        __onjects: a dictionary used to store created objects
    """
    __file_path = 'file.json'
    __objects = {}


    def __init__(self):
        """ Consturtor """

    def all(self):
        """ 
            returns the dictionary '__objects' containing all created objects
        """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the given 'obj' with key <obj class name>.id """
        Id = str(obj.id)
        # The object key consists of its class name and id value
        key = f"{obj.__class__.__name__}.{Id}"
        # set the key (<obj class name>.id) as the key of the newly created object
        self.__objects[key] =  obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        json_obj = {}

        """ 
            after we created the emply dictionary 'json_obj' we will now
            proceed to updating it with all key/value from __objects, then
            we serializes our dictionary and save it to our JSON file
        """
        for key in self.__objects:
            # save the dictionary representation of the each object
            value = self.__objects[key].to_dict()
            json_obj[key] = value

        with open(self.__file_path, 'w') as fl:
            js.dump(json_obj, fl)

    def reload(self):
        """
            deserializes contents the JSON file and loads it to __objects
            (only if the JSON file (__file_path) exists), if not; return
        """
        # check if file exists
        if (not path.isfile(self.__file_path)):
            return

        with open(self.__file_path, 'r', encoding="utf-8") as fl:
            # load and deserializes file contents
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
                # save object in '__objects'
                self.__objects[key] = atrbt_val