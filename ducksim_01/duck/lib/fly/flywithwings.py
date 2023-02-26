from .flystrategy import FlyStrategy


class FlyWithWings(FlyStrategy):
    _fly_counter: int

    def __init__(self):
        self._fly_counter = 0

    def fly(self) -> str:
        self._fly_counter += 1
        return f'летим, машем крылышками. Полет под номером {self._fly_counter}'
