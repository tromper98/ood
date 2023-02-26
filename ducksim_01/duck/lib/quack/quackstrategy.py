from typing import Optional
from abc import ABC


class QuackStrategy(ABC):
    def quack(self) -> Optional[str]:
        ...
