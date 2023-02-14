from .duck import Duck

from .lib.fly import FlyWithWings
from .lib.quack import Quack
from .lib.dance import Minuet


class ReadHeadDuck(Duck):
    def __init__(self):
        super().__init__(Quack(), FlyWithWings(), Minuet())

    @staticmethod
    def display() -> str:
        return 'красноголовая утка'
