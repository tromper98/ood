from .quackstrategy import QuackStrategy


class Quack(QuackStrategy):
    def __init__(self):
        super().__init__()

    def quack(self) -> str:
        return 'Крякаем'
