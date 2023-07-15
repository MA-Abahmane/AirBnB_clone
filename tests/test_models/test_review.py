#!/usr/bin/python3
""" Review test file """

import unittest
import models
from models.review import *


class TestReview(unittest.TestCase):
    """ Review testing class """

    def test_Review(self):
        """ testing the class BaseModel """

        # test if instance belongs to its class
        _object = Review()

        self.assertIsInstance(_object, Review)

        # test if 2 instance ids are unidentical
        _object = Review()
        _object2 = Review()

        self.assertNotEqual(_object, _object2)
        self.assertNotEqual(_object.id, _object2.id)

        # test if instance string is correctly formated
        _object = Review()
        _object_str = str(_object)
        Sformat = f"[Review] ({_object.id}) {_object.__dict__}"

        self.assertEqual(Sformat, _object_str)

        # check if to_dict return a dictionary representation of instance
        # containing class name
        _object = Review()
        obj_dict = _object.to_dict()
        classN = obj_dict['__class__']

        self.assertEqual(classN, 'Review')

        # check if update time gets updated when saved
        _object = Review()
        time1 = _object.updated_at
        _object.save()
        time2 = _object.updated_at

        self.assertNotEqual(time1, time2)

        # check is email and password first_name last_name are strings
        _object = Review()

        self.assertEqual(type(_object.place_id), str)
        self.assertEqual(type(_object.user_id), str)
        self.assertEqual(type(_object.text), str)

        self.assertIsNotNone(_object.place_id)
        self.assertIsNotNone(_object.user_id)
        self.assertIsNotNone(_object.text)


if __name__ == '__main__':
    unittest.main()
