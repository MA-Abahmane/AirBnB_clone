#!/usr/bin/python3
""" City test file """

import unittest
import models
from models.city import *


class TestCity(unittest.TestCase):
    """ City testing class """

    def test_City(self):
        """ testing the class BaseModel """
        
        # test if instance belongs to its class
        _object = City()

        self.assertIsInstance(_object, City)

        # test if 2 instance ids are unidentical
        _object = City()
        _object2 = City()

        self.assertNotEqual(_object, _object2)
        self.assertNotEqual(_object.id, _object2.id)

        # test if instance string is correctly formated
        _object = City()
        _object_str = str(_object)
        Sformat = f"[City] ({_object.id}) {_object.__dict__}"

        self.assertEqual(Sformat, _object_str)

        # check if to_dict return a dictionary representation of instance
        # containing class name
        _object = City()
        obj_dict = _object.to_dict()
        classN = obj_dict['__class__']

        self.assertEqual(classN, 'City')

        # check if update time gets updated when saved
        _object = City()
        time1 = _object.updated_at
        _object.save()
        time2 = _object.updated_at

        self.assertNotEqual(time1, time2)

        # check is email and password first_name last_name are strings
        _object = City()
        
        self.assertEqual(type(_object.state_id), str)
        self.assertEqual(type(_object.name), str)

        self.assertIsNotNone(_object.state_id)
        self.assertIsNotNone(_object.name)


if __name__ == '__main__':
    unittest.main()
