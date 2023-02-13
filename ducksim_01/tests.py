import pytest

from .duck import *


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
    assert duck.perform_fly() == 'летим, машем крылышками'
    assert duck.perform_quack() == 'крякаем'
    assert duck.perform_dance() == 'танцует вальс'
    assert duck.swim() == 'плавает'
    assert duck.display() == 'дикая утка'


def test_create_readhead_duck():
    duck = ReadHeadDuck()
    assert duck.perform_fly() == 'летим, машем крылышками'
    assert duck.perform_quack() == 'крякаем'
    assert duck.perform_dance() == 'танцует менует'
    assert duck.swim() == 'плавает'
    assert duck.display() == 'красноголовая утка'
