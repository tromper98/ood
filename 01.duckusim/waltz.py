from dancestrategy import DanceStrategy


class Waltz(DanceStrategy):
    def __init__(self):
        super().__init__()

    def dance(self) -> str:
        return 'танцует вальс'
