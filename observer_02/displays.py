import math

from lib.interfaces import ObserverInterface, ObservableInterface
from lib import WeatherCalc, WeatherInfo


class Display(ObserverInterface):
    _source_info: str

    def update(self, info: WeatherInfo):
        print('-' * 15, end='\n')
        print(f'Info from {info.source_description} sensor', end='\n\n')
        print(f'Current Temp: {info.temperature}')
        print(f'Current Pressure: {info.pressure}')
        print(f'Current Humidity: {info.humidity}')
        print(f'Current Wind Direction: {info.wind_direction}')
        print(f'Current Wind Speed: {info.wind_speed}')
        print('-' * 15, end='\n\n')


class StatisticDisplay(ObserverInterface):
    _temperature_calc: WeatherCalc
    _pressure_calc: WeatherCalc
    _humidity_calc: WeatherCalc

    _avg_wind_direction: float
    _avg_wind_speed: float

    _sum_sin: float
    _sum_cos: float

    _measure_count: int

    def __init__(self):
        self._temperature_calc = WeatherCalc()
        self._humidity_calc = WeatherCalc()
        self._pressure_calc = WeatherCalc()

        self._avg_wind_direction = 0.0
        self._avg_wind_direction = 0.0

        self._sum_sin = 0.0
        self._sum_cos = 0.0

        self._measure_count = 0

    def update(self, info: WeatherInfo):
        self._update_measurements(info)
        self._display_measurements(info.source_description)

#        self._update_avg_wind_parameters(info)

        self._measure_count += 1

    def _update_measurements(self, info: WeatherInfo) -> None:
        self._update_temperature(info.temperature)
        self._update_pressure(info.pressure)
        self._update_humidity(info.humidity)

    def _display_measurements(self, source_name: str) -> None:
        print('-' * 15, end='\n')
        print(f'Info from {source_name} sensor', end='\n\n')
        self._display_temperature()
        self._display_humidity()
        self._display_pressure()
        print('-' * 15, end='\n\n')

    # Устранить дублирование кода. Минимальное, максимальное, среднее
    def _update_temperature(self, temperature: float):
        self._temperature_calc.update_values(temperature)

    def _update_pressure(self, pressure: float):
        self._temperature_calc.update_values(pressure)

    def _update_humidity(self, humidity: float):
        self._humidity_calc.update_values(humidity)

    def _display_temperature(self):
        self._display_measurement('temperature', self._temperature_calc)

    def _display_humidity(self):
        self._display_measurement('humidity', self._humidity_calc)

    def _display_pressure(self):
        self._display_measurement('pressure', self._pressure_calc)

    @staticmethod
    def _display_measurement(measure: str, values: WeatherCalc):
        print(f'Max {measure}: {round(values.max_value, 2)}')
        print(f'Min {measure}: {round(values.min_value, 2)}')
        print(f'Avg {measure}: {round(values.avg_value, 2)}')
        print()

    # def _update_avg_wind_parameters(self, info: WeatherInfo):
    #     self._sum_sin += info.wind_speed * math.sin(math.radians(info.wind_direction))
    #     self._sum_cos += info.wind_speed * math.cos(math.radians(info.wind_direction))
    #
    #     avg_sin = self._sum_sin / self._measure_count
    #     avg_cos = self._sum_cos / self._measure_count
    #
    #     self._avg_wind_direction = (math.degrees(math.atan2(avg_sin, avg_cos)) + 360) % 360
    #     self._avg_wind_speed = math.sqrt(avg_sin * avg_sin + avg_cos * avg_cos)
    #
    #     self._display_avg_wind_measurement()

    # def _display_avg_wind_measurement(self):
    #     print(f'Source: {self._source_info}')
    #     print(f'Avg wind direction: {round(self._avg_wind_direction, 2)}')
    #     print(f'Avg wind speed: {round(self._avg_wind_speed, 2)}')
    #     print()
