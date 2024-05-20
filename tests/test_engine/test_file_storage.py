#!/usr/bin/python3
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.model = BaseModel()
        self.storage.new(self.model)

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        self.assertEqual(self.storage.all()[f"BaseModel.{self.model.id}"], self.model)

    def test_new(self):
        new_model = BaseModel()
        self.storage.new(new_model)
        self.assertIn(f"BaseModel.{new_model.id}", self.storage.all())

    def test_save(self):
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        self.storage.save()
        self.storage.reload()
        self.assertIn(f"BaseModel.{self.model.id}", self.storage.all())

if __name__ == '__main__':
    unittest.main()
