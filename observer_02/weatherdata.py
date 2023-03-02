from typing import Dict

from lib import ObserverInterface, ObservableInterface, WeatherInfo


class WeatherData(ObservableInterface):
    _temperature: float
    _humidity: float
    _pressure: float
    _wind_direction: float
    _wind_speed: float
    _description: str
    _observers: Dict[ObserverInterface, float]

    def __init__(self, description: str):
        self._temperature = 0.0
        self._humidity = 0.0
        self._pressure = 760
        self._wind_direction = 0.0
        self._wind_speed = 0.0
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
            #Проверить как обновляется коллекция при изменении ее в процессе итерации

    def measurements_changed(self):
        self.notify_observers()

    def get_measurements(self) -> WeatherInfo:
        return WeatherInfo(temperature=self.temperature,
                           humidity=self.humidity,
                           pressure=self.pressure,
                           wind_direction=self._wind_direction,
                           wind_speed=self._wind_speed)

    def set_measurements(self, temperature: float, humidity: float, pressure: float, wind_direction: float, wind_speed: float):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self._wind_direction = wind_direction
        self._wind_speed = wind_speed

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
    def wind_direction(self) -> float:
        return self._wind_direction

    @property
    def wind_speed(self) -> float:
        return self._wind_speed

    def get_info(self) -> str:
        return self._description
