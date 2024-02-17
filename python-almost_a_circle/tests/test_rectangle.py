#!/usr/bin/python3
"""Unittests for the class Rectangle"""
import unittest
import sys
import os
from io import StringIO
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

    def test_display(self):
        """Test the display function"""

        """Display without x and y"""
        a = Rectangle(2, 3)
        a_desired = "##\n##\n##\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        a.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), a_desired)
        """Display without y"""
        b = Rectangle(2, 2, 3)
        b_desired = "   ##\n   ##\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        b.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), b_desired)
        """Display with x and y"""
        c = Rectangle(2, 2, 2, 2)
        c_desired = "\n\n  ##\n  ##\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        c.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), c_desired)

    def test_to_dictionary(self):
        """Test the to dictionary function"""
        a = Rectangle(1, 2, 3, 4, 10)
        a_desired = {'id': 10, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        dic = a.to_dictionary()
        self.assertEqual(dic, a_desired)

    def test_update(self):
        """Test the update function"""

        """Tests with args[]"""
        a = Rectangle(10, 10, 10, 10, 1)
        a.update()
        self.assertEqual(str(a), "[Rectangle] (1) 10/10 - 10/10")
        a.update(89)
        self.assertEqual(str(a), "[Rectangle] (89) 10/10 - 10/10")
        b = Rectangle(10, 10, 10, 10, 1)
        b.update(89, 1)
        self.assertEqual(str(b), "[Rectangle] (89) 10/10 - 1/10")
        c = Rectangle(10, 10, 10, 10, 1)
        c.update(89, 1, 2)
        self.assertEqual(str(c), "[Rectangle] (89) 10/10 - 1/2")
        d = Rectangle(10, 10, 10, 10, 1)
        d.update(89, 1, 2, 3)
        self.assertEqual(str(d), "[Rectangle] (89) 3/10 - 1/2")
        e = Rectangle(10, 10, 10, 10, 1)
        e.update(89, 1, 2, 3, 4)
        self.assertEqual(str(e), "[Rectangle] (89) 3/4 - 1/2")
        """Tests with **kargs{}"""
        ka = Rectangle(10, 10, 10, 10, 25)
        ka.update(**{'id': 89})
        self.assertEqual(str(ka), "[Rectangle] (89) 10/10 - 10/10")
        kb = Rectangle(10, 10, 10, 10, 25)
        kb.update(**{'id': 89, 'width': 1})
        self.assertEqual(str(kb), "[Rectangle] (89) 10/10 - 1/10")
        kc = Rectangle(10, 10, 10, 10, 25)
        kc.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(str(kc), "[Rectangle] (89) 10/10 - 1/2")
        kd = Rectangle(10, 10, 10, 10, 25)
        kd.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(str(kd), "[Rectangle] (89) 3/10 - 1/2")
        ke = Rectangle(10, 10, 10, 10, 25)
        ke.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(str(ke), "[Rectangle] (89) 3/4 - 1/2")

    def test_create(self):
        """Test the create static method"""
        a = Rectangle(1, 1)
        b = a.create(**{'id': 89, 'width': 10, 'height': 20, 'x': 3, 'y': 4})
        self.assertNotEqual(a, b)
