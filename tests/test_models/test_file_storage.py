#!/usr/bin/python3
import unittest
import os
from models.base_model import BaseModel
from models import storage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        # Remove the file.json if it exists before each test
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_save_and_reload(self):
        # Create an instance of BaseModel
        obj = BaseModel()

        # Save the object
        storage.save()

        # Reload storage
        storage.reload()

        # Check if object is present in storage
        self.assertIn("BaseModel.{}".format(obj.id), storage.all())

if __name__ == '__main__':
    unittest.main()

