#!/usr/bin/python3
"""Unittests for the class Rectangle"""
import unittest
import sys
import os
from io import StringIO
from models.square import Square


class TestSquare(unittest.TestCase):
    """Define unittests for TestSquare"""

    def test_size(self):
        """Test size attribute"""
        a = Square(1)
        self.assertEqual(a.width, 1)
        b = Square(2, 3, 4)
        self.assertEqual(b.width, 2)
        c = Square(5, 6, 7)
        self.assertEqual(c.width, 5)

    def test_xy(self):
        """Test x,y and id attributes"""
        a = Square(1)
        self.assertEqual(a.x, 0)
        b = Square(2, 3, 4)
        self.assertEqual(b.x, 3)
        c = Square(5, 6, 7)
        self.assertEqual(c.y, 7)
        d = Square(5, 6, 7, 10)
        self.assertEqual(d.id, 10)

    def test_instantiation_errors(self):
        """Test instantiation errors"""
        with self.assertRaises(TypeError):
            Square("1")
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(-100)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(-24, -4)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)
        with self.assertRaises(ValueError):
            Square(0)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_print(self):
        """Test the default print of the class"""
        a = Square(1, 1, 1, 1)
        self.assertEqual(str(a), "[Square] (1) 1/1 - 1")
        b = Square(1, 2, 3, 4)
        self.assertEqual(str(b), "[Square] (4) 2/3 - 1")

    def test_area(self):
        """Test the area funtion"""
        a = Square(2)
        self.assertEqual(a.area(), 4)
        b = Square(3)
        self.assertEqual(b.area(), 9)
        c = Square(5)
        self.assertEqual(c.area(), 25)

    def test_to_dictionary(self):
        """Test the to dictionary function"""
        a = Square(1, 2, 3, 4,)
        a_desired = {'id': 4, 'size': 1, 'x': 2, 'y': 3}
        dic = a.to_dictionary()
        self.assertEqual(dic, a_desired)

    def test_update(self):
        """Test the update function"""

        """Tests with args[]"""
        a = Square(10, 10, 10, 1)
        a.update()
        self.assertEqual(str(a), "[Square] (1) 10/10 - 10")
        a.update(89)
        self.assertEqual(str(a), "[Square] (89) 10/10 - 10")
        b = Square(10, 10, 10, 1)
        b.update(89, 1)
        self.assertEqual(str(b), "[Square] (89) 10/10 - 1")
        c = Square(10, 10, 10, 1)
        c.update(89, 1, 2)
        self.assertEqual(str(c), "[Square] (89) 2/10 - 1")
        d = Square(10, 10, 10, 1)
        d.update(89, 1, 2, 3)
        self.assertEqual(str(d), "[Square] (89) 2/3 - 1")
        """Tests with **kargs{}"""
        ka = Square(10, 10, 10, 25)
        ka.update(**{'id': 89})
        self.assertEqual(str(ka), "[Square] (89) 10/10 - 10")
        kb = Square(10, 10, 10, 25)
        kb.update(**{'id': 89, 'size': 1})
        self.assertEqual(str(kb), "[Square] (89) 10/10 - 1")
        kc = Square(10, 10, 10, 25)
        kc.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(str(kc), "[Square] (89) 2/10 - 1")
        kd = Square(10, 10, 10, 25)
        kd.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(str(kd), "[Square] (89) 2/3 - 1")

    def test_create(self):
        """Test the create static method"""
        a = Square(1, 1)
        b = a.create(**{'id': 89, 'size': 10, 'x': 3, 'y': 4})
        self.assertNotEqual(a, b)

    def test_save_to_file(self):
        """Test the save to file method"""
        a = Square(1, 1, 1, 1)
        b = Square(2, 2, 2, 2)
        l1 = "[{\"id\": 1, \"size\": 1, \"x\": 1, \"y\": 1}"
        l2 = ", {\"id\": 2, \"size\": 2, \"x\": 2, \"y\": 2}]"

        a.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Square.json")

        a.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Square.json")

        a.save_to_file([a, b])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), l1 + l2)
        os.remove("Square.json")

    def test_load_from_file(self):
        """Test the load from file method"""
        a = Square(1, 1, 1, 1)
        b = Square(2, 2, 2, 2)

        """Loading a path that does not exist"""
        self.assertEqual(a.load_from_file(), [])

        """Addidg a and b to a new file"""
        a.save_to_file([a, b])

        """Loading a path that exist
        compares it's loaded values"""
        list_read = a.load_from_file()
        self.assertEqual(list_read[0].id, 1)
        self.assertEqual(list_read[1].x, 2)
        os.remove("Square.json")


if __name__ == "__main__":
    unittest.main()
