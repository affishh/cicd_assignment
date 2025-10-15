import unittest
from rectangle import Rectangle

def test_area():
    rect = Rectangle(5, 8)
    assert rect.area() == 40

def test_perimeter():
    rect = Rectangle(5, 8)
    assert rect.perimeter() == 26