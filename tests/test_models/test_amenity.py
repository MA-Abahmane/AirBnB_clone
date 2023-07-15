#!/usr/bin/python3
""" Amenity test file """

import unittest
import models
from models.amenity import *


class TestAmenity(unittest.TestCase):
    """ Amenity testing class """

    def test_Amenity(self):
        """ testing the class BaseModel """

        # test if instance belongs to its class
        _object = Amenity()

        self.assertIsInstance(_object, Amenity)

        # test if 2 instance ids are unidentical
        _object = Amenity()
        _object2 = Amenity()

        self.assertNotEqual(_object, _object2)
        self.assertNotEqual(_object.id, _object2.id)

        # test if instance string is correctly formated
        _object = Amenity()
        _object_str = str(_object)
        Sformat = f"[Amenity] ({_object.id}) {_object.__dict__}"

        self.assertEqual(Sformat, _object_str)

        # check if to_dict return a dictionary representation of instance
        # containing class name
        _object = Amenity()
        obj_dict = _object.to_dict()
        classN = obj_dict['__class__']

        self.assertEqual(classN, 'Amenity')

        # check if update time gets updated when saved
        _object = Amenity()
        time1 = _object.updated_at
        _object.save()
        time2 = _object.updated_at

        self.assertNotEqual(time1, time2)

        # check is email and password first_name last_name are strings
        _object = Amenity()

        self.assertEqual(type(_object.name), str)
        self.assertIsNotNone(_object.name)


if __name__ == '__main__':
    unittest.main()
