from typing import Optional

from .impl.quack import QuackStrategy
from .impl.fly import FlyStrategy
from .impl.dance import DanceStrategy


class Duck:
    _quack_strategy: QuackStrategy
    _fly_strategy: FlyStrategy
    _dance_strategy: DanceStrategy

    def __init__(self, quack_strategy: QuackStrategy, fly_strategy: FlyStrategy, dance_strategy: DanceStrategy):
        self._quack_strategy = quack_strategy
        self._fly_strategy = fly_strategy
        self._dance_strategy = dance_strategy

    def perform_quack(self) -> Optional[str]:
        return self._quack_strategy.quack()

    def perform_fly(self) -> Optional[str]:
        return self._fly_strategy.fly()

    def perform_dance(self) -> Optional[str]:
        return self._dance_strategy.dance()

    @staticmethod
    def display() -> str:
        ...

    @staticmethod
    def swim() -> str:
        return 'плавает'
