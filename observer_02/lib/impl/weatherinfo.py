from typing import Optional
from dataclasses import dataclass


@dataclass()
class WeatherInfo:
    temperature: float
    pressure: float
    humidity: float
    wind_direction: Optional[float] = None
    wind_speed: Optional[float] = None

