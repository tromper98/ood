from weatherstation import WeatherStation
from displays import *


station = WeatherStation()

display = Display()
stats_display = StatisticDisplay()

station.register_observer(display)

station.set_measurements(30, 70.5, 780)

station.register_observer(stats_display)


station.set_measurements(20, 50, 767)

station.remove_observer(display)

station.set_measurements(40, 73, 780)
pass