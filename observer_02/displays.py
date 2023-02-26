from interfaces import ObserverInterface
from dataclass import WeatherInfo


class Display(ObserverInterface):
    def update(self, info: WeatherInfo):
        print(f'Current Temp: {info.temperature}')
        print(f'Current Pressure: {info.pressure}')
        print(f'Current Humidity: {info.humidity}')
        print('-' * 10)


class StatisticDisplay(ObserverInterface):
    _min_temperature: float = 0.0
    _max_temperature: float = 0.0
    _avg_temperature: float = 0.0
    _sum_temperature: float = 0.0
    _measure_count: int = 0

    def update(self, info: WeatherInfo):
        if self._min_temperature > info.temperature:
            self._min_temperature = info.temperature

        if self._max_temperature < info.temperature:
            self._max_temperature = info.temperature

        self._sum_temperature += info.temperature
        self._measure_count += 1

        print(f'Max Temperature: {self._max_temperature}')
        print(f'Min Temperature: {self._min_temperature}')
        print(f'Avg Temperature: {self._sum_temperature / self._avg_temperature}')
        print('-' * 10)
