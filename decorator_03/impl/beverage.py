from .interfaces import BeverageInterface


class Beverage(BeverageInterface):
    _description: str

    def __init__(self, description: str):
        self._description = description

    def get_description(self) -> str:
        return self._description


class Coffee(Beverage):
    def __init__(self, description: str = 'Coffee'):
        super().__init__(description)

    def get_cost(self) -> float:
        return 60


class Cappuccino(Coffee):
    def __init__(self):
        super().__init__('Cappuccino')

    def get_cost(self) -> float:
        return 80


class Latte(Coffee):
    def __init__(self):
        super().__init__('Latte')

    def get_cost(self) -> float:
        return 90


class Tea(Beverage):
    def __init__(self):
        super().__init__('Tea')

    def get_cost(self) -> float:
        return 30
