from typing import Tuple, List
from .shapes import *


class ShapeFactoryInterface:

    def create_shape(self, description: str) -> Shape:
        ...


class ShapeFactory(ShapeFactoryInterface):

    def create_shape(self, description: str) -> Shape:
        shape_name, color, params = self._parse_description(description)

        if shape_name == 'rectangle':
            return self._create_rectangle(color, params)
        elif shape_name == 'triangle':
            return self._create_triangle(color, params)
        elif shape_name == 'ellipse':
            return self._create_ellipse(color, params)
        elif shape_name == 'polygon':
            return self._create_regular_polygon(color, params)
        else:
            raise ValueError('Invalid shape name')

    @staticmethod
    def _create_rectangle(color: Color, params: List[float]) -> Shape:
        if len(params) != 4:
            raise ValueError('Invalid argument count to create rectangle')
        return Rectangle(Point(params[0], params[1]), Point(params[2], params[3]), color)

    @staticmethod
    def _create_ellipse(color: Color, params: List[float]) -> Shape:
        if len(params) != 4:
            raise ValueError('Invalid argument count to create ellipse')
        return Ellipse(Point(params[0], params[1]), params[2], params[3], color)

    @staticmethod
    def _create_triangle(color: Color, params: List[float]) -> Shape:
        if len(params) != 6:
            raise ValueError('Invalid argument count to create triangle')
        return Triangle(Point(params[0], params[1]), Point(params[2], params[3]), Point(params[4], params[5]), color)

    @staticmethod
    def _create_regular_polygon(color: Color, params: List[float]) -> Shape:
        if len(params) != 4:
            raise ValueError('Invalid argument count to create regular polygon')
        return RegularPolygon(Point(params[0], params[1]), params[2], int(params[3]), color)

    def _parse_description(self, desc: str) -> Tuple[str, Color, List[float]]:
        desc = desc.lstrip().lstrip().lower()
        params: List[str] = desc.split(' ')
        parsed_params: List[float] = []

        shape_name: str = params[0]
        color_name: str = params[1]
        params = params[2:]
        for param in params:
            if not self._is_float(param):
                print(f'Cannot convert {param} to float')
                break
            else:
                parsed_params.append(float(param))

        color: Color = self._get_color(color_name)
        return shape_name, color, parsed_params

    @staticmethod
    def _is_float(n: str) -> bool:
        try:
            float(n)
            return True
        except ValueError:
            return False

    @staticmethod
    def _get_color(name: str) -> Color:
        for color in Color:
            if color.name.lower() == name:
                return color
        raise ValueError('Invalid Color')
