from .duck import Duck

from .impl.fly import FlyWithWings
from .impl.quack import Quack
from .impl.dance import Minuet


class ReadHeadDuck(Duck):
    def __init__(self):
        super().__init__(Quack, FlyWithWings, Minuet)

    @staticmethod
    def display() -> str:
        return 'красноголовая утка'
