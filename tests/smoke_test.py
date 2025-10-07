from pathlib import Path

from PIL import Image

import imha

h = imha.average_hash(Image.open(Path(__file__).parent / "data" / "imagehash.webp"))
assert int(h) == -11380488630829057
