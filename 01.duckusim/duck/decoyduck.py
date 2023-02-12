from duck import Duck

from impl.fly import FlyNoWay
from impl.quack import MuteQuack
from impl.dance import NoDance


class DecoyDuck(Duck):
    def __init__(self):
        super().__init__(MuteQuack, FlyNoWay, NoDance)

    @staticmethod
    def display() -> str:
        return 'маннок для уток'
