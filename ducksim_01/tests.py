import pytest

from .duck import *
from .duck.impl.fly import *
from .duck.impl.dance import *
from .duck.impl.quack import *


def test_create_decoy_duck():
    duck = DecoyDuck()
    assert duck.perform_fly() is None
    assert duck.perform_quack() is None
    assert duck.perform_dance() is None
    assert duck.swim() == 'плавает'
    assert duck.display() == 'маннок для уток'
