from .lib.weatherdata import WeatherData
from .lib.displays import *
from .lib.impl.interfaces import *


class DisplaySubscriber(Display):

    @staticmethod
    def subscribe_observer(observable: ObservableInterface, observer: ObserverInterface):
        observable.register_observer(observer, 2)

    @staticmethod
    def remove_observer(observable: ObservableInterface, observer: ObserverInterface):
        observable.remove_observer(observer)


def test_observer_priority():
    display = Display()
    stats_display = StatisticDisplay()

    data = WeatherData('test station')

    data.register_observer(stats_display, 2)
    data.register_observer(display, 1)
    observer_iter = iter(data._observers)
    assert isinstance(next(observer_iter), Display)
    assert isinstance(next(observer_iter), StatisticDisplay)


def test_get_data_from_to_weather_data():
    display = Display()

    first_data = WeatherData('first_station')
    second_data = WeatherData('second_station')

    first_data.register_observer(display, 1)
    second_data.register_observer(display, 1)

    first_data.set_measurements(1, 1, 1, 0, 0)
    assert display._source_description == 'first_station'

    second_data.set_measurements(2, 2, 2, 0, 0)
    assert display._source_description == 'second_station'


def test_subscribe_observer_from_other_observer():
    display1 = DisplaySubscriber()
    display2 = Display()

    weather_data = WeatherData('test station')

    weather_data.register_observer(display1, 1)
    display1.subscribe_observer(weather_data, display2)

    weather_data.set_measurements(1, 1, 1, 0, 0)
    observer_iter = iter(weather_data._observers)
    assert next(observer_iter) == display1
    assert next(observer_iter) == display2


def test_remove_observer_from_other_observer():
    display1 = DisplaySubscriber()
    display2 = Display()
    display3 = Display()

    weather_data = WeatherData('test station')
    weather_data.register_observer(display1, 1)
    weather_data.register_observer(display2, 5)
    weather_data.register_observer(display3, 3)

    assert len(weather_data._observers) == 3
    display1.remove_observer(weather_data, display2)
    assert len(weather_data._observers) == 2
