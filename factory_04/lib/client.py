from sys import stdin

from .designer import DesignerInterface
from .picturedraft import PictureDraft
from .painter import Painter
from .canvas import CanvasInterface


class Client:
    _canvas: CanvasInterface

    def __init__(self, canvas: CanvasInterface):
        self._canvas = canvas

    def draw_pictures(self, designer: DesignerInterface, stream: stdin):
        draft: PictureDraft = designer.create_draft(stream)
        Painter.draw_picture(draft, self._canvas)

