#!/usr/bin/python3
""" Place test file """

import unittest
import models
from models.place import *


class TestPlace(unittest.TestCase):
    """ Place testing class """

    def test_Place(self):
        """ testing the class BaseModel """
        
        # test if instance belongs to its class
        _object = Place()

        self.assertIsInstance(_object, Place)

        # test if 2 instance ids are unidentical
        _object = Place()
        _object2 = Place()

        self.assertNotEqual(_object, _object2)
        self.assertNotEqual(_object.id, _object2.id)

        # test if instance string is correctly formated
        _object = Place()
        _object_str = str(_object)
        Sformat = f"[Place] ({_object.id}) {_object.__dict__}"

        self.assertEqual(Sformat, _object_str)

        # check if to_dict return a dictionary representation of instance
        # containing class name
        _object = Place()
        obj_dict = _object.to_dict()
        classN = obj_dict['__class__']

        self.assertEqual(classN, 'Place')

        # check if update time gets updated when saved
        _object = Place()
        time1 = _object.updated_at
        _object.save()
        time2 = _object.updated_at

        self.assertNotEqual(time1, time2)

        # check is email and password first_name last_name are strings
        _object = Place()
        
        self.assertEqual(type(_object.city_id), str)
        self.assertEqual(type(_object.user_id), str)
        self.assertEqual(type(_object.name), str)
        self.assertEqual(type(_object.description), str)
        self.assertEqual(type(_object.number_rooms), int)
        self.assertEqual(type(_object.number_bathrooms), int)
        self.assertEqual(type(_object.max_guest), int)
        self.assertEqual(type(_object.price_by_night), int)
        self.assertEqual(type(_object.latitude), float)
        self.assertEqual(type(_object.longitude), float)
        self.assertEqual(type(_object.amenity_ids), list)

        self.assertIsNotNone(_object.city_id)
        self.assertIsNotNone(_object.user_id)
        self.assertIsNotNone(_object.name)
        self.assertIsNotNone(_object.description)
        self.assertIsNotNone(_object.number_rooms)
        self.assertIsNotNone(_object.number_bathrooms)
        self.assertIsNotNone(_object.max_guest)
        self.assertIsNotNone(_object.price_by_night)
        self.assertIsNotNone(_object.latitude)
        self.assertIsNotNone(_object.longitude)
        self.assertIsNotNone(_object.amenity_ids)


if __name__ == '__main__':
    unittest.main()
