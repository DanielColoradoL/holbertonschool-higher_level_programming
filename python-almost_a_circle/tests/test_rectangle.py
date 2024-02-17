#!/usr/bin/python3
"""Unittests for the class Rectangle"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Define unittests for TestRectangle"""

    def test_instantiation(self):
        """Test instantiation id"""

        a = Rectangle(1, 2)
        self.assertEqual(str(a), "[Rectangle] (1) 0/0 - 1/2")

        b = Rectangle(1, 2, 3)
        self.assertEqual(str(b), "[Rectangle] (2) 3/0 - 1/2")

        c = Rectangle(1, 2, 3, 4)
        self.assertEqual(str(c), "[Rectangle] (3) 3/4 - 1/2")

        h = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(h), "[Rectangle] (5) 3/4 - 1/2")

        with self.assertRaises(TypeError):
            Rectangle("1", 2)

        with self.assertRaises(TypeError):
            Rectangle(1, "2")

        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

        with self.assertRaises(ValueError):
            Rectangle(1, -2)

        with self.assertRaises(ValueError):
            Rectangle(0, 2)

        with self.assertRaises(ValueError):
            Rectangle(1, 0)

        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)
