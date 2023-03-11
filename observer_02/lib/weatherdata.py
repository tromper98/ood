from .impl import WeatherInfo, Observable


class WeatherData(Observable):
    _temperature: float
    _humidity: float
    _pressure: float

    _description: str

    def __init__(self, description: str):
        self._temperature = 0.0
        self._humidity = 0.0
        self._pressure = 760
        self._description = description

        super().__init__()

    def measurements_changed(self):
        self.notify_observers(self.get_measurements()) # Передавать self, не упаковывать в WeatherInfo

    def get_measurements(self) -> WeatherInfo:
        return WeatherInfo(temperature=self.temperature,
                           humidity=self.humidity,
                           pressure=self.pressure)

    def set_measurements(self, temperature: float, humidity: float, pressure: float, *args, **kwargs):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure

        self.measurements_changed()

    def get_info(self) -> str:
        return self._description

    @property
    def temperature(self) -> float:
        return self._temperature

    @property
    def pressure(self) -> float:
        return self._pressure

    @property
    def humidity(self) -> float:
        return self._humidity
