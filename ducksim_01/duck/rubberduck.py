from .duck import Duck

from .lib.fly import FlyNoWay
from .lib.quack import Squeak
from .lib.dance import NoDance


class RubberDuck(Duck):
    def __init__(self):
        super().__init__(Squeak(), FlyNoWay(), NoDance())

    @staticmethod
    def display() -> str:
        return 'резиновая уточка'
