import pytest

from .duck import *
from .duck.lib.quack import *
from .duck.lib.dance import *
from .duck.lib.fly import *


def test_create_decoy_duck():
    duck = DecoyDuck()
    assert duck.perform_fly() is None
    assert duck.perform_quack() is None
    assert duck.perform_dance() is None
    assert duck.swim() == 'плавает'
    assert duck.display() == 'маннок для уток'


def test_create_rubber_duck():
    duck = RubberDuck()
    assert duck.perform_fly() is None
    assert duck.perform_quack() == 'пищим'
    assert duck.perform_dance() is None
    assert duck.swim() == 'плавает'
    assert duck.display() == 'резиновая уточка'


def test_create_mallard_duck():
    duck = MallardDuck()
    assert duck.perform_fly() == 'летим, машем крылышками. Полет под номером 1'
    assert duck.perform_quack() == 'крякаем'
    assert duck.perform_dance() == 'танцует вальс'
    assert duck.swim() == 'плавает'
    assert duck.display() == 'дикая утка'


def test_create_readhead_duck():
    duck = ReadHeadDuck()
    assert duck.perform_fly() == 'летим, машем крылышками. Полет под номером 1'
    assert duck.perform_quack() == 'крякаем'
    assert duck.perform_dance() == 'танцует менует'
    assert duck.swim() == 'плавает'
    assert duck.display() == 'красноголовая утка'


def test_increase_fly_counter_when_duck_fly():
    duck = MallardDuck()
    duck.perform_fly()
    duck.perform_fly()
    duck.perform_fly()
    assert duck.perform_fly() == 'летим, машем крылышками. Полет под номером 4'


def test_change_quack_strategy():
    duck = RubberDuck()
    assert duck.perform_quack() == 'пищим'
    duck.change_quack_strategy(Quack())
    assert duck.perform_quack() == 'крякаем'


def test_change_dance_strategy():
    duck = DecoyDuck()
    assert duck.perform_dance() is None
    duck.change_dance_strategy(Waltz())
    assert duck.perform_dance() == 'танцует вальс'


def test_change_fly_strategy():
    duck = ReadHeadDuck()
    duck.perform_fly()
    duck.perform_fly()

    assert duck.perform_fly() == 'летим, машем крылышками. Полет под номером 3'
    duck.change_fly_strategy(FlyNoWay())

    assert duck.perform_fly() is None
    duck.change_fly_strategy(FlyWithWings())

    duck.perform_fly()
    duck.perform_fly()
    duck.perform_fly()
    assert duck.perform_fly() == 'летим, машем крылышками. Полет под номером 4'
