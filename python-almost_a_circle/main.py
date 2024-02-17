#!/usr/bin/python3
""" 19-main """
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base



a = print(Rectangle(1, 2))

b = Rectangle(1, 2, 3)
"[Rectangle] (2) 3/0 - 1/2"

c = Rectangle(1, 2, 3, 4)
"[Rectangle] (3) 3/4 - 1/2"



""" with self.assertRaises(TypeError):
    d = Rectangle("1", 2)

with self.assertRaises(TypeError):
    e = Rectangle(1, "2") """

""" with self.assertRaises(TypeError):
    f = Rectangle(1, 2, "3") """

""" with self.assertRaises(TypeError):
    g = Rectangle(1, 2, 3, "4") """

h = Rectangle(1, 2, 3, 4, 5)
"[Rectangle] (5) 3/4 - 1/2"

""" with self.assertRaises(ValueError):
    h = Rectangle(-1, 2) """

""" with self.assertRaises(ValueError):
    i = Rectangle(1, -2) """

""" with self.assertRaises(ValueError):
    j = Rectangle(0, 2) """

""" with self.assertRaises(ValueError):
    k = Rectangle(1, 0) """

""" with self.assertRaises(ValueError):
    l = Rectangle(1, 2, -3) """

""" with self.assertRaises(ValueError):
    m = Rectangle(1, 2, 3, -4) """




# Test of area() exists

# Test of __str__() for Rectangle exists

# Test of display() without x and y exists

# Test of display() without y exists

# Test of display() exists

# Test of to_dictionary() in Rectangle exists

# Test of update() in Rectangle exists

# Test of update(89) in Rectangle exists

# Test of update(89, 1) in Rectangle exists

# Test of update(89, 1, 2) in Rectangle exists

# Test of update(89, 1, 2, 3) in Rectangle exists

# Test of update(89, 1, 2, 3, 4) in Rectangle exists

# Test of update(**{ 'id': 89 }) in Rectangle exists

# Test of update(**{ 'id': 89, 'width': 1 }) in Rectangle exists

# Test of update(**{ 'id': 89, 'width': 1, 'height': 2 }) in Rectangle exists

# Test of update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 }) in Rectangle exists

# Test of update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 }) in Rectangle exists

# Test of Rectangle.create(**{ 'id': 89 }) in Rectangle exists

# Test of Rectangle.create(**{ 'id': 89, 'width': 1 }) in Rectangle exists

# Test of Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2 }) in Rectangle exists

# Test of Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 }) in Rectangle exists

# Test of Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 }) in Rectangle exists

# Test of Rectangle.save_to_file(None) in Rectangle exists

# Test of Rectangle.save_to_file([]) in Rectangle exists

# Test of Rectangle.save_to_file([Rectangle(1, 2)]) in Rectangle exists

# Test of Rectangle.load_from_file() when file doesn’t exist exists

# Test of Rectangle.load_from_file() when file exists exists