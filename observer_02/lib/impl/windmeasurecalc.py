import math


class WindMeasureCalc:
    _avg_direction: float
    _avg_speed: float

    _sum_sin: float
    _sum_cos: float

    _calc_count: int

    def __init__(self):
        self._avg_direction = 0.0
        self._avg_speed = 0.0
        self._sum_sin = 0.0
        self._sum_cos = 0.0
        self._calc_count = 0

    def update_values(self, new_speed: float, new_direction: float) -> None:
        self._calc_count += 1
        self._update_avg_wind_parameters(new_speed, new_direction)

    def _update_avg_wind_parameters(self, new_speed: float, new_direction: float) -> None:
        self._sum_sin += new_speed * math.sin(math.radians(new_direction))
        self._sum_cos += new_speed * math.cos(math.radians(new_direction))

        avg_sin = self._sum_sin / self._calc_count
        avg_cos = self._sum_cos / self._calc_count

        self._avg_direction = (math.degrees(math.atan2(avg_sin, avg_cos)) + 360) % 360
        self._avg_speed = math.sqrt(avg_sin * avg_sin + avg_cos * avg_cos)

    @property
    def avg_direction(self) -> float:
        return self._avg_direction

    @property
    def avg_speed(self) -> float:
        return self._avg_speed
