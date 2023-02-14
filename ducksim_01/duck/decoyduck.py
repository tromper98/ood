from .duck import Duck

from .lib.fly import FlyNoWay
from .lib.quack import MuteQuack
from .lib.dance import NoDance


class DecoyDuck(Duck):
    def __init__(self):
        super().__init__(MuteQuack(), FlyNoWay(), NoDance())

    @staticmethod
    def display() -> str:
        return 'маннок для уток'
