#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        # Reset storage to ensure clean state for each test
        storage.reload()

    def test_attributes(self):
        # Create an instance of BaseModel
        obj = BaseModel()

        # Check if attributes are set correctly
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_str_method(self):
        # Create an instance of BaseModel
        obj = BaseModel()

        # Check if __str__ method returns the expected string format
        expected_str = "[BaseModel] ({}) {}".format(obj.id, obj.__dict__)
        self.assertEqual(str(obj), expected_str)

    def test_save_method(self):
        # Create an instance of BaseModel
        obj = BaseModel()

        # Get the initial updated_at value
        initial_updated_at = obj.updated_at

        # Call save method and check if updated_at is updated
        obj.save()
        self.assertNotEqual(obj.updated_at, initial_updated_at)

    def test_to_dict_method(self):
        # Create an instance of BaseModel
        obj = BaseModel()

        # Get the dictionary representation using to_dict method
        obj_dict = obj.to_dict()

        # Check if the returned dictionary has the expected keys
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        self.assertCountEqual(obj_dict.keys(), expected_keys)

        # Check if the values of created_at and updated_at are in ISO format
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())

        # Check if __class__ key has the correct value
        self.assertEqual(obj_dict['__class__'], 'BaseModel')

def test_save_and_reload(self):
    # Create an instance of BaseModel
    obj = BaseModel()

    # Save the object
    obj.save()

    # Create a new BaseModel instance
    new_obj = BaseModel(id=obj.id)

    # Reload storage
    storage.reload()

    # Check if object is present in storage
    self.assertIn("BaseModel.{}".format(obj.id), storage.all())

    # Check if the reloaded object has the same attributes as the original object
    self.assertEqual(new_obj.id, obj.id)
    self.assertEqual(new_obj.created_at, obj.created_at)
    self.assertEqual(new_obj.updated_at, obj.updated_at)

if __name__ == '__main__':
    unittest.main()
