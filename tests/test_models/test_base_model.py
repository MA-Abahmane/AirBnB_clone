#!/usr/bin/python3
""" base_model test file """

import unittest
import models
from models.base_model import *


class BaseModelTest(unittest.TestCase):
    """ BaseModel testing class """

    def test_BaseModel(self):
        """ testing the class BaseModel """
        
        # test if instance belongs to its class
        _object = BaseModel()

        self.assertIsInstance(_object, BaseModel)

        # test if 2 instance ids are unidentical
        _object = BaseModel()
        _object2 = BaseModel()

        self.assertNotEqual(_object, _object2)

        # test if instance string is correctly formated
        _object = BaseModel()
        _object_str = str(_object)
        Sformat = f"[BaseModel] ({_object.id}) {_object.__dict__}"

        self.assertEqual(Sformat, _object_str)

        # check if to_dict return a dictionary representation of instance
        # containing class name
        _object = BaseModel()
        obj_dict = _object.to_dict()
        classN = obj_dict['__class__']

        self.assertEqual(classN, 'BaseModel')

        # check if update time gets updated when saved
        _object = BaseModel()
        time1 = _object.updated_at
        _object.save()
        time2 = _object.updated_at

        self.assertNotEqual(time1, time2)





if __name__ == '__main__':
    unittest.main()
