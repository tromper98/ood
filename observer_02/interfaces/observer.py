from typing import Protocol

from observer_02.dataclass import WeatherInfo


class ObserverInterface(Protocol):
    def update(self, info: WeatherInfo):
        ...
