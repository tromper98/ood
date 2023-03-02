from observer_02.lib.weatherdata import WeatherData
from displays import *


in_station = WeatherData('in house station')
out_station = WeatherData('outdoor station')

display = Display()
stats_display = StatisticDisplay()

in_station.register_observer(display, 2)
out_station.register_observer(display, 2)

in_station.set_measurements(24, 50.5, 760, 0, 0)
out_station.set_measurements(30, 93.3, 760, 90, 2)

in_station.register_observer(stats_display, 1)
out_station.register_observer(stats_display, 1)

in_station.set_measurements(26, 50, 767, 0, 0)
out_station.set_measurements(32, 95.5, 770, 94, 4)

in_station.remove_observer(display)

in_station.set_measurements(23, 43, 760, 0, 0)
out_station.set_measurements(39, 90.5, 780, 120, 15)

pass
