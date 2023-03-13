from typing import Optional

from .interfaces import *


class StreamDecorator(InputStreamInterface, OutputStreamInterface):
    _input_stream: InputStreamInterface
    _output_stream: OutputStreamInterface

    def is_EOF(self):
        ...

    def read_byte(self):
        ...

    def read_block(self, data, size):
        ...

    def write_byte(self, data):
        ...

    def write_block(self, data, size):
        ...

    def process_byte(self):
        ...

    def process_block(self):
        ...


class Compress(StreamDecorator):
    def process_byte(self):
        ...

    def process_block(self):
        ...

    @staticmethod
    def _rle_compress(data) -> str:
        compressed_data: str = ''
        prev_char: str = ''
        count: int = 1

        if not data:
            return ''

        for char in data:
            if char != prev_char:
                if prev_char:
                    compressed_data += str(count) + prev_char
                count = 1
                prev_char = char
            else:
                count += 1

        compressed_data += str(count) + prev_char
        return compressed_data


class Decompress(StreamDecorator):
    def process_byte(self):
        ...

    def process_block(self):
        ...

    @staticmethod
    def _rle_decompress(data: str) -> str:
        decompressed_data: str = ''
        count: str = ''

        for char in data:
            if char.isdigit():
                count += char
            else:
                decompressed_data += char * int(count)
                count = ''
        return decompressed_data


class Encrypt(StreamDecorator):
    def process_byte(self):
        ...

    def process_block(self):
        ...


class Decrypt(StreamDecorator):
    def process_byte(self):
        ...

    def process_block(self):
        ...
