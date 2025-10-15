import unittest
from rectangle import Rectangle, Triangle

def test_area():
    rect = Rectangle(5, 8)
    assert rect.area() == 40

def test_perimeter():
    rect = Rectangle(5, 8)
    assert rect.perimeter() == 26

def test_triangle_area():
    tri = Triangle(5, 8)
    assert tri.area() == 20