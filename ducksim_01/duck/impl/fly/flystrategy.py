from typing import Optional
from abc import ABC


class FlyStrategy(ABC):
    _fly_counter: int

    def __init__(self):
        self._fly_counter = 0

    def fly(self) -> Optional[str]:
        ...
