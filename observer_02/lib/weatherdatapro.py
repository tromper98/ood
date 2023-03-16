from .weatherdata import WeatherData
from .impl import WeatherInfo


class WeatherDataPro(WeatherData):
    _wind_direction: float
    _wind_speed: float
    _description: str

    def __init__(self, description: str):
        super().__init__(description)
        self._wind_direction = 0.0
        self._wind_speed = 0.0

    def get_measurements(self) -> WeatherInfo:
        return WeatherInfo(temperature=self.temperature,
                           humidity=self.humidity,
                           pressure=self.pressure,
                           wind_direction=self._wind_direction,
                           wind_speed=self._wind_speed)

    def set_measurements(self,
                         temperature: float,
                         humidity: float,
                         pressure: float,
                         wind_direction: float = None,
                         wind_speed: float = None):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self._wind_direction = wind_direction
        self._wind_speed = wind_speed

        self.measurements_changed()

    @property
    def wind_direction(self) -> float:
        return self._wind_direction

    @property
    def wind_speed(self) -> float:
        return self._wind_speed

