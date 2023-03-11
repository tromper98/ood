from enum import Enum

from interfaces import BeverageInterface


class CondimentDecorator(BeverageInterface):
    _beverage: BeverageInterface

    def __init__(self, beverage: BeverageInterface):
        self._beverage = beverage

    def get_description(self) -> str:
        return self._beverage.get_description() + ', ' + self.get_condiment_description()

    def get_cost(self) -> float:
        return self._beverage.get_cost() + self.get_condiment_cost()

    def get_condiment_description(self) -> str:
        ...

    def get_condiment_cost(self) -> float:
        ...


class Cinnamon(CondimentDecorator):
    def __init__(self, beverage: BeverageInterface):
        super().__init__(beverage)

    def get_condiment_description(self) -> str:
        return 'Cinnamon'

    def get_condiment_cost(self) -> float:
        return 20


class Lemon(CondimentDecorator):
    _quantity: int

    def __init__(self, beverage: BeverageInterface, quantity: int):
        super().__init__(beverage)
        self._quantity = quantity

    def get_condiment_description(self) -> str:
        return f'Lemon x {str(self._quantity)}'

    def get_condiment_cost(self) -> float:
        return 10 * self._quantity


class IceCubeType(Enum):
    DRY = 'Dry'
    WATER = 'Water'


class IceCubes(CondimentDecorator):
    _quantity: int
    _ice_cube_type: IceCubeType

    def __init__(self,
                 beverage: BeverageInterface,
                 quantity: int,
                 ice_cube_type: IceCubeType):
        super().__init__(beverage)
        self._quantity = quantity
        self._ice_cube_type = ice_cube_type

    def get_condiment_description(self) -> str:
        return f'{self._ice_cube_type} ice cubes x {str(self._quantity)}'

    def get_condiment_cost(self) -> float:
        cost: float = 10 if self._ice_cube_type.DRY else 5
        return cost * self._quantity


class SyrupType(Enum):
    CHOCOLATE = 'Chocolate'
    MAPLE = 'Maple'


class Syrup(CondimentDecorator):
    _syrup_type: SyrupType

    def __init__(self,
                 beverage: BeverageInterface,
                 syrup_type: SyrupType):
        super().__init__(beverage)
        self._syrup_type = syrup_type

    def get_description(self) -> str:
        return f'{self._syrup_type} syrup'

    def get_condiment_cost(self) -> float:
        return 15


class ChocolateCrumbs(CondimentDecorator):
    _mass: float

    def __init__(self,
                 beverage: BeverageInterface,
                 mass: float):
        super().__init__(beverage)
        self._mass = mass

    def get_condiment_description(self) -> str:
        return f'Chocolate crumbs {self._mass}g'

    def get_condiment_cost(self) -> float:
        return 2 * self._mass


class CoconutFlakes(CondimentDecorator):
    _mass: float

    def __init__(self,
                 beverage: BeverageInterface,
                 mass: float):
        super().__init__(beverage)
        self._mass = mass

    def get_condiment_description(self) -> str:
        return f'Coconut flakes {self._mass}g'

    def get_condiment_cost(self) -> float:
        return 1 * self._mass
