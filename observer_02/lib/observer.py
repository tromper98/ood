from typing import Protocol

from .weatherinfo import WeatherInfo


class ObserverInterface(Protocol):
    def update(self, observable, info: WeatherInfo):
        ...
