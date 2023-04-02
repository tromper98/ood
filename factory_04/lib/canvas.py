from typing import Protocol, Tuple
from svgwrite import Drawing
from svgwrite.utils import rgb

from .color import Color
from .point import Point


LENGTH = 1920
WIDTH = 1080


class CanvasInterface(Protocol):
    def set_color(self, color: Color):
        ...

    def draw_line(self, start: Point, end: Point):
        ...

    def draw_ellipse(self, x: float, y: float, h_radius: float, v_radius: float):
        ...


class SVGCanvas(CanvasInterface):
    _painter: Drawing
    _center: Point
    _color: Color

    def __init__(self, file_name: str):
        self._painter = Drawing(file_name, size=(LENGTH, WIDTH))
        self._center = Point(LENGTH / 2, WIDTH / 2)
        self._color = Color.Black

    def set_color(self, color: Color):
        self._color = color

    def draw_line(self, start: Point, end: Point):
        new_start = self._move_origin(start)
        new_end = self._move_origin(end)
        self._painter.add(
            self._painter.line(new_start, new_end, stroke=self._color)
        )

    def draw_ellipse(self, x: float, y: float, h_radius: float, v_radius: float):
        center = self._move_origin(Point(x, y))
        self._painter.add(
            self._painter.ellipse(center, (h_radius, v_radius), stroke=self._color)
        )

    def _move_origin(self, point: Point) -> Tuple[float, float]:
        return self.x + point.x, self.y - point.y

    @property
    def x(self) -> float:
        return self._center.x

    @property
    def y(self) -> float:
        return self._center.y
