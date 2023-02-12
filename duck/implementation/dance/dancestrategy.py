from typing import Protocol, Optional


class DanceStrategy(Protocol):
    def dance(self) -> Optional[str]:
        ...
