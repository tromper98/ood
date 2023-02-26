from typing import Protocol


class ObservableInterface(Protocol):

    def register_observer(self, observer):
        ...

    def remove_observer(self, observer):
        ...

    def notify_observers(self):
        ...
