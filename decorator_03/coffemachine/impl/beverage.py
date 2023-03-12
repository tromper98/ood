from enum import Enum

from .interfaces import BeverageInterface


class Beverage(BeverageInterface):
    _description: str

    def __init__(self, description: str):
        self._description = description

    def get_description(self) -> str:
        return self._description


class CoffeePortion(Enum):
    SINGLE = 'single'
    DOUBLE = 'double'


class Coffee(Beverage):
    _portion: CoffeePortion

    def __init__(self, description: str = 'Coffee', portion: CoffeePortion = CoffeePortion.SINGLE):
        super().__init__(description)
        self._portion = portion

    def get_cost(self) -> float:
        return 60


class Cappuccino(Coffee):

    def __init__(self, portion: CoffeePortion):
        super().__init__(f'{portion.value} Cappuccino', portion)

    def get_cost(self) -> float:
        cost = 120 if self._portion.DOUBLE else 80
        return cost


class Latte(Coffee):
    _portion: CoffeePortion

    def __init__(self, portion: CoffeePortion):
        super().__init__(f'{portion.value} Latte', portion)

    def get_cost(self) -> float:
        cost = 130 if self._portion.DOUBLE else 90
        return cost


class TeaType(Enum):
    OOLONG = 'Oolong'
    BLACK = 'Black'
    GREEN = 'Green'
    HERBAL = 'Herbal'


class Tea(Beverage):
    _tea_type: TeaType

    def __init__(self, tea_type: TeaType):
        super().__init__(f'{tea_type.value} Tea')
        self._tea_type = tea_type

    def get_cost(self) -> float:
        return 30


class MilkshakePortion(Enum):
    SMALL = 'Small'
    MEDIUM = 'Medium'
    BIG = 'Big'


class Milkshake(Beverage):
    _portion: MilkshakePortion

    def __init__(self, portion: MilkshakePortion):
        super().__init__(f'{portion.value} Milkshake')
        self._portion = portion

    def get_cost(self) -> float:
        if self._portion.SMALL:
            cost = 50
        elif self._portion.MEDIUM:
            cost = 60
        else:
            cost = 80

        return cost
