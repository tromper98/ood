from enum import Enum

from .interfaces import BeverageInterface


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
        return f'{self._ice_cube_type.value} ice cubes x {str(self._quantity)}'

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

    def get_condiment_description(self) -> str:
        return f'{self._syrup_type.value} syrup'

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


class Cream(CondimentDecorator):

    def __init__(self, beverage: BeverageInterface):
        super().__init__(beverage)

    def get_condiment_description(self) -> str:
        return 'Cream'

    def get_condiment_cost(self) -> float:
        return 25


class Chocolate(CondimentDecorator):
    _count: int

    def __init__(self, beverage: BeverageInterface, count: int):
        super().__init__(beverage)
        self._count = count

    def get_condiment_description(self) -> str:
        return f'Chocolate slices x {self._count}'

    def get_condiment_cost(self) -> float:
        return 10 * self._count


class LiquorType(Enum):
    NUT = 'Nut'
    CHOCOLATE = 'Chocolate'
    

class Liquor(CondimentDecorator):
    _liquor_type: LiquorType
    
    def __init__(self, beverage: BeverageInterface, liquor_type: LiquorType):
        super().__init__(beverage)
        self._liquor_type = liquor_type
        
    def get_condiment_description(self) -> str:
        return f'{self._liquor_type.value} Liquor'
    
    def get_condiment_cost(self) -> float:
        return 50
