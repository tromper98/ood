from typing import Protocol

from observer_02.weatherinfo import WeatherInfo


class ObserverInterface(Protocol):
    def update(self, observable, info: WeatherInfo):
        ...
