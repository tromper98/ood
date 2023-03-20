from math import sqrt, cos, sin, pi
from typing import List, Optional

from color import Color
from canvas import CanvasInterface
from point import Point


class Shape:
    _color: Color

    def __init__(self, color: Color):
        self._color = color

    def draw(self, canvas: CanvasInterface):
        ...

    @property
    def color(self) -> Color:
        return self._color


class Rectangle(Shape):
    _left_top: Point
    _right_bottom: Point

    def __init__(self, left_top: Point, right_bottom: Point, color: Color):
        super().__init__(color)
        if left_top == right_bottom:
            raise ValueError('Left top point and right bottom point must be different')

        self._left_top = left_top
        self._right_bottom = right_bottom

    def draw(self, canvas: CanvasInterface):
        right_top = Point(self.right_bottom.x, self.left_top.y)
        left_bottom = Point(self.left_top.x, self.right_bottom.y)

        canvas.draw_line(self.left_top, right_top)
        canvas.draw_line(right_top, self.right_bottom)
        canvas.draw_line(self.right_bottom, left_bottom)
        canvas.draw_line(left_bottom, self.left_top)
        canvas.set_color(self.color)

    @property
    def left_top(self) -> Point:
        return self._left_top

    @property
    def right_bottom(self) -> Point:
        return self._right_bottom


class Triangle(Shape):
    _vertex1: Point
    _vertex2: Point
    _vertex3: Point

    def __init__(self, vertex1: Point, vertex2: Point, vertex3: Point, color: Color):
        super().__init__(color)
        if not self._is_exist_triangle(vertex1, vertex2, vertex3):
            raise ValueError(f'Cannot create Triangle with point {vertex1}, {vertex2}, {vertex3}')

        self._vertex1 = vertex1
        self._vertex2 = vertex2
        self._vertex3 = vertex3

    def draw(self, canvas: CanvasInterface):
        canvas.set_color(self.color)
        canvas.draw_line(self.vertex1, self.vertex2)
        canvas.draw_line(self.vertex2, self.vertex3)
        canvas.draw_line(self.vertex3, self.vertex1)

    @property
    def vertex1(self) -> Point:
        return self._vertex1

    @property
    def vertex2(self) -> Point:
        return self._vertex2

    @property
    def vertex3(self) -> Point:
        return self._vertex3

    def _is_exist_triangle(self, vertex1: Point, vertex2: Point, vertex3: Point) -> bool:
        a: float = self._get_dist(vertex1, vertex2)
        b: float = self._get_dist(vertex2, vertex3)
        c: float = self._get_dist(vertex3, vertex1)

        if a + b < c or b + c < a or a + c < b:
            return False
        return True

    @staticmethod
    def _get_dist(start: Point, end: Point) -> float:
        dist: float = sqrt((end.x - start.x) ** 2 + (end.y - start.y) ** 2)
        return dist


class Ellipse(Shape):
    _center: Point
    _horizontal_radius: float
    _vertical_radius: float

    def __init__(self, center: Point, h_radius: float, v_radius: float, color: Color):
        if h_radius <= 0 or v_radius <= 0:
            raise ValueError('Cannot create Ellipse with non positive radius')

        super().__init__(color)
        self._center = center
        self._horizontal_radius = h_radius
        self._vertical_radius = v_radius

    def draw(self, canvas: CanvasInterface):
        canvas.set_color(self.color)
        canvas.draw_ellipse(self.center.x, self.center.y, self.horizontal_radius, self.vertical_radius)

    @property
    def center(self) -> Point:
        return self._center

    @property
    def horizontal_radius(self) -> float:
        return self._horizontal_radius

    @property
    def vertical_radius(self) -> float:
        return self._vertical_radius


class RegularPolygon(Shape):
    _center: Point
    _radius: float
    _vertex_count: int

    def __init__(self, center: Point, radius: float, vertex_count: int, color: Color):
        if radius <= 0:
            raise ValueError('Cannot create Regular Polygon with non positive radius')

        super().__init__(color)
        self._center = center
        self._radius = radius
        self._vertex_count = vertex_count

    def draw(self, canvas: CanvasInterface):
        canvas.set_color(self.color)

        vertexes = self._get_vertexes()
        vertexes.append(vertexes[0])

        prev: Optional[Point] = None
        for vertex in vertexes:
            if prev is not None:
                canvas.draw_line(prev, vertex)
            prev = vertex

    def _get_vertexes(self) -> List[Point]:
        vertexes = []
        fi = 360 / self._vertex_count
        for i in range(self._vertex_count):
            x = self.center.x + self.radius * cos(fi + 2 * pi/self._vertex_count)
            y = self.center.x + self.radius * sin(fi + 2 * pi/self._vertex_count)
            vertexes.append(Point(x, y))
        return vertexes

    @property
    def center(self) -> Point:
        return self._center

    @property
    def radius(self) -> float:
        return self._radius

    @property
    def vertex_count(self) -> int:
        return self._vertex_count
