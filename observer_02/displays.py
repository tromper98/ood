import math

from lib import ObserverInterface, ObservableInterface
from lib.weatherinfo import WeatherInfo


class Display(ObserverInterface):
    _source_info: str

    def update(self, observable: ObservableInterface, info: WeatherInfo):
        self._source_info = observable.get_info()
        print(f'Source: {self._source_info}')
        print(f'Current Temp: {info.temperature}')
        print(f'Current Pressure: {info.pressure}')
        print(f'Current Humidity: {info.humidity}')
        print(f'Current Wind Direction: {info.wind_direction}')
        print(f'Current Wind Speed: {info.wind_speed}')
        print('-' * 10)


class StatisticDisplay(ObserverInterface):
    _min_temperature: float
    _max_temperature: float
    _sum_temperature: float

    _min_pressure: float
    _max_pressure: float
    _sum_pressure: float

    _min_humidity: float
    _max_humidity: float
    _sum_humidity: float

    _avg_wind_direction: float
    _avg_wind_speed: float

    _sum_sin: float
    _sum_cos: float

    _measure_count: int

    def __init__(self):
        self._min_temperature = 0.0
        self._max_temperature = 0.0
        self._sum_temperature = 0.0

        self._min_pressure = 0.0
        self._max_pressure = 0.0
        self._sum_pressure = 0.0

        self._min_humidity = 0.0
        self._max_humidity = 0.0
        self._sum_humidity = 0.0

        self._avg_wind_direction = 0.0
        self._avg_wind_direction = 0.0

        self._sum_sin = 0.0
        self._sum_cos = 0.0

        self._measure_count = 0
        self._source_info = None

    def update(self, observable: ObservableInterface, info: WeatherInfo):
        self._source_info = observable.get_info()
        self._measure_count += 1
        self._update_temperature(info)
        self._update_pressure(info)
        self._update_humidity(info)
        self._update_avg_wind_parameters(info)

    def _update_temperature(self, info: WeatherInfo):
        if self._min_temperature > info.temperature:
            self._min_temperature = info.temperature

        if self._max_temperature < info.temperature:
            self._max_temperature = info.temperature

        self._sum_temperature += info.temperature

        self._display_measurement(self._max_temperature,
                                  self._min_temperature,
                                  self._sum_temperature,
                                  'Temperature')

    # Устранить дублирование кода. Минимальное, максимальное, среднее
    def _update_pressure(self, info: WeatherInfo):
        if self._min_pressure > info.pressure:
            self._min_pressure = info.pressure

        if self._max_pressure < info.pressure:
            self._max_pressure = info.pressure

        self._sum_pressure += info.pressure

        self._display_measurement(self._max_pressure,
                                  self._min_pressure,
                                  self._sum_pressure,
                                  'Pressure')

    def _update_humidity(self, info: WeatherInfo):
        if self._min_humidity > info.humidity:
            self._min_humidity = info.humidity

        if self._max_humidity < info.humidity:
            self._max_humidity = info.humidity

        self._sum_humidity += info.humidity

        self._display_measurement(self._max_humidity,
                                  self._min_humidity,
                                  self._sum_humidity,
                                  'Humidity')

    def _update_avg_wind_parameters(self, info: WeatherInfo):
        self._sum_sin += info.wind_speed * math.sin(math.radians(info.wind_direction))
        self._sum_cos += info.wind_speed * math.cos(math.radians(info.wind_direction))

        avg_sin = self._sum_sin / self._measure_count
        avg_cos = self._sum_cos / self._measure_count

        self._avg_wind_direction = (math.degrees(math.atan2(avg_sin, avg_cos)) + 360) % 360
        self._avg_wind_speed = math.sqrt(avg_sin * avg_sin + avg_cos * avg_cos)

        self._display_avg_wind_measurement()

    def _display_measurement(self, max_value: float, min_value: float, sum_values: float, measure: str):
        print(f'Source: {self._source_info}')
        print(f'Max {measure}: {max_value}')
        print(f'Min {measure}: {min_value}')
        print(f'Avg {measure}: {round(sum_values / self._measure_count, 2)}')
        print('-' * 10)

    def _display_avg_wind_measurement(self):
        print(f'Source: {self._source_info}')
        print(f'Avg wind direction: {round(self._avg_wind_direction, 2)}')
        print(f'Avg wind speed: {round(self._avg_wind_speed, 2)}')
        print('-' * 10)
