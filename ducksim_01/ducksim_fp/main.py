from typing import Callable


# Fly strategies


def fly_no_way() -> Callable:
    def perform_fly():
        return 'Летать не умею'
    return perform_fly


def fly_with_wing() -> Callable:
    # Добавить счетчик полетов Замыкание в помощь.
    fly_count: int = 0

    def perform_fly():
        nonlocal fly_count
        fly_count += 1
        return f'Летим, машем крылышками. Полет по номером {fly_count}'
    return perform_fly


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


class Duck:
    _fly_strategy: Callable
    _quack_strategy: Callable
    _dance_strategy: Callable

    def __init__(self,
                 fly_strategy: Callable,
                 quack_strategy: Callable,
                 dance_strategy: Callable):
        self._fly_strategy = fly_strategy()
        self._quack_strategy = quack_strategy
        self._dance_strategy = dance_strategy

    def fly(self) -> None:
        print(self._fly_strategy())

    def quack(self) -> None:
        print(self._quack_strategy())

    def dance(self) -> None:
        print(self._dance_strategy())

    def display(self) -> None:
        ...

    def set_fly_strategy(self, new_strategy: Callable) -> None:
        self._fly_strategy = new_strategy()

    def set_quack_strategy(self, new_strategy: Callable) -> None:
        self._quack_strategy = new_strategy

    def set_dance_strategy(self, new_strategy: Callable) -> None:
        self._dance_strategy = new_strategy


class ReadheadDuck(Duck):
    def __init__(self):
        super().__init__(fly_with_wing, quack, minuet)

    def display(self) -> None:
        print('Красноголовая уточка')


class MallardDuck(Duck):
    def __init__(self):
        super().__init__(fly_with_wing, quack, minuet)

    def display(self) -> None:
        print('Дикая уточка')


class DecoyDuck(Duck):
    def __init__(self):
        super().__init__(fly_no_way, mute_quack, no_dance)

    def display(self) -> None:
        print('Маннок для уточек')


class RubberDuck(Duck):
    def __init__(self):
        super().__init__(fly_no_way, squeak, no_dance)

    def display(self) -> None:
        print('Резиновая уточка')


readhead_duck = ReadheadDuck()
mallard_duck = MallardDuck()
decoy_duck = DecoyDuck()
rubber_duck = RubberDuck()


readhead_duck.fly()
readhead_duck.fly()
readhead_duck.set_fly_strategy(fly_no_way)

readhead_duck.fly()

readhead_duck.set_fly_strategy(fly_with_wing)
readhead_duck.fly()
readhead_duck.fly()
