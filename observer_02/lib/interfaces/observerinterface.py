from typing import Protocol

from .. import WeatherInfo


class ObserverInterface(Protocol):
    def update(self, observable, info: WeatherInfo):
        ...
