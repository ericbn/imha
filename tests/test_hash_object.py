import pytest

import imha


def test_hash_128_8():
    h = imha.Hash(128, 8)
    assert h == imha.Hash(128, 8)
    assert h.bin() == "10000000"
    assert h.hex() == "80"
    assert h.uint() == 128
    assert bytes(h) == b"\x80"
    assert int(h) == -128
    assert bin(h) == f"0b{h.bin()}"
    assert len(h) == 8
    assert repr(h) == "Hash(128, 8)"
    assert str(h) == h.hex()


def test_hash_1_16():
    h = imha.Hash(1, 16)
    assert h == imha.Hash(1, 16)
    assert h.bin() == "0000000000000001"
    assert h.hex() == "0001"
    assert h.uint() == 1
    assert bytes(h) == b"\x00\x01"
    assert int(h) == 1
    assert bin(h) == "0b1"
    assert len(h) == 16
    assert repr(h) == "Hash(1, 16)"
    assert str(h) == h.hex()


def test_hash_16777214_24():
    h = imha.Hash(16777214, 24)
    assert h == imha.Hash(16777214, 24)
    assert h.bin() == "111111111111111111111110"
    assert h.hex() == "fffffe"
    assert h.uint() == 16777214
    assert bytes(h) == b"\xff\xff\xfe"
    assert int(h) == -2
    assert bin(h) == f"0b{h.bin()}"
    assert len(h) == 24
    assert repr(h) == "Hash(16777214, 24)"
    assert str(h) == h.hex()


def test_hash_0_32():
    h = imha.Hash(0, 32)
    assert h == imha.Hash(0, 32)
    assert h.bin() == "0" * 32
    assert h.hex() == "0" * 8
    assert h.uint() == 0
    assert bytes(h) == b"\x00" * 4
    assert int(h) == 0
    assert bin(h) == "0b0"
    assert len(h) == 32
    assert repr(h) == "Hash(0, 32)"
    assert str(h) == h.hex()


def test_hash_4398046511103_42():
    h = imha.Hash(4398046511103, 42)
    assert h == imha.Hash(4398046511103, 42)
    assert h.bin() == "1" * 42
    assert h.hex() == "3ffffffffff"
    assert h.uint() == 4398046511103
    assert bytes(h) == b"\x03\xff\xff\xff\xff\xff"
    assert int(h) == 4398046511103
    assert bin(h) == f"0b{h.bin()}"
    assert len(h) == 42
    assert repr(h) == "Hash(4398046511103, 42)"
    assert str(h) == h.hex()


def test_hash_18369614221190020847_64():
    h = imha.Hash(18369614221190020847, 64)
    assert h == imha.Hash(18369614221190020847, 64)
    assert h.bin() == "1111111011101101111110101100111011001010111111101011111011101111"
    assert h.hex() == "feedfacecafebeef"
    assert h.uint() == 18369614221190020847
    assert bytes(h) == b"\xfe\xed\xfa\xce\xca\xfe\xbe\xef"
    assert int(h) == -77129852519530769
    assert bin(h) == f"0b{h.bin()}"
    assert len(h) == 64
    assert repr(h) == "Hash(18369614221190020847, 64)"
    assert str(h) == h.hex()


def test_hash_sub():
    distance = imha.Hash(128, 8) - imha.Hash(0, 8)
    assert distance == 1


def test_hash_sub_different_type():
    with pytest.raises(TypeError, match="other must be a hash object"):
        imha.Hash(128, 8) - b"\x00"


def test_hash_sub_different_len():
    with pytest.raises(ValueError, match="hash objects must be of the same length"):
        imha.Hash(128, 8) - imha.Hash(0, 4)


def test_hash_negative_value():
    with pytest.raises(ValueError, match="value must be >= 0"):
        imha.Hash(-1, 8)
