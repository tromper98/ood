from typing import List
from sys import stdin

from .designer import DesignerInterface
from .picturedraft import PictureDraft
from .painter import Painter
from .canvas import CanvasInterface


class Client:
    _canvas: CanvasInterface

    def __init__(self, canvas: CanvasInterface):
        self._canvas = canvas

    def draw_pictures(self, designer: DesignerInterface):
        lines: List[str] = []
        for line in stdin:
            if line == 'exit':
                break
            lines.append(line)

        draft: PictureDraft = designer.create_draft(lines)
        Painter.draw_picture(draft, self._canvas)

