from pathlib import Path

import pytest
from PIL import Image

import imha

FUNC_PARAMS = [
    pytest.param(imha.average_hash, id="average_hash"),
    pytest.param(imha.dhash, id="dhash"),
    pytest.param(imha.dhash_vertical, id="dhash_vertical"),
]


@pytest.fixture
def image():
    return Image.open(Path(__file__).parent / "data" / "imagehash.webp")


@pytest.mark.parametrize("func", FUNC_PARAMS)
def test_hash_function(func, image):
    hash1 = func(image)
    image2 = image.rotate(-1)
    hash2 = func(image2)
    distance = hash1 - hash2
    assert distance <= 10
    image2 = image.rotate(-90)
    hash2 = func(image2)
    distance = hash1 - hash2
    assert distance > 10


@pytest.mark.parametrize("size", range(-1, 1))
@pytest.mark.parametrize("func", FUNC_PARAMS)
def test_hash_function_size(func, image, size):
    with pytest.raises(ValueError, match="height and width must be > 0"):
        func(image, (size, size))
