#!/usr/bin/python3
"""Unittests for the class Base"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Define unittests for TestBase."""

    def test_id(self):
        """Test instantiation id"""
        b1 = Base()
        b2 = Base()
        b3 = Base(89)

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 89)

    def test_to_json_string_dic(self):
        """Test the json to string function
        with dictionaries"""

        b = Base.to_json_string([])
        self.assertEqual(b, "[]")

        c = Base.to_json_string([{'id': 12}])
        self.assertEqual(c, '[{"id": 12}]')

        d = type(Base.to_json_string([{'id': 12}]))
        self.assertEqual(d, str)

        e = Base.from_json_string(None)
        self.assertEqual(e, [])

        f = Base.from_json_string("[]")
        self.assertEqual(f, [])

        g = Base.from_json_string('[{ "id": 89 }]')
        self.assertEqual(g, [{'id': 89}])

        h = type(Base.from_json_string('[{ "id": 89 }]'))
        self.assertEqual(h, list)

    def test_to_json_string_none(self):
        """Test the json to string function
        with None"""
        a = Base.to_json_string(None)
        self.assertEqual(a, "[]")

        z = Base.to_json_string(None)
        self.assertEqual(z, "[]")


if __name__ == "__main__":
    unittest.main()
