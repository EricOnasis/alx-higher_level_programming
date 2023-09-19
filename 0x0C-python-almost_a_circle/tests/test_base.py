#!/usr/bin/python3
"""Tests for TestBaseClass class"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBaseClass(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_create_new_instance_with_id(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.id, 1)

        r2 = Rectangle(2, 4)
        self.assertEqual(r2.id, 2)

    def test_create_new_instance_with_custom_id(self):
        s = Square(5, id=10)
        self.assertEqual(s.id, 10)

    def test_create_new_instance_with_default_id(self):
        s = Square(3)
        self.assertEqual(s.id, 1)

    def test_to_json_string_with_empty_list(self):
        self.assertEqual(Base.to_json_string([]), '[]')

    def test_to_json_string_with_none(self):
        self.assertEqual(Base.to_json_string(None), '[]')

    def test_from_json_string_with_empty_list(self):
        self.assertEqual(Base.from_json_string('[]'), [])

    def test_from_json_string_with_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def tearDown(self):
        try:
            os.remove("Rectangle.json")
            os.remove("Rectangle.csv")
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    unittest.main()
