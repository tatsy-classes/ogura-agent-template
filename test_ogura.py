import os
import sys
import glob
import argparse
from pathlib import Path

import cv2
import numpy as np
import pytest

from ogura import solve

CUR_DIR: str = os.path.dirname(os.path.abspath(__file__))
DATA_DIR: str = os.path.join(CUR_DIR, "data")


def get_test_data() -> list[tuple[str, int]]:
    rng = np.random.RandomState(31415)

    levels = [1, 2, 3]
    data = []
    for level in levels:
        image_paths = glob.glob(str(Path(DATA_DIR) / f"level{level:d}/*.jpg"))
        if len(image_paths) > 10:
            idx = rng.choice(len(image_paths), 10)
            image_paths = [image_paths[i] for i in idx]
            image_paths = sorted(image_paths)
        data.extend([(path, level) for path in image_paths])

    return data


def check(path: str, level: int) -> None:
    img_path = Path(path)
    txt_path = img_path.with_suffix(".txt")
    assert img_path.exists(), f"Image file not found: {str(img_path):s}"
    assert txt_path.exists(), f"Text file not found: {str(txt_path):s}"

    # load input image
    image = cv2.imread(str(img_path), cv2.IMREAD_COLOR)
    if image is None:
        raise FileNotFoundError(f"Failed to read image file: {img_path:s}")

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = image.astype("uint8")

    kami = []
    expected = []
    with open(txt_path, mode="r", encoding="utf-8") as content:
        for ln in content:
            kami.append(ln.strip().split()[0])
            expected.append(int(ln.strip().split()[1]))

    predicted = solve(image, kami, level)
    for e, p in zip(expected, predicted):
        assert e == p, f"Expected: {e:d}, Predicted: {p:d}"


@pytest.mark.parametrize("image_path, level", get_test_data())
def test_solve(image_path: str, level: int) -> None:
    check(image_path, level)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("image_path", type=str, help="Path to the image file")
    parser.add_argument("level", type=int, help="Level of the problem")
    args = parser.parse_args()

    check(args.image_path, args.level)
