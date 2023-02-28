from typing import Dict

from interfaces.observer import ObserverInterface
from interfaces.observable import ObservableInterface
from weatherinfo import WeatherInfo


class WeatherStation(ObservableInterface):
    _temperature: float
    _humidity: float
    _pressure: float
    _description: str
    _observers: Dict[ObserverInterface, float]

    def __init__(self, description: str):
        self._temperature = 0.0
        self._humidity = 0.0
        self._pressure = 760
        self._description = description
        self._observers = {}

    def register_observer(self, observer: ObserverInterface, priority: int):
        self._observers[observer] = priority
        sorted_observers = sorted(self._observers.items(), key=lambda x: x[1])
        self._observers = dict(sorted_observers)

    def remove_observer(self, observer: ObserverInterface):
        self._observers.pop(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self, self.get_measurements())

    def measurements_changed(self):
        self.notify_observers()

    def get_measurements(self) -> WeatherInfo:
        return WeatherInfo(temperature=self.temperature,
                           humidity=self.humidity,
                           pressure=self.pressure,
                           source_info=self._description)

    def set_measurements(self, temperature: float, humidity: float, pressure: float):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure

        self.measurements_changed()

    @property
    def temperature(self) -> float:
        return self._temperature

    @property
    def pressure(self) -> float:
        return self._pressure

    @property
    def humidity(self) -> float:
        return self._humidity

    @property
    def description(self) -> str:
        return self._description
