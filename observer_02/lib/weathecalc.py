class WeatherCalc:
    _max_value: float
    _min_value: float
    _sum_value: float
    _avg_value: float

    _calc_count: int

    def __init__(self):
        self._max_value = 0.0
        self._min_value = 0.0
        self._sum_value = 0.0
        self._calc_count = 0
        self._avg_value = 0.0

    def update_values(self, new_value: float) -> None:
        if self._max_value < new_value:
            self._max_value = new_value

        if self._min_value > new_value:
            self._min_value = new_value

        self._calc_count += 1
        self._sum_value += new_value
        self._avg_value = self._sum_value / self._calc_count

    @property
    def max_value(self) -> float:
        return self._max_value

    @property
    def min_value(self) -> float:
        return self._min_value

    @property
    def avg_value(self) -> float:
        return self._avg_value
