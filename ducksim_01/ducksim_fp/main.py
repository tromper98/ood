from typing import Callable, Optional


# Fly strategies


def fly_no_way() -> str:
    return 'Летать не умею'


def fly_with_wing() -> str:
    return 'Летим, машем крылышками'


# Quack strategies


def mute_quack() -> str:
    return ''


def quack() -> str:
    return 'Кря'


def squeak() -> str:
    return 'Писк'


# dance strategies

def minuet() -> str:
    return 'Танцуем минует'


def waltz() -> str:
    return 'Танцуем вальс'


def no_dance() -> str:
    return ''


class DuckContext:
    _name: str
    _fly_strategy: Callable
    _quack_strategy: Callable
    _dance_strategy: Callable

    def __init__(self,
                 name: str,
                 fly_strategy: Callable,
                 quack_strategy: Callable,
                 dance_strategy: Callable):
        self._name = name
        self._fly_strategy = fly_strategy
        self._quack_strategy = quack_strategy
        self._dance_strategy = dance_strategy

    def use_fly_strategy(self) -> None:
        print(self._fly_strategy())

    def use_quack_strategy(self) -> None:
        print(self._quack_strategy())

    def use_waltz_strategy(self) -> None:
        print(self._dance_strategy())

    def display_name(self) -> None:
        print(self._name)

    def set_fly_strategy(self, new_strategy: Callable) -> None:
        self._fly_strategy = new_strategy

    def set_quack_strategy(self, new_strategy: Callable) -> None:
        self._quack_strategy = new_strategy

    def set_dance_strategy(self, new_strategy: Callable) -> None:
        self._dance_strategy = new_strategy


readhead_duck = DuckContext('Красноголовая уточка', fly_with_wing, quack, minuet)
mallard_duck = DuckContext('Дикая уточка', fly_with_wing, quack, waltz)
decoy_duck = DuckContext('Маннок для уток', fly_no_way, mute_quack, no_dance)
rubber_duck = DuckContext('Резиновая уточка', fly_no_way, squeak, no_dance)

pass
