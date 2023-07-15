#!/usr/bin/python3
""" file_storage test file """

import pep8
import unittest
from os import path
import models.engine
from models.engine.file_storage import *


class FileStorageTest(unittest.TestCase):
    """ FileStorage testing class """

    def test_file_storage(self):
        """ testing the class BaseModel """

        # test if instance belongs to its class
        _object = FileStorage()

        self.assertIsInstance(_object, FileStorage)

        # test if object dictionary exists and is not none
        dataBase = FileStorage()
        objsD = _object.all()

        self.assertEqual(type(objsD), dict)
        self.assertIsNotNone(objsD)

        # test if function save saves objects in dictionary correctly
        dataBase = FileStorage()
        obj_dict = dataBase.all()
        _object = BaseModel()
        obj_key = f"{BaseModel.__name__}.{_object.id}"

        self.assertIsNotNone(obj_dict[obj_key])

        # check if update time gets updated when saved
        _object = BaseModel()
        time1 = _object.updated_at
        _object.save()
        time2 = _object.updated_at

        self.assertNotEqual(time1, time2)

        # check is file storage exists
        Fname = "file.json"
        if (not path.isfile(Fname)):
            raise FileNotFoundError

        # check if file is in pep style
        pep_style = pep8.StyleGuide(quiet=True)
        p = pep_style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")


if __name__ == '__main__':
    unittest.main()