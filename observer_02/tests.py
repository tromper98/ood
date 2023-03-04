from observer_02.lib.weatherdata import WeatherData
from observer_02.lib.displays import *


def test_observer_priority():
    display = Display()
    stats_display = StatisticDisplay()

    station = WeatherData('test station')

    station.register_observer(stats_display, 2)
    station.register_observer(display, 1)
    observer_iter = iter(station._observers)
    assert isinstance(next(observer_iter), Display)
    assert isinstance(next(observer_iter), StatisticDisplay)


def test_get_data_from_to_weather_data():
    display = Display()

    first_station = WeatherData('first_station')
    second_station = WeatherData('second_station')

    first_station.register_observer(display, 1)
    second_station.register_observer(display, 1)

    first_station.set_measurements(1, 1, 1, 0, 0)
    assert display._source_description == 'first_station'

    second_station.set_measurements(2, 2, 2, 0, 0)
    assert display._source_description == 'second_station'
