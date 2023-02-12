from typing import Protocol, Optional


class FlyStrategy(Protocol):
    def fly(self) -> Optional[str]:
        ...
