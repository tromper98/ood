from typing import Protocol

from .color import Color
from .point import Point


class CanvasInterface(Protocol):
    def set_color(self, color: Color):
        ...

    def draw_line(self, start: Point, end: Point):
        ...

    def draw_ellipse(self, x, y, h_radius, v_radius):
        ...
