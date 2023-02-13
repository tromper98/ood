from .flystrategy import FlyStrategy


class FlyNoWay(FlyStrategy):
    def __init__(self):
        super().__init__()

    def fly(self) -> None:
        ...
