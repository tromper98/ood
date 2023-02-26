from .duck import Duck

from .lib.fly import FlyWithWings
from .lib.quack import Quack
from .lib.dance import Waltz


class MallardDuck(Duck):
    def __init__(self):
        super().__init__(Quack(), FlyWithWings(), Waltz())

    @staticmethod
    def display() -> str:
        return 'дикая утка'
