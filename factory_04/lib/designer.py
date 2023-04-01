from typing import Protocol
import fileinput

from .shapefactory import ShapeFactoryInterface
from .picturedraft import PictureDraft


class DesignerInterface(Protocol):
    def create_draft(self, description: str) -> PictureDraft:
        ...


class Designer(DesignerInterface):
    _shape_factory: ShapeFactoryInterface

    def __init__(self, factory: ShapeFactoryInterface):
        self._shape_factory = factory

    def create_draft(self, input_stream: str) -> PictureDraft:
        draft = PictureDraft()
        for line in fileinput.input():
            draft.add_shape(self._shape_factory.create_shape(line))
        return draft
