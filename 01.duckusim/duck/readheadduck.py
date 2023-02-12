from duck import Duck

from impl.fly import FlyWithWings
from impl.quack import Quack
from impl.dance import Menuet


class ReadHeadDuck(Duck):
    def __init__(self):
        super().__init__(Quack, FlyWithWings, Menuet)

    @staticmethod
    def display() -> str:
        return 'красноголовая утка'
