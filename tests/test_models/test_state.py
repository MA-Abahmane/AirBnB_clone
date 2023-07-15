#!/usr/bin/python3
""" state test file """

import unittest
import models
from models.state import *


class StateTest(unittest.TestCase):
    """ State testing class """

    def test_User(self):
        """ testing the class BaseModel """

        # test if instance belongs to its class
        _object = State()

        self.assertIsInstance(_object, State)

        # test if 2 instance ids are unidentical
        _object = State()
        _object2 = State()

        self.assertNotEqual(_object, _object2)
        self.assertNotEqual(_object.id, _object2.id)

        # test if instance string is correctly formated
        _object = State()
        _object_str = str(_object)
        Sformat = f"[State] ({_object.id}) {_object.__dict__}"

        self.assertEqual(Sformat, _object_str)

        # check if to_dict return a dictionary representation of instance
        # containing class name
        _object = State()
        obj_dict = _object.to_dict()
        classN = obj_dict['__class__']

        self.assertEqual(classN, 'State')

        # check if update time gets updated when saved
        _object = State()
        time1 = _object.updated_at
        _object.save()
        time2 = _object.updated_at

        self.assertNotEqual(time1, time2)

        # check is email and password first_name last_name are strings
        _object = State()

        self.assertEqual(type(_object.name), str)
        self.assertIsNotNone(_object.name)


if __name__ == '__main__':
    unittest.main()
