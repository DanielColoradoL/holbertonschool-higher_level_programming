#!/usr/bin/python3
"""Unittests for the class Rectangle"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Define unittests for TestRectangle"""

    def test_widht(self):
        """Test width attribute"""
        a = Rectangle(1, 2)
        self.assertEqual(a.width, 1)
        b = Rectangle(15, 2, 3)
        self.assertEqual(b.width, 15)
        c = Rectangle(3, 2, 3, 4)
        self.assertEqual(c.width, 3)
        d = Rectangle(4, 2, 3, 4, 5)
        self.assertEqual(d.width, 4)

    def test_height(self):
        """Test height attribute"""
        a = Rectangle(1, 2)
        self.assertEqual(a.height, 2)
        b = Rectangle(15, 2, 3)
        self.assertEqual(b.height, 2)
        c = Rectangle(3, 6, 3, 4)
        self.assertEqual(c.height, 6)
        d = Rectangle(4, 44, 3, 4, 5)
        self.assertEqual(d.height, 44)

    def test_instantiation_errors(self):
        """Test instantiation errors"""
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

    def test_print(self):
        """Test the default print of the class"""
        a = Rectangle(1, 1, 1, 1, 1)
        self.assertEqual(str(a), "[Rectangle] (1) 1/1 - 1/1")
        b = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(b), "[Rectangle] (5) 3/4 - 1/2")

    def test_area(self):
        """Test the area funtion"""
        a = Rectangle(2, 3)
        self.assertEqual(a.area(), 6)
        b = Rectangle(3, 3)
        self.assertEqual(b.area(), 9)
        c = Rectangle(5, 5)
        self.assertEqual(c.area(), 25)
