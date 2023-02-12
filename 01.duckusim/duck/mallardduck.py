from duck import Duck
from impl.fly import FlyWithWings
from impl.quack import Quack
from impl.dance import Waltz


class MallardDuck(Duck):
    def __init__(self):
        super().__init__(Quack, FlyWithWings, Waltz)

    @staticmethod
    def display() -> str:
        return 'дикая утка'
