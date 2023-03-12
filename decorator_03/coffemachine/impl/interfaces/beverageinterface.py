from typing import Protocol


class BeverageInterface(Protocol):

    def get_description(self) -> str:
        ...

    def get_cost(self) -> float:
        ...
