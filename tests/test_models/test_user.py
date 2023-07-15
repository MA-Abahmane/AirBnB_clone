#!/usr/bin/python3
""" user test file """

import unittest
import pep8
import models
from models.base_model import *
from models.user import *


class UserTest(unittest.TestCase):
    """ User testing class """

    def test_User(self):
        """ testing the class BaseModel """
        
        # test if instance belongs to its class
        _object = User()

        self.assertIsInstance(_object, User)

        # test if 2 instance ids are unidentical
        _object = User()
        _object2 = User()

        self.assertNotEqual(_object, _object2)
        self.assertNotEqual(_object.id, _object2.id)

        # test if instance string is correctly formated
        _object = User()
        _object_str = str(_object)
        Sformat = f"[User] ({_object.id}) {_object.__dict__}"

        self.assertEqual(Sformat, _object_str)

        # check if to_dict return a dictionary representation of instance
        # containing class name
        _object = User()
        obj_dict = _object.to_dict()
        classN = obj_dict['__class__']

        self.assertEqual(classN, 'User')

        # check if update time gets updated when saved
        _object = User()
        time1 = _object.updated_at
        _object.save()
        time2 = _object.updated_at

        self.assertNotEqual(time1, time2)

        # test for pip mode
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")


if __name__ == '__main__':
    unittest.main()
