import os
import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorageInstatiation(unittest.TestCase):
    """This test file storage instatiation."""
    def test_FileStorage_instatiation_no_args(self):
        # test when no argument is passed during instatiation
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instatiation_with_arg(self):
        # test instatiation with an arg which should raise error
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_storage_initialization(self):
        # test is variable storage is an instance of FileStorage
        self.assertEqual(type(models.storage), FileStorage)


class testFileStorage(unittest.TestCase):
    # test the FileStorage class
    def setUp(self):
        # temporary file to test saving data
        self.test_file = "test_file.json"

    def tearDown(self):
        # this removes the previously created file after use
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_all_storage_returns_dictionary(self):
        # this test whether the func all() returns a dict.
        self.assertEqual(dict, type(models.storage.all()))

    def test_new(self):
        # test the method new() to create and store the object
        my_obj = BaseModel()
        models.storage.new(my_obj)
        self.assertIn(f"BaseModel.{my_obj.id}", models.storage.all())

    def test_new_with_args(self):
        # test if new() is called with an additional argument
        # is should raise TypeError
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        # test using the method new() with None as the arg
        # this should raise AttributeError
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save_and_reload(self):
        # this test saving an object and reloading it
        my_obj1 = BaseModel()
        my_obj2 = BaseModel()
        models.storage.new(my_obj1)
        models.storage.new(my_obj2)
        models.storage.save()

        # create an instance of FileStorage to simulate reload
        my_storage = FileStorage()
        my_storage.reload()

        # check if the newly reloaded object matchs the orginal
        self.assertTrue(my_storage.all().get(f"BaseModel.{my_obj1.id}") is not
                        None)
        self.assertTrue(my_storage.all().get(f"BaseModel.{my_obj2.id}") is not
                        None)

    def test_save_to_file(self):
        # this test if an object is saved to a file and if the file is created
        my_obj = BaseModel()
        models.storage.new(my_obj)
        models.storage.save()
        self.assertTrue(os.path.exists(models.storage._FileStorage__file_path))

    def test_reload_empty_file(self):
        # this test when trying to reload an empty file or
        # file that doesnt exist
        with self.assertRaises(TypeError):
            models.storage()
            models.storage.reload()


if __name__ == "__main__":
    unittest.main()
