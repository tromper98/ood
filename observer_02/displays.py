from interfaces import ObserverInterface
from weatherinfo import WeatherInfo


class Display(ObserverInterface):
    def update(self, info: WeatherInfo):
        print(f'Current Temp: {info.temperature}')
        print(f'Current Pressure: {info.pressure}')
        print(f'Current Humidity: {info.humidity}')
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
        self._measure_count = 0

    def update(self, info: WeatherInfo):
        self._measure_count += 1
        self._update_temperature(info)
        self._update_pressure(info)
        self._update_humidity(info)

    def _update_temperature(self, info: WeatherInfo):
        if self._min_temperature > info.temperature:
            self._min_temperature = info.temperature

        if self._max_temperature < info.temperature:
            self._max_temperature = info.temperature

        self._sum_temperature += info.temperature

        self._display_measurement(self._max_temperature, self._min_temperature, self._sum_temperature, 'Temperature')

    def _update_pressure(self, info: WeatherInfo):
        if self._min_pressure > info.pressure:
            self._min_pressure = info.pressure

        if self._max_pressure < info.pressure:
            self._max_pressure = info.pressure

        self._sum_pressure += info.pressure

        self._display_measurement(self._max_pressure, self._min_pressure, self._sum_pressure, 'Pressure')

    def _update_humidity(self, info: WeatherInfo):
        if self._min_humidity > info.humidity:
            self._min_humidity = info.humidity

        if self._max_humidity < info.humidity:
            self._max_humidity = info.humidity

        self._sum_humidity += info.humidity

        self._display_measurement(self._max_humidity, self._min_humidity, self._sum_humidity, 'Humidity')

    def _display_measurement(self, max_value: float, min_value: float, sum_values: float, measure: str):
        print(f'Max {measure}: {max_value}')
        print(f'Min {measure}: {min_value}')
        print(f'Avg {measure}: {sum_values / self._measure_count}')
        print('-' * 10)
