#!/usr/bin/python3
'''amenity test class'''
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()

    def test_name(self):
        self.assertEqual(self.amenity.name, "")


if __name__ == '__main__':
    unittest.main()