from .picturedraft import PictureDraft
from .canvas import CanvasInterface


class Painter:

    @staticmethod
    def draw_picture(draft: PictureDraft, canvas: CanvasInterface) -> None:
        for shape in draft.shapes:
            shape.draw(canvas)
