#!/usr/bin/python3
"""Unittests for the class Base"""
import unittest
from models.base import Base


class Base_Test(unittest.TestCase):
    """Define unittests for Base_Test([..])."""

    def test_base(self):
        """Test the class base
        basic features"""
        b1 = Base()
        b2 = Base()
        b3 = Base(89)

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 89)
