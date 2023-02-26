from typing import Optional
from abc import ABC


class FlyStrategy(ABC):

    def fly(self) -> Optional[str]:
        ...
