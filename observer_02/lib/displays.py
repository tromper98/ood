from typing import Optional, Dict

from .impl.interfaces import ObserverInterface, ObservableInterface
from .impl import MeasureCalc, WindMeasureCalc, WeatherInfo
from .weatherdatapro import WeatherDataPro


class Display(ObserverInterface):
    _source_description: str

    def __init__(self):
        self._source_description = ''

    def update(self, observable: ObservableInterface, info: WeatherInfo):
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


class ObservableStatistic:
    _observable: ObservableInterface
    temperature_calc: MeasureCalc
    pressure_calc: MeasureCalc
    humidity_calc: MeasureCalc
    wind_calc: Optional[WindMeasureCalc]

    description: str

    def __init__(self, observable: ObservableInterface) -> None:
        self._observable = observable
        self.description = observable.get_info()
        self.temperature_calc = MeasureCalc()
        self.pressure_calc = MeasureCalc()
        self.humidity_calc = MeasureCalc()

        if isinstance(observable, WeatherDataPro):
            self.wind_calc = WindMeasureCalc()
        else:
            self.wind_calc = None

    def update_measurements(self, info: WeatherInfo):
        self.temperature_calc.update_values(info.temperature)
        self.pressure_calc.update_values(info.pressure)
        self.humidity_calc.update_values(info.humidity)

        if self.wind_calc:
            self.wind_calc.update_values(info.wind_speed, info.wind_direction)


class StatisticDisplay(ObserverInterface):
    _observables: Dict[ObservableInterface, ObservableStatistic]

    def __init__(self):
        self._observables = {}

    def update(self, observable: ObservableInterface, info: WeatherInfo) -> None:
        if observable not in self._observables.keys():
            self._observables[observable] = ObservableStatistic(observable)

        statistics: ObservableStatistic = self._observables[observable]
        statistics.update_measurements(info)

        self._display_measurements(statistics)

    def _display_measurements(self, statistics: ObservableStatistic) -> None:
        print('-' * 15, end='\n')
        print(f'Info from {statistics.description} sensor', end='\n\n')
        self._display_measurement('temperature', statistics.temperature_calc)
        self._display_measurement('humidity', statistics.humidity_calc)
        self._display_measurement('pressure', statistics.pressure_calc)

        if statistics.wind_calc:
            self._display_avg_wind_measurement(statistics.wind_calc)
        print('-' * 15, end='\n\n')

    @staticmethod
    def _display_measurement(measure: str, values: MeasureCalc):
        print(f'Max {measure}: {round(values.max_value, 2)}')
        print(f'Min {measure}: {round(values.min_value, 2)}')
        print(f'Avg {measure}: {round(values.avg_value, 2)}')
        print()

    @staticmethod
    def _display_avg_wind_measurement(values: WindMeasureCalc):
        print(f'Avg wind direction: {round(values.avg_direction, 2)}')
        print(f'Avg wind speed: {round(values.avg_speed, 2)}')
        print()
