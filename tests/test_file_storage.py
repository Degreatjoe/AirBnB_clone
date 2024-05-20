#!/usr/bin/python3
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """
    Test cases for FileStorage class
    """

    def setUp(self):
        """
        Set up the test environment
        """
        self.storage = FileStorage()

    def tearDown(self):
        """
        Clean up the test environment
        """
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_save_and_reload(self):
        """
        Test saving and reloading objects
        """
        # Create a BaseModel instance
        obj = BaseModel()
        obj.save()

        # Reload storage to ensure the object is saved to the file
        self.storage.reload()

        # Check if the object exists in storage
        self.assertIn('BaseModel.{}'.format(obj.id), self.storage.all())

        # Create a new storage instance to reload from file
        new_storage = FileStorage()
        new_storage.reload()

        # Check if the reloaded object matches the original
        self.assertIn('BaseModel.{}'.format(obj.id), new_storage.all())


if __name__ == '__main__':
    unittest.main()
