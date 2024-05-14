#!/usr/bin/python3

import unittest
from AirBnB_clone.models import storage
from models.engine.file_storage import FileStorage

class TestInitPy(unittest.TestCase):
    def test_import_storage(self):
        from AirBnB_clone.models import storage
        self.assertIsInstance(storage, FileStorage)

if __name__ == '__main__':
    unittest.main()

