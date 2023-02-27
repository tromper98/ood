from typing import Dict

from interfaces import ObservableInterface, ObserverInterface
from weatherinfo import WeatherInfo


class WeatherStation(ObservableInterface):
    __temperature: float
    __humidity: float
    __pressure: float
    _observers: Dict[ObserverInterface, float]

    def __init__(self):
        self.__temperature = 0.0
        self.__humidity = 0.0
        self.__pressure = 760
        self._observers = {}

    def register_observer(self, observer: ObserverInterface, priority: int):
        self._observers[observer] = priority
        sorted_observers = sorted(self._observers.items(), key=lambda x: x[1])
        self._observers = dict(sorted_observers)

    def remove_observer(self, observer: ObserverInterface):
        self._observers.pop(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self.get_measurements())

    def measurements_changed(self):
        self.notify_observers()

    def get_measurements(self) -> WeatherInfo:
        return WeatherInfo(temperature=self.temperature, humidity=self.humidity, pressure=self.pressure)

    def set_measurements(self, temperature: float, humidity: float, pressure: float):
        self.__temperature = temperature
        self.__humidity = humidity
        self.__pressure = pressure

        self.measurements_changed()

    @property
    def temperature(self) -> float:
        return self.__temperature

    @property
    def pressure(self) -> float:
        return self.__pressure

    @property
    def humidity(self) -> float:
        return self.__humidity
