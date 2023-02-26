from typing import Protocol


class ObserverInterface(Protocol):
    def update(self):
        ...
