from typing import Protocol

from .color import Color


class CanvasInterface(Protocol):
    def set_color(self, color: Color):
        ...

    def draw_line(self, start, end):
        ...

    def draw_ellipse(self, x, y, h_radius, v_radius):
        ...
