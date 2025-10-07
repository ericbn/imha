from __future__ import annotations

from typing import TYPE_CHECKING

import imha

if TYPE_CHECKING:
    from PIL import Image


def test_average_hash_16(image: Image.Image) -> None:
    h = imha.average_hash(image, (4, 4))
    assert h.hex() == "f00f"
    assert int(h) == -4081
    assert len(h) == 16


def test_dhash_16(image: Image.Image) -> None:
    h = imha.dhash(image, (5, 4))
    assert h.hex() == "5552"
    assert int(h) == 21842
    assert len(h) == 16


def test_dhash_16_skip_corners(image: Image.Image) -> None:
    h = imha.dhash(image, (6, 4), skip_corners=True)
    assert h.hex() == "a92b"
    assert int(h) == -22229
    assert len(h) == 16


def test_dhash_128(image: Image.Image) -> None:
    h = imha.dhash(image, (13, 11), skip_corners=True)
    assert h.hex() == "00066265ca5850cc8caac94c94c96c1c"
    assert int(h) == 33149521959519788799173856787524636
    assert len(h) == 128


def test_dhash_vertical_16(image: Image.Image) -> None:
    h = imha.dhash_vertical(image, (4, 5))
    assert h.hex() == "00ff"
    assert int(h) == 255
    assert len(h) == 16


def test_dhash_vertical_16_skip_corners(image: Image.Image) -> None:
    h = imha.dhash_vertical(image, (5, 5), skip_corners=True)
    assert h.hex() == "00ff"
    assert int(h) == 255
    assert len(h) == 16


def test_dhash_vertical_128(image: Image.Image) -> None:
    h = imha.dhash_vertical(image, (12, 12), skip_corners=True)
    assert h.hex() == "000000768084000f31df9ff8329a3bfb"
    assert int(h) == 9388696836428808063907677223931
    assert len(h) == 128
