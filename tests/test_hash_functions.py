from __future__ import annotations

from typing import TYPE_CHECKING, Final

import pytest

import imha

if TYPE_CHECKING:
    from collections.abc import Callable

    from PIL import Image

FUNC_PARAMS: Final = [
    pytest.param(imha.average_hash, id="average_hash"),
    pytest.param(imha.dhash, id="dhash"),
    pytest.param(imha.dhash_vertical, id="dhash_vertical"),
]


@pytest.mark.parametrize("func", FUNC_PARAMS)
def test_hash_function(
    func: Callable[[Image.Image], imha.Hash], image: Image.Image
) -> None:
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
def test_hash_function_size(
    func: Callable[[Image.Image, tuple[int, int]], imha.Hash],
    image: Image.Image,
    size: int,
) -> None:
    with pytest.raises(ValueError, match="height and width must be > 0"):
        func(image, (size, size))
