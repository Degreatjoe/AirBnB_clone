#!/usr/bin/python3
"""
Test cases for BaseModel class
"""
import unittest
from models.base_model import BaseModel
from models import storage

# from AirBnB_clone import models

class TestBaseModel(unittest.TestCase):
    """
    Test cases for BaseModel class
    """

    def test_attributes(self):
        """
        Test instantiation of BaseModel with attributes
        """
        obj = BaseModel()
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))

    def test_id_generation(self):
        """
        Test if unique id is generated for each BaseModel instance
        """
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_str_method(self):
        """
        Test __str__ method of BaseModel
        """
        obj = BaseModel()
        obj_str = str(obj)
        self.assertEqual(obj_str, "[BaseModel] ({}) {}".format(obj.id, obj.__dict__))

    def test_save_method(self):
        """
        Test save method of BaseModel
        """
        obj = BaseModel()
        initial_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(initial_updated_at, obj.updated_at)

    def test_to_dict_method(self):
        """
        Test to_dict method of BaseModel
        """
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertTrue(isinstance(obj_dict, dict))
        self.assertTrue('__class__' in obj_dict)
        self.assertTrue('id' in obj_dict)
        self.assertTrue('created_at' in obj_dict)
        self.assertTrue('updated_at' in obj_dict)
    def test_from_dict_method(self):
        """
        Test recreating BaseModel instance from dictionary representation
        """
        obj = BaseModel()
        obj_dict = obj.to_dict()
        new_obj = BaseModel(**obj_dict)
        self.assertEqual(obj.__dict__, new_obj.__dict__)


if __name__ == '__main__':
    unittest.main()
