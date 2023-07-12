#!/usr/bin/python3


import uuid
from datetime import datetime
import models


class BaseModel:
    """ class BaseModel defines all common attributes/methods for other classes: """

    def __str__(self):
        """ Class print """
        classN = self.__class__.__name__
        return f"[{classN}] ({self.id}) {self.__dict__}"

    def __init__(self, *args, **kwargs):
        """ Constructor """

        if (kwargs):
            for key, val in kwargs.items():
                """
                    'created_at' and 'updated_at' values are converted from
                    string objects to datetime objects using 'strptime()':
                    datetime object format:
                    [datetime.datetime(YYYY, MM, DD, HH, MM, SS, mmmmmm)]
                """
                if (key == 'created_at'):
                    val = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')
                if (key == 'updated_at'):
                    val = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f') # type: ignore
                """
                    if key is not '__class__'; set 'key' as a public instance
                    attribute name and 'val' as its initial value
                """
                if (key != '__class__'):
                    setattr(self, key, val)

        else:
            # assign a unique ID to instance when created
            self.id = str(uuid.uuid4())
            # creation date of instance
            self.created_at = datetime.now()
            # updated time of instance
            self.updated_at = datetime.now()
            # if user dosent exist, set new user account
            models.storage.new(self)

    def save(self):
        """ 
            updates 'updated_at' with the current datetime
            after updating account to JSON file using 'storage.save()'
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary of all keys/values of set instance attributes """
        """
            '__dict__': return a dictionary of all instance attributes of an object
            'created_at' and 'updated_at' are converted to string object in ISO format
            [YYYY-MM-DD HH:MM:SS.mmmmmm] using 'isoformat()':
        """
        attributes_dict = self.__dict__.copy()
        attributes_dict['__class__'] = self.__class__.__name__
        attributes_dict['created_at'] = self.created_at.isoformat()
        attributes_dict['updated_at'] = self.updated_at.isoformat()

        return attributes_dict
