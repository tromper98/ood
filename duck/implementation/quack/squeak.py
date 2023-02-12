from .quackstrategy import QuackStrategy


class Squeak(QuackStrategy):
    def __init__(self):
        super().__init__()

    def quack(self) -> str:
        return 'пищим'
