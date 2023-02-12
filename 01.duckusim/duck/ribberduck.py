from duck import Duck

from impl.fly import FlyNoWay
from impl.quack import Squeak
from impl.dance import NoDance


class RibberDuck(Duck):
    def __init__(self):
        super().__init__(Squeak, FlyNoWay, NoDance)

    @staticmethod
    def display() -> str:
        return 'резиновая уточка'
