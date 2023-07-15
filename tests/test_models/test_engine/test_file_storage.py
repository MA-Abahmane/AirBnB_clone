""" file_storage test file """

import unittest
import os
from os import path as p
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
        if (not p.isfile(Fname)):
            raise FileNotFoundError

        # test for reload and save
        dataBase = FileStorage()
        _object = User()
        _object.email = "MAA@gmail.com"
        _object.save()
        dataBase.reload()

        """ tests reload """
        user = User()
        user.first_name = "Alx"
        user.last_name = "amu"
        user.email = "MAA@gmail.com"
        storage = FileStorage()

        storage.save()
        Root = os.path.dirname(os.path.abspath("console.py"))
        path = os.path.join(Root, "file.json")
        with open(path, 'r') as f:
            lines = f.readlines()
        try:
            os.remove(path)
        except FileNotFoundError:
            pass
        storage.save()
        with open(path, 'r') as f:
            lines2 = f.readlines()
        self.assertEqual(lines, lines2)
        try:
            os.remove(path)
        except FileNotFoundError:
            pass
        with open(path, "w") as f:
            f.write("{}")
        with open(path, "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(storage.reload(), None)





if __name__ == '__main__':
    unittest.main()