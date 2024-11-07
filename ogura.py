import numpy as np
import numpy.typing as npt


def solve(
    image: npt.NDArray[np.uint8],
    poems: list[str],
    level: int,
) -> list[tuple[int, str]]:
    """
    Inputs:
      image: input color image with size (H, W, 3)
      poems: list of Ogura poems
      level: difficulty of the problem (from 1 to 3)
    Outputs:
      answer: list of tuples of integer and string, where integer represent
      the number with which the player can guess the poem, while the string
      represent the poem itself. If the poem is inexistent, the integer should
      be 0, and the string should be an empty one.
    """
    answer = [(0, "")] * len(poems)
    return answer
