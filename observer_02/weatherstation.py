from typing import List

from interfaces import ObservableInterface, ObserverInterface
from dataclass import WeatherInfo


class WeatherStation(ObservableInterface):
    __temperature: float
    __humidity: float
    __pressure: float
    __observers: List[ObserverInterface]

    def __init__(self):
        self.__temperature = 0.0
        self.__humidity = 0.0
        self.__pressure = 760
        self.__observers = []

    def register_observer(self, observer: ObserverInterface):
        self.__observers.append(observer)

    def remove_observer(self, observer: ObserverInterface):
        self.__observers.remove(observer)

    def notify_observers(self):
        for observer in self.__observers:
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
