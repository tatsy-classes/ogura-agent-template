import numpy as np
import numpy.typing as npt


def solve(image: npt.NDArray[np.uint8], poems: list[str], level: int) -> list[int]:
    """
    Inputs:
      image: input color image with size (H, W, 3)
      poems: list of Ogura poems
      level: difficulty of the problem (from 1 to 3)
    Outputs:
      answer: list of integers, where each integer represent the number
      with which the player can uniquely determine the corresponding poem.
      If the poem is inexistent, the integer is expected to be 0.
    """
    answer = [0] * len(poems)
    return answer
