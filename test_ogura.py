import os

import cv2
import numpy as np
import pytest
from ogura import solve

plane_kana = "かきくけこさしすせそたちつてとはひふへほはひふへほ"
henka_kana = "がぎぐげござじずぜぞだぢづでどばびぶべぼぱぴぷぺぽ"


@pytest.fixture(scope="session")
def path(pytestconfig):
    return pytestconfig.getoption("path")


def test_solve(path: str):
    base = os.path.splitext(path)[0]
    img_path = path
    txt_path = base + ".txt"
    assert os.path.exists(img_path), f"Image file not found: {img_path:s}"
    assert os.path.exists(txt_path), f"Text file not found: {txt_path:s}"

    dirname = os.path.basename(os.path.dirname(img_path))
    level = int(dirname[-1])

    image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    poems = []
    expected = []
    with open(txt_path) as content:
        for ln in content:
            poem, ans = ln.strip().split()
            poems.append(poem)
            expected.append(int(ans))

    print(poems)

    actual = solve(image, poems, level)

    actual = np.array(actual, dtype="uint8")
    expacted = np.array(expected, dtype="uint8")

    assert (actual == expected).all(), "Your answer is wrong!"
