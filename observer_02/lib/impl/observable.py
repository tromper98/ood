from typing import Dict
from collections import OrderedDict

from .interfaces import ObservableInterface, ObserverInterface


class Observable(ObservableInterface):
    _observers: Dict[ObserverInterface, float]

    def __init__(self):
        self._observers = {}

    def register_observer(self, observer: ObserverInterface, priority: int):
        self._observers[observer] = priority
        sorted_observers = sorted(self._observers.items(), key=lambda x: x[1])
        self._observers = OrderedDict(sorted_observers)
        # Обычный dict не гарантирует сохранения порядка вставки

    def remove_observer(self, observer: ObserverInterface):
        self._observers.pop(observer)

    def notify_observers(self, info):
        for observer in self._observers:
            observer.update(self, info)
            # Проверить как обновляется коллекция при изменении ее в процессе итерации
            # Выпадает ошибка RuntimeError: dictionary changed size during iteration
            # Поддержать возможность добавлять или удалять во время notify
