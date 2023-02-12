from .dancestrategy import DanceStrategy


class NoDance(DanceStrategy):
    def __init__(self):
        super().__init__()

    def dance(self) -> None:
        ...
