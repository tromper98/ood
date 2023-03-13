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

    def process_byte(self, byte):
        ...

    def process_block(self, data):
        ...


class Compress(StreamDecorator):
    def process_byte(self, byte):
        ...

    def process_block(self, data):
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
    def process_byte(self, byte):
        ...

    def process_block(self, data):
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
    _alphabet: list
    _encryption_key: int

    def __init__(self, encryption_key: int):
        self._alphabet = self._create_byte_array()
        self._encryption_key = encryption_key

    def process_byte(self, byte) -> bytes:
        return self._encrypt_byte(byte)

    def process_block(self, data: bytearray) -> bytearray:
        encrypted = []
        for byte in data:
            encrypted.append(self._encrypt_byte(bytes(byte)))
        return encrypted

    def _encrypt_byte(self, byte: bytes) -> bytes:
        shift = self._encryption_key - 256 * (self._encryption_key // 256)
        pos = self._alphabet.index(byte)
        return self._alphabet[pos + shift]

    @staticmethod
    def _create_byte_array() -> list:
        byte_arr = []
        for i in range(256):
            byte_arr.append(bytes(i))

        return byte_arr + byte_arr


class Decrypt(StreamDecorator):
    def process_byte(self, byte):
        ...

    def process_block(self, data):
        ...
