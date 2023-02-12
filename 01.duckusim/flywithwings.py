from .flystrategy import FlyStrategy


class FlyWithWings(FlyStrategy):
    def __init__(self):
        super().__init__()

    def fly(self) -> str:
        return 'летим, машем крылышками'
