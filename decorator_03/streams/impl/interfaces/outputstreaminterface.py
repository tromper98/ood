from typing import Protocol


class OutputStreamInterface(Protocol):

    def write_byte(self, data):
        ...

    def write_block(self, data, size):
        ...
