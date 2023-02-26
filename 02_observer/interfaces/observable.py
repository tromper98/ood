from typing import Protocol


from .observer import ObserverInterface


class ObservableInterface(Protocol):

    def register_observer(self, observer: ObserverInterface):
        ...

    def remove_observer(self, observer: ObserverInterface):
        ...

    def notify_observers(self):
        ...
