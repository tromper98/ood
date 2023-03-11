from .impl.interfaces import ObserverInterface
from .impl import MeasureCalc, WindMeasureCalc, WeatherInfo


class Display(ObserverInterface):
    _source_description: str

    def __init__(self):
        self._source_description = ''

    def update(self, observable, info: WeatherInfo):
        self._source_description = observable.get_info()
        print('-' * 15, end='\n')
        print(f'Info from {self._source_description} sensor', end='\n\n')
        self._display_weather_info(info)
        if info.wind_direction:
            self._display_wind_data(info)
        print('-' * 15, end='\n\n')

    @staticmethod
    def _display_weather_info(info: WeatherInfo) -> None:
        print(f'Current Temp: {info.temperature}')
        print(f'Current Pressure: {info.pressure}')
        print(f'Current Humidity: {info.humidity}')

    @staticmethod
    def _display_wind_data(info: WeatherInfo) -> None:
        print(f'Current Wind Direction: {info.wind_direction}')
        print(f'Current Wind Speed: {info.wind_speed}')


class StatisticDisplay(ObserverInterface):
    _temperature_calc: MeasureCalc
    _pressure_calc: MeasureCalc
    _humidity_calc: MeasureCalc

    _source_description: str

    def __init__(self):
        self._temperature_calc = MeasureCalc()
        self._humidity_calc = MeasureCalc()
        self._pressure_calc = MeasureCalc()
        self._wind_calc = WindMeasureCalc()

        self._source_description = ''

    def update(self, observable, info: WeatherInfo):
        self._update_measurements(info)
        self._display_measurements(observable.get_info())

    def _update_measurements(self, info: WeatherInfo) -> None:
        self._temperature_calc.update_values(info.temperature)
        self._pressure_calc.update_values(info.pressure)
        self._humidity_calc.update_values(info.humidity)
        if info.wind_direction:
            self._wind_calc.update_values(info.wind_speed, info.wind_direction)

    def _display_measurements(self, source_name: str) -> None:
        print('-' * 15, end='\n')
        print(f'Info from {source_name} sensor', end='\n\n')
        self._display_measurement('temperature', self._temperature_calc)
        self._display_measurement('humidity', self._humidity_calc)
        self._display_measurement('pressure', self._pressure_calc)
        self._display_avg_wind_measurement()
        print('-' * 15, end='\n\n')

    @staticmethod
    def _display_measurement(measure: str, values: MeasureCalc):
        print(f'Max {measure}: {round(values.max_value, 2)}')
        print(f'Min {measure}: {round(values.min_value, 2)}')
        print(f'Avg {measure}: {round(values.avg_value, 2)}')
        print()

    def _display_avg_wind_measurement(self):
        print(f'Avg wind direction: {round(self._wind_calc.avg_direction, 2)}')
        print(f'Avg wind speed: {round(self._wind_calc.avg_speed, 2)}')
        print()
