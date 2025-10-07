from pathlib import Path

import pytest
from PIL import Image

import imha


@pytest.fixture
def image():
    return Image.open(Path(__file__).parent / "data" / "imagehash.webp")


def test_average_hash(image):
    h = imha.average_hash(image)
    assert h.hex() == "ffd7918181c9ffff"
    assert int(h) == -11380488630829057
    assert len(h) == 64


def test_dhash(image):
    h = imha.dhash(image)
    assert h.hex() == "0026273b2b19550e"
    assert int(h) == 10739184194639118
    assert len(h) == 64


def test_dhash_vertical(image):
    h = imha.dhash_vertical(image)
    assert h.hex() == "002000007eff37fe"
    assert int(h) == 9007201385396222
    assert len(h) == 64
