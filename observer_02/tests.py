import pytest

from weatherstation import WeatherStation
from displays import *


def test_observer_priority():
    display = Display()
    stats_display = StatisticDisplay()

    station = WeatherStation('test station')

    station.register_observer(stats_display, 2)
    station.register_observer(display, 1)
    observer_iter = iter(station._observers)
    assert isinstance(next(observer_iter), Display)
    assert isinstance(next(observer_iter), StatisticDisplay)
