from typing import List

from .shapes import Shape


class PictureDraft:
    shapes: List

    def __init__(self):
        self.shapes = []

    def add_shape(self, shape: Shape) -> None:
        self.shapes.append(shape)

    def get_shape_count(self) -> int:
        return len(self.shapes)
