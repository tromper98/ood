from dataclasses import dataclass


@dataclass()
class WeatherInfo:
    temperature: float
    pressure: float
    humidity: float
    source_info: str
