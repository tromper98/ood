from typing import Protocol


from . import ObserverInterface


class ObservableInterface(Protocol):

    def register_observer(self, observer: ObserverInterface, priority: int):
        ...

    def remove_observer(self, observer: ObserverInterface):
        ...

    def notify_observers(self):
        ...
