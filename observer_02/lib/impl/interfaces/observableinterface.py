from typing import Protocol


from . import ObserverInterface


class ObservableInterface(Protocol):

    def register_observer(self, observer: ObserverInterface, priority: int) -> None:
        ...

    def remove_observer(self, observer: ObserverInterface) -> None:
        ...

    def notify_observers(self, info) -> None:
        ...

    def get_info(self) -> str:
        ...
