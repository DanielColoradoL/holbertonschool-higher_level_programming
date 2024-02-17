#!/usr/bin/python3
""" 19-main """
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base




a = Rectangle(2, 3)
print(a.area())
# 6


b = Rectangle(1, 1, 1, 1, 1)
print(b)
# [Rectangle] (1) 1/1 - 1/1


c = Rectangle(2, 3)
""" c.display() """
"""
##
##
##
"""

d = Rectangle(2, 2, 3)
d.display()
"""
  ##
  ##
"""

e = Rectangle(2, 2, 2, 2)
e.display()
"""

  ##
  ##
"""

f = Rectangle(1, 2, 3, 4, 10)
dic = f.to_dictionary()
print(dic)
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