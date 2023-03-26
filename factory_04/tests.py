import pytest
from typing import List

from lib import *


class MockLine:
    _start: Point
    _end: Point

    def __init__(self, start: Point, end: Point):
        self._start = start
        self._end = end

    def __eq__(self, other):
        if self._start == other._start and self._end == other._end:
            return True
        return False


class MockCanvas(CanvasInterface):
    lines: List[MockLine]
    color: Color
    x: float
    y: float
    h_radius: float
    v_radius: float

    def __init__(self):
        self.lines = []

    def draw_line(self, start: Point, end: Point):
        self.lines.append(MockLine(start, end))

    def set_color(self, color: Color):
        self.color = color

    def draw_ellipse(self, x, y, h_radius, v_radius):
        self.x = x
        self.y = y
        self.h_radius = h_radius
        self.v_radius = v_radius

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


def test_create_regular_polygon():
    polygon = RegularPolygon(Point(15, 15), 100, 6, Color.Black)
    assert polygon.center == Point(15, 15)
    assert polygon.radius == 100
    assert polygon.vertex_count == 6
    assert polygon.color == Color.Black


def test_draw_rectangle():
    rectangle = Rectangle(Point(-25, 30), Point(60, -50), Color.Blue)
    m_canvas = MockCanvas()

    rectangle.draw(m_canvas)
    expected_lines: List[MockLine] = [
        MockLine(Point(-25, 30), Point(60, 30)),
        MockLine(Point(60, 30), Point(60, -50)),
        MockLine(Point(60, -50), Point(-25, -50)),
        MockLine(Point(-25, -50), Point(-25, 30))
    ]
    expected_color = Color.Blue

    assert m_canvas.lines == expected_lines
    assert m_canvas.color == expected_color


def test_draw_triangle():
    triangle = Triangle(Point(0, 0), Point(10, 10), Point(25, 25), Color.Yellow)
    m_canvas = MockCanvas()

    triangle.draw(m_canvas)
    expected_lines: List[MockLine] = [
        MockLine(Point(0, 0), Point(10, 10)),
        MockLine(Point(10, 10), Point(25, 25)),
        MockLine(Point(25, 25), Point(0, 0))
    ]
    expected_color = Color.Yellow
    assert m_canvas.lines == expected_lines
    assert m_canvas.color == expected_color


def test_draw_ellipse():
    ellipse = Ellipse(Point(0, 0), 10, 15, Color.Pink)
    m_canvas = MockCanvas()

    ellipse.draw(m_canvas)
    assert ellipse.center.x == m_canvas.x
    assert ellipse.center.y == m_canvas.y
    assert ellipse.vertical_radius == m_canvas.v_radius
    assert ellipse.horizontal_radius == m_canvas.h_radius
    assert ellipse.color == m_canvas.color


def test_draw_regular_polygon():
    polygon = RegularPolygon(Point(15, 15), 25, 8, Color.Red)
    m_canvas = MockCanvas()

    p1 = Point(9.244477206645351, 39.328459823325744)
    p2 = Point(-6.272588113352985, 28.133049720443204)
    p3 = Point(-9.328459823325737, 9.24447720664531)
    p4 = Point(1.866950279556832, -6.272588113353006)
    p5 = Point(20.755522793354732, -9.32845982332573)
    p6 = Point(36.27258811335294, 1.8669502795567148)
    p7 = Point(39.328459823325716, 20.755522793354775)
    p8 = Point(28.133049720443246, 36.27258811335296)

    polygon.draw(m_canvas)
    expected_lines: List[MockLine] = [
        MockLine(p1, p2),
        MockLine(p2, p3),
        MockLine(p3, p4),
        MockLine(p4, p5),
        MockLine(p5, p6),
        MockLine(p6, p7),
        MockLine(p7, p8),
        MockLine(p8, p1)
    ]
    expected_color = Color.Red

    assert m_canvas.lines == expected_lines
    assert m_canvas.color == expected_color