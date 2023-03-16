from typing import Protocol


class ObserverInterface(Protocol):
    def update(self, observable, info):
        ...

    def remove(self, observable):
        ...
