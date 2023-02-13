from .quackstrategy import QuackStrategy


class MuteQuack(QuackStrategy):
    def __init__(self):
        super().__init__()

    def quack(self) -> None:
        ...
