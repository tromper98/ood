import pytest

from impl.decorators import *


def test_rle_compress():
    raw_data = 'AAAABBBBCCEEEEEEEEFFFFFFAJS'
    expected = '4A4B2C8E6F1A1J1S'
    result = Compress._rle_compress(raw_data)
    assert expected == result


def test_rle_decompress():
    compressed_data = '4E9H3D17L2A'
    expected = 'EEEEHHHHHHHHHDDDLLLLLLLLLLLLLLLLLAA'
    result = Decompress._rle_decompress(compressed_data)
    assert expected == result


def test_encrypt():
    encrypt = Encrypt(3)
    raw_data = b'Hello World'
    expected = b'Khoor#Zruog'
    result = encrypt.process_block(raw_data)
    assert expected == result
