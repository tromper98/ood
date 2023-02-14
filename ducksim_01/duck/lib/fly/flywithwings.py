from .flystrategy import FlyStrategy


class FlyWithWings(FlyStrategy):
    def __init__(self):
        super().__init__()

    def fly(self) -> str:
        self._fly_counter += 1
        return f'летим, машем крылышками. Полет под номером {self._fly_counter}'
