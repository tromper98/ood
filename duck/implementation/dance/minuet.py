from dancestrategy import DanceStrategy


class Minuet(DanceStrategy):
    def __init__(self):
        super().__init__()

    def dance(self) -> str:
        return 'танцует минует'
