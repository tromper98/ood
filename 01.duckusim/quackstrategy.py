from typing import Protocol, Optional


class QuackStrategy(Protocol):
    def quack(self) -> Optional[str]:
        ...
