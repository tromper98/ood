import pytest

from lib import *


def test_create_shape():
    shape = Shape(Color.Yellow)
    assert shape.color == Color.Yellow


def test_create_rectangle():
    rect = Rectangle(Point(-10, 10), Point(10, -10), Color.Red)
    assert rect.left_top == Point(-10, 10)
    assert rect.right_bottom == Point(10, -10)
    assert rect.color == Color.Red


def test_create_triangle():
    triangle = Triangle(Point(-5, 0), Point(5, 0), Point(2.5, 5), Color.Blue)
    assert triangle.vertex1 == Point(-5, 0)
    assert triangle.vertex2 == Point(5, 0)
    assert triangle.vertex3 == Point(2.5, 5)
    assert triangle.color == Color.Blue


def test_create_ellipse():
    ellipse = Ellipse(Point(25, 25), 5, 10, Color.Red)
    assert ellipse.center == Point(25, 25)
    assert ellipse.horizontal_radius == 5
    assert ellipse.vertical_radius == 10
    assert ellipse.color == Color.Red

