from pathlib import Path

import pytest
from PIL import Image


@pytest.fixture(scope="session")
def image() -> Image.Image:
    return Image.open(Path(__file__).parent / "data" / "imagehash.webp")
