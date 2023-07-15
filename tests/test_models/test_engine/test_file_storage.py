""" file_storage test file """

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
        self.assertEqual(time1, time1)

        # check is file storage exists
        Fname = "file.json"
        if (not path.isfile(Fname)):
            raise FileNotFoundError



        # test for reload and save
        dataBase = FileStorage()
        _object = User()
        _object.email = "MAA@gmail.com"
        _object.save()
        dataBase.reload()





if __name__ == '__main__':
    unittest.main()