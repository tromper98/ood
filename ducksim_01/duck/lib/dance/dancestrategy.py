from typing import Optional
from abc import ABC


class DanceStrategy(ABC):
    def dance(self) -> Optional[str]:
        ...
