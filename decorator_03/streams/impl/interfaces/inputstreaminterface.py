from typing import Protocol


class InputStreamInterface(Protocol):

    def is_E0F(self):
        ...

    def read_byte(self):
        ...

    def read_block(self, data, size):
        ...
